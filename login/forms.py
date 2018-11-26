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
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(max_length=255,label="用户名",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=255,label="密码",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label="验证码")
class RegisretForm(forms.Form):
    gender =(
        ('male','男'),
        ('female','女')
    )
    username = forms.CharField(max_length=255,label="用户名",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=255,label="密码",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=255,label="确认密码",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="邮箱",widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex = forms.ChoiceField(label="性别",choices=gender)
    mobile_phone = forms.CharField(max_length=11,label='手机号码',widget=forms.TextInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label="验证码")