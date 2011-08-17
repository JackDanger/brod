#!/usr/bin/env python

import setuptools

# Don't install deps for development mode.
setuptools.bootstrap_install_from = None

setuptools.setup(
  name = 'pykafka',
  version = '1.0.0',
  license = 'MIT',
  description = open('README.md').read(),
  author = "Dan Sully",
  author_email = "dsully@gmail.com",
  url = 'http://github.com/dsully/pykafka',
  platforms = 'any',

  # What are we packaging up?
  packages = ['kafka'],

  tests_require = [
    'nose',
    'ludibrio',
  ],

  zip_safe = True,
  verbose = False,
)
