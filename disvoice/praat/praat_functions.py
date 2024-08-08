
import os
import sys
import subprocess

import numpy as np


PATH = os.path.dirname(os.path.realpath(__file__))


def multi_find(s, r):
	"""
	Internal function used to decode the Formants file generated by Praat.
	"""
	s_len = len(s)
	r_len = len(r)
	_complete = []
	for i in range(s_len):
		# search for r in s until not enough characters are left
		if s[i:i + r_len] == r:
			_complete.append(i)
		else:
			i = i + 1
	return _complete


def run_praat_script(script_name, arguments):
    """
    Helper function to run a Praat script with specified arguments.

    :param script_name: Name of the Praat script to run
    :param arguments: List of arguments to pass to the script
    :returns: None
    """
    praat_executable = "praat.exe" if sys.platform.startswith('win') else "praat"
    command = [praat_executable, "--run", script_name] + arguments

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result.check_returncode()
    except subprocess.CalledProcessError as e:
        print(f"Error executing Praat script {script_name}: {e.stderr.decode()}")
    except FileNotFoundError:
        print(f"Praat executable not found. Ensure that Praat is installed and added to PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def praat_vuv(audio_filename, resultsp, resultst, time_stepF0=0, minf0=75, maxf0=600, maxVUVPeriod=0.02, averageVUVPeriod=0.01):
    """
    Runs vuv_praat script to obtain pitch and voicing decisions for a wav file.
    Writes the results into two text files: one for pitch and another for voicing decisions.

    :param audio_filename: Full path to the wav file
    :param resultsp: Full path to the resulting file with the pitch
    :param resultst: Full path to the resulting file with the voiced/unvoiced decisions
    :param time_stepF0: Time step to compute the pitch, default is 0 (Praat uses 0.75 / minf0)
    :param minf0: Minimum frequency for the pitch in Hz, default is 75Hz
    :param maxf0: Maximum frequency for the pitch in Hz, default is 600Hz
    :param maxVUVPeriod: Maximum interval considered part of a larger voiced interval, default 0.02s
    :param averageVUVPeriod: Half of this value is taken as the amount to extend a voiced interval beyond its initial and final points, default 0.01s
    :returns: None
    """
    script_path = os.path.join(PATH, "vuv_praat.praat")
    arguments = [
        audio_filename,
        resultsp,
        resultst,
        str(minf0),
        str(maxf0),
        str(time_stepF0),
        str(maxVUVPeriod),
        str(averageVUVPeriod)
    ]

    run_praat_script(script_path, arguments)


def praat_formants(audio_filename, results_filename, sizeframe, step, n_formants=5, max_formant=5500):
    """
    Runs FormantsPraat script to obtain formants for a wav file.
    Writes the results into a text file.

    :param audio_filename: Full path to the wav file
    :param results_filename: Full path to the resulting file with the formants
    :param sizeframe: Window size
    :param step: Time step to compute formants
    :param n_formants: Number of formants to look for, default is 5
    :param max_formant: Maximum frequency of formants to look for, default is 5500Hz
    :returns: None
    """
    script_path = os.path.join(PATH, "FormantsPraat.praat")
    arguments = [
        audio_filename,
        results_filename,
        str(n_formants),
        str(max_formant),
        str(float(sizeframe) / 2),
        str(float(step))
    ]

    run_praat_script(script_path, arguments)


def read_textgrid_trans(file_textgrid, data_audio, fs, win_trans=0.04):
	"""
	This function reads a text file with the text grid with voiced/unvoiced
	decisions then finds the onsets (unvoiced -> voiced) and
	offsets (voiced -> unvoiced) and then reads the audio data to returns
	lists of segments of lenght win_trans around these transitions.

	:param file_textgrid: The text file with the text grid with voicing decisions.
	:param data_audio: the audio signal.
	:param fs: sampling frequency of the audio signal.
	:param win_trans: the transition window lenght, default 0.04
	:returns segments: List with both onset and offset transition segments.
	:returns segments_onset: List with onset transition segments
	:returns segments_offset: List with offset transition segments
	"""
	segments=[]
	segments_onset=[]
	segments_offset=[]
	prev_trans=""
	prev_line=0
	with open(file_textgrid) as fp:
		for line in fp:
			line = line.strip('\n')
			if line in ('"V"', '"U"'):
				transVal=int(float(prev_line)*fs)-1
				segment=data_audio[int(transVal-win_trans*fs):int(transVal+win_trans*fs)]
				segments.append(segment)
				if prev_trans in ('"V"', ""):
					segments_onset.append(segment)
				elif prev_trans=='"U"':
					segments_offset.append(segment)
				prev_trans=line
			prev_line=line
	return segments,segments_onset,segments_offset


def decodeF0(fileTxt,len_signal=0, time_stepF0=0):
	"""
	Reads the content of a pitch file created with praat_vuv function.
	By default it will return the contents of the file in two arrays,
	one for the actual values of pitch and the other with the time stamps.
	Optionally the lenght of the signal and the time step of the pitch
	values can be provided to return an array with the full pitch contour
	for the signal, with padded zeros for unvoiced segments.

	:param fileTxt: File with the pitch, which can be generated using the function praat_vuv
	:param len_signal: Lenght of the audio signal in
	:param time_stepF0: The time step of pitch values. Optional.
	:returns pitch: Numpy array with the values of the pitch.
	:returns time_voiced: time stamp for each pitch value.
	"""
	if os.stat(fileTxt).st_size==0:
		return np.array([0]), np.array([0])
	pitch_data=np.loadtxt(fileTxt)
	if len(pitch_data.shape)>1:
		time_voiced=pitch_data[:,0] # First column is the time stamp vector
		pitch=pitch_data[:,1] # Second column
	elif len(pitch_data.shape)==1: # Only one point of data
		time_voiced=pitch_data[0] # First datum is the time stamp
		pitch=pitch_data[1] # Second datum is the pitch value
	if len_signal>0:
		n_frames=int(len_signal/time_stepF0)
		t=np.linspace(0.0,len_signal,n_frames)
		pitch_zeros=np.zeros(int(n_frames))
		if len(pitch_data.shape)>1:
			for idx,time_p in enumerate(time_voiced):
				argmin=np.argmin(np.abs(t-time_p))
				pitch_zeros[argmin]=pitch[idx]
		else:
			argmin=np.argmin(np.abs(t-time_voiced))
			pitch_zeros[argmin]=pitch
		return pitch_zeros, t
	return pitch, time_voiced


def decodeFormants(fileTxt):
	"""
	Read the praat textgrid file for formants and return the array
	
	:param fileTxt: File with the formants, which can be generated using the '''praat_formants'''
	:returns F1: Numpy array containing the values for the first formant
	:returns F2: Numpy array containing the values for the second formant
	"""
	with open(fileTxt, 'r') as fid:
		datam=fid.read()
	fid.close()
	end_line1=multi_find(datam, '\n')
	F1=[]
	F2=[]
	ji=10
	while (ji<len(end_line1)-1):
		line1=datam[end_line1[ji]+1:end_line1[ji+1]]
		cond=(line1 in ('3', '4', '5'))
		if (cond):
			F1.append(float(datam[end_line1[ji+1]+1:end_line1[ji+2]]))
			F2.append(float(datam[end_line1[ji+3]+1:end_line1[ji+4]]))
		ji=ji+1
	F1=np.asarray(F1)
	F2=np.asarray(F2)
	return F1, F2
