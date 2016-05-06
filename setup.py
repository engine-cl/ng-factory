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
        """When setup_tools find_packages fail because are not installed or something
        this overwrite it and return default package.
        :return: list
        """
        return ['ng_factory']

setup(
    name='ng_factory',
    version='1.0',
    description='Factory ',
    author='Jorge A. Medina',
    author_email='jorge@engine.cl',
    url='http://github.com/engine-cl/ng-factory',
    packages=find_packages(),
    license='BSD',
    keywords=['factory', 'introspective'],
)
