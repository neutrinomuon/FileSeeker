from setuptools import Extension
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as vh:
    version_description = vh.read()
    
setup( name='FileSeeker',
       version=version_description,
       description='FileSeeker is a Python package for finding a given file or name in a given file within a given directory with color-coded representation.',
       long_description=long_description,      # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/FileSeeker',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
           "Operating System :: OS Independent",
                   ],
       package_dir={"FileSeeker": "src/python", "fileseeker": "src/python"},
       packages=['FileSeeker'],
       data_files=[('', ['LICENSE.txt','version.txt']),],
      )
    
