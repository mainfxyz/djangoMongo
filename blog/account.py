from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

#原始的方法，函数编程，一步一步自己写
def logIN(request):
    if request.user.is_authenticated:
        return HttpResponse("已经登录了")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")

def logOUT(request):
    logout(request)

def reg(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    u=User(username=username,password=password)
    u.save()
    return HttpResponse("注册成功")

def forgotPasswd(request):
    email = request.POST.get('email')
    from django.core.mail import send_mail
    import random
    code=random.randint(1000,9999)
    send_mail(
        'Subject here',
        "code is "+str(code),
        '15610575692@163.com',
        [email],
        fail_silently=False,
    )

def changePaawd(request):
    username = request.user
    password = request.POST.get('password')
    User.objects.fiter(username=username).update(password=password)
    return HttpResponse("修改成功")


def logHTML(request):
    return render(request, "login.html")