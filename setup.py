# coding: utf-8

from distutils.core import setup
import yapredict

setup(name='yapredict',
      version=yapredict.__version__,
      description='Simple wrapper for Yandex prediction typing API.',
      packages=['yapredict'],
      package_dir={'yapredict': 'yapredict'},
      provides=['yapredict'],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      long_description=open('README.md').read(),
      platforms=['All'],
      )
