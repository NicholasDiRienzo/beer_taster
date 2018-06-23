#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 08:47:39 2018

@author: nick
"""

from wtforms import Form, validators, StringField

class InputForm(Form):

    good = StringField(
        label='things you like', 
        validators=[validators.InputRequired()])
    bad = StringField(
        label='things you do not like')
