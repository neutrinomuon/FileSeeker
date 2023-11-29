'''Setup for FileSeeker installation'''
# --------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

# from setuptools import Extension
from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

with open("version.txt","r",encoding="utf-8") as vh:
    version_description = vh.read()

setup( name='FileSeeker',
       version=version_description,
       description=('FileSeeker is a Python package for finding a given'
                   'file or name in a given file within a given'
                   'directory with color-coded representation.'),
       long_description=long_description, # Long description read from the the readme file
       long_description_content_type="text/markdown",
       author='Jean Gomes',
       author_email='antineutrinomuon@gmail.com',
       url='https://github.com/neutrinomuon/FileSeeker',
       install_requires=[ 'numpy','matplotlib' ],
       classifiers=[
           "Programming Language :: Python :: 3",
           "Operating System :: OS Independent",
                   ],
       package_dir={"fileseeker": "src/python"},
       packages=['fileSeeker'],
       data_files=[('', ['LICENSE.txt','version.txt']),],
      )
