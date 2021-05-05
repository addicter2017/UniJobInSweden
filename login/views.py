from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.

from login.models import User
from login.myforms import UserForm


def login(request):
     #t = Chalmers.objects.all()
    # print(t)
    # for obj in t:
    #     print(obj.title)
    if request.session.get('is_login',None):
        return render(request,'login.html')
    # if request.method == 'GET':
    #     return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        print(username,password)
        if username and password:
            username = username.strip()
            try:
                user = User.objects.get(name=username)
            except:
                return render(request,'login.html')
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return HttpResponseRedirect('http://127.0.0.1:8000/front_page/info/?#')
            else:
                message = 'wrong password!'
        else:
            message = "User doesn't exist"

    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单数据

            username = uf.cleaned_data['username'] # cleaned_data 是字典,里面存放提交完成的信息
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # add to database

            registAdd = User.objects.create(name = username,password = password,email = email)
            # print registAdd
            if registAdd == False:
                return render(request, 'share1.html', {'registAdd': registAdd, 'username': username})

            else:
                # return HttpResponse('ok')
                return render(request, 'share1.html', {'registAdd': registAdd})
                # return render_to_response('share.html',{'registAdd':registAdd},context_instance = RequestContext(request))
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        uf = UserForm()
    # return render_to_response('regist.html',{'uf':uf},context_instance = RequestContext(request))

    return render(request,'register.html')

def logout(request):
    if not request.session.get('is_login',None):
        return HttpResponseRedirect("http://127.0.0.1:8000/front_page/index")
    request.session.flush()
    return HttpResponseRedirect("http://127.0.0.1:8000/front_page/index")

