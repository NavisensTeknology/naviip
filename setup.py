#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#
# @name   : Infoga - Email OSINT
# @url    : http://github.com/NavisensTeknology
# @author : Momo Outaadi (NavisensTeknology)

from setuptools import setup 

setup(
    name='infoga',

    version='0.1.5',
    description='Email OSINT',
    url='https://github.com/NavisensTeknology',
    
    author = 'Momo (NavisensTeknology) Outaadi',
    author_email='destek@navisensteknology.com.tr',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['navi.py'],
)