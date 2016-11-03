# -*- coding:utf-8 -*-
#coding=utf-8
__author__ = 'lihui'

from flask_wtf import Form
from wtforms import TextAreaField,SubmitField,validators,SelectField
from wtforms.validators import Required

class InceptionTableStructure(Form):
    db_name = SelectField(u'selectdb', choices=[('default', '')])
    table_name = TextAreaField('请输入需要评审的表结构: ', validators=[Required()])
    submit = SubmitField('Submit')
