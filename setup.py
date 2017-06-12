from setuptools import setup, find_packages
import subprocess

with open('VERSION.txt') as fs:
    VERSION = fs.read().strip()

with open('requirements.txt') as fs:
    REQUIREMENTS = fs.read().strip().split('\n')

def readme():
    with open('README.rst') as fs:
        return fs.read()

setup(name='gisplus',
      version=VERSION,
      long_description=readme(),
      description='Lecture notes for GIS+ at University of Freiburg.',
      author='João Paulo Pereira',
      author_email='joao.pereira@felis.uni-freiburg.de',
      license='MIT',
      packages=find_packages(),
      install_requires=REQUIREMENTS,
      include_package_data=True,
      zip_safe=False

)