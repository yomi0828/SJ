from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from account.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class UserForm(forms.ModelForm):
    username = forms.CharField(label='帳號')
    password = forms.CharField(widget=forms.PasswordInput(), label='密碼')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='確認密碼')
    class Meta:
        model = User
        fields = ('username', 'password')

def clean_password2(self):
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password and password2 and password!=password2:
        raise forms.ValidationError('密碼不相符')
    return password2

class UserProfileForm(forms.ModelForm):
    fullName = forms.CharField(max_length=128, label='姓名')
    website = forms.CharField(max_length=128, label='個人網址')
    address = forms.CharField(max_length=128, label='住址')
    class Meta:
        model = UserProfile
        fields = ('fullName', 'website', 'address')
def register(request):
    template = 'account/register.html'
    if request.method=='GET':
        return render(request, template, {'userForm':UserForm(),
                                          'userProfileForm':UserProfileForm()})
 # request.method == 'POST':
    userForm = UserForm(request.POST)
    userProfileForm = UserProfileForm(request.POST)
    if not (userForm.is_valid() and userProfileForm.is_valid()):
        return render(request, template, {'userForm':userForm,
                                          'userProfileForm':userProfileForm})
    user = userForm.save()
    user.set_password(user.password)
    user.save()
    userProfile = userProfileForm.save(commit=False)
    userProfile.user = user
    userProfile.save()
    messages.success(request, '歡迎註冊')
    return redirect(reverse('main:main'))
def userLogin(request):
    template = 'account/userLogin.html'
    if request.method=='GET':
        return render(request, template)
 # request.method=='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if not user: # authenticate fail
        return render(request, template, {'error':'登入失敗'})
    if not user.is_active:
        return render(request, template, {'error':'帳號已停用'})
 # login success
    login(request, user)
    messages.success(request, '登入成功')
    return redirect(reverse('main:main'))
@login_required
def userLogout(request):
    logout(request)
    messages.success(request, '登出成功')
    return redirect(reverse('main:main'))