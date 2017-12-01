from django.shortcuts import render,render_to_response


from django.http import  HttpResponse,HttpResponseRedirect

# Create your views here.

from django import  forms
from django.template import  RequestContext
from  django.contrib import  auth
from  .models import User
import  time


#主页
def home(request):
    #return  HttpResponse("hello world")
    #return render(request,'home/zz.html')

    data = [1,2,3,4,5,6,7,8]

    return render(request,'home/index.html',{'data':data})

#    登录
def login(request):





    return render(request,'home/login.html')





# 注册
def  register(request):
    curtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if request.method == "POST":
        uf = UserForm(request.POST)
        #获取表单信息
        if uf.is_valid():
            username = uf.cleaned_data['username']
            filterResult = User.objects.filter(username=username)
            # 从home_user 表中获取数据
            if len(filterResult) > 0:
                return render_to_response('home/register.html',{'error':'用户已存在'})
        else:
            password1 = uf.cleaned_data['password1']
            password2 = uf.cleaned_data['password2']
            error = []
            if (password1 != password2):
                error.append("两次输入的密码不一致！！")
                return render_to_response('home/register.html',{'error':error})
            password = password2
            email = uf.cleaned_data['email']
            user = User.objects.create(username=username,password=password2,email=email)
            user.save()
            return  render_to_response('home/successful.html',{'username':username,'operation':"注册"})
    else:
        uf = UserForm()
    return  render_to_response('home/register.html',{'uf':uf})

   # return  render(request,'home/register.html')      直接跳转到注册页




#查找
def search(request):
    return  render(request,'home/search.html')







#退出
def logout(request):
    return  render(request,'home/login.html')

class UserForm(forms.Form):
    username = forms.CharField(label='昵称',max_length=50)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')

class UserFormLogin():
    username = forms.CharField(label='昵称',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


# 登陆后用户看到的界面

def zz(request):
    return render(request,'home/move_home.html')