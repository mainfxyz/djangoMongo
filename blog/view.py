from django.shortcuts import render
import sys
from django.http import JsonResponse,HttpResponse
sys.path.append("..")
from db.models import ShopDB,User
"""
    视图函数"""
def index(request):
    result = ShopDB.objects.all()
    context={}
    context['shops']=result
    context['username']=request.session.get('username',"登录")
    return render(request,'com.html',context)

def shop(request):
    id=request.GET.get("id")
    result = ShopDB.objects.get(id=id)
    context = {}
    context['shop'] = result
    context['username'] = request.session.get('username', "登录")
    return render(request, 'shop.html', context)

def register(request):
    context={}
    context['username'] = request.session.get('username', "登录")
    return render(request,'register.html')

def admin(request):
    result = ShopDB.objects.all()
    context={}
    context['shops'] = result
    return render(request,'admin.html',context)

def adminUser(request):
    context={}
    context['users']=User.objects.all()
    return render(request,'adminUser.html',context)

"""
    异步函数"""
def say(request):
    say=request.GET.get('say')
    username = request.session.get('username')
    if username==None:
        return HttpResponse('没有登录')
    id = request.GET.get('id')
    if username==None:
        return HttpResponse('评论失败')
    try:
        s = ShopDB.objects.get(id=id)
    except:
        return HttpResponse('没有该商品')
    s.comment.append([{'user':username},{'com':say}])
    try:
        s.save()
    except:
        return HttpResponse('保存失败')
    return HttpResponse('OK')





'''
    用户模块'''
def login(request):
    username=request.GET.get('username')
    try:
        u = User.objects.get(username=username)
    except:
        return HttpResponse("没有该用户")
    if u.password == request.GET.get('password'):
        request.session['username'] = u.username
        return HttpResponse("OK")
    else:
        return HttpResponse("密码错误")


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("OK")


def reg(request):
    username=request.GET.get('username')
    password=request.GET.get('password')
    if len(username)<6:
        return HttpResponse("用户名太短")
    if len(password)<6:
        return HttpResponse("密码太短")
    u=User(username,password)
    try:
        u.save()
    except:
        return HttpResponse('注册失败')
    return HttpResponse('OK')


"""
    管理员模块"""
def saveS(request):
    id=request.GET.get('_id')
    name=request.GET.get('name')
    price = request.GET.get('price')
    shop=request.GET.get('shop')
    s=ShopDB.objects.get(id=id)
    s.name=name
    s.price=float(price)
    s.shop=shop
    s.save()
    return HttpResponse("OK")

def delS(request):
    id=request.GET.get('_id')
    s=ShopDB.objects.get(id=id)
    s.delete()
    return HttpResponse("OK")

def saveU(request):
    id=request.GET.get('_id')
    username=request.GET.get('username')
    password = request.GET.get('password')
    s=User.objects.get(id=id)
    s.username=username
    s.password=password
    s.save()
    return HttpResponse("OK")

def delU(request):
    id=request.GET.get('_id')
    s=User.objects.get(id=id)
    s.delete()
    return HttpResponse("OK")