try:
    from setuptools import setup, find_packages #enables develop
except ImportError:
    from distutils.core import setup, find_packages
import pathlib

install_requires = [
    'kaldi_io',
    'tqdm',
    'matplotlib',
    'numpy',
    'torch',
    'librosa',
    'pandas',
    'pysptk',
    'phonet',
    'scipy',
    'scikit_learn',
]

HERE = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

setup(
    name='disvoice',
    version='0.2.0',
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    install_requires=install_requires,
    package_data={'': ['audios/*', "*.praat", "*.pt"]},
    dependency_links=['git+git://github.com/jameslyons/python_speech_features'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
        "Topic :: Scientific/Engineering",
    ]
)
