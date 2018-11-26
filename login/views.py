from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.session.get('is_login'):
        return redirect('/index/')
    if request.method=="POST":
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写!"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_name'] = user.name
                    request.session['user_id'] = user.id
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        return render(request,'login/login.html',locals())
    login_form = forms.UserForm()
    return render(request,'login/login.html',locals())
def register(request):
    if request.session.get('is_login'):
        return redirect('/index/')
    if request.method == 'POST':
        register_form = forms.RegisretForm(request.POST)
        message = "请检查填写内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            mobile_phone = register_form.cleaned_data['mobile_phone']
            if password1!=password2:
                message = "两次输入的密码不同！"
                return render(request,'login/register.html',locals())
            else :
                same_name = models.User.objects.filter(name=username)
                if same_name:
                    message = "用户名已存在，请输入别的用户名！"
                    return render(request, 'login/register.html', locals())
                same_email = models.User.objects.filter(email=email)
                if same_email:
                    message = "该邮箱地址已被注册，请使用别的邮箱！"
                    return render(request, 'login/register.html', locals())
                same_mobil_phone = models.User.objects.filter(mobile_phone=mobile_phone)
                if same_mobil_phone:
                    message = "该手机号码已被注册，请使用别的手机号码！"
                    return render(request, 'login/register.html', locals())
                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.mobile_phone = mobile_phone
                new_user.save()
                return redirect('/login/')
    register_form = forms.RegisretForm()
    return render(request,'login/register.html',locals())
def logout(request):
    # if not request.session.get('is_login'):
    #     return redirect('/index/')
    request.session.flush()
    return redirect('/index/')
