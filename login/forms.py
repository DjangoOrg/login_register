# !usr/bin/env python3
# -*- coding:utf-8 -*- 
"""
@project = mysite
@file = forms
@author = Easton Liu
@time = 2018/11/25 21:29
@Description: 

"""
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=255,label="用户名")
    password = forms.CharField(max_length=255,label="密码",widget=forms.PasswordInput)
