try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from os import path

import priest

here = path.abspath(path.dirname(__file__))


setup(
  name = 'priest',
  packages=find_packages(),
  version = priest.__version__,
  include_package_data=True,
  description = 'Generate wishes from your command line with full customization.',
  author = 'Ankush Sharma',
  author_email = 'ankprahsar@gmail.com',
  url = 'https://github.com/black-perl/priest', 
  download_url = 'https://github.com/black-perl/priest/tarball/0.5', 
  keywords = ['priest', 'automated-wishes'], 
  license='MIT',
  install_requires=[
  'requests==2.31.0',
  'pytz==2015.4',
  'goslate==1.4.0'
  ]
  
)