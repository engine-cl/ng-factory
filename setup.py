# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Description
__author__ = 'themanda'

from distutils.core import setup
try:
    from setup_tools import find_packages
except ImportError:
    def find_packages():
        return ['ng_factory']
setup(name='ng_factory',
      version='1.0',
      description='Factory ',
      author='Jorge A. Medina',
      author_email='jorge_at_engine_dot_cl',
      url='http://github.com/mnothic/factory_poc',
      packages=find_packages(),
      license='BSD')
