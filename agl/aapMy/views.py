from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    product = Urun.objects.all().order_by("?")[:3]
    anaurun = SatilikUrun.objects.all().order_by("?")[:2]
    context = {
        'product':product,
        'anaurun':anaurun
    }
    
    if request.method== "POST":
         username = request.POST["username"]
         password = request.POST["password"]
         print(username)
         user = authenticate(username=username,password=password)
         
         if user is not None:
             login(request,user)
             return redirect('index')
         else:
             hata= "Kullanıcı Adı veya Şifre Yanlış"
             context.update({'hata':hata})
             
    return render(request,'index.html',context)


def referans(request):
    isortak = Referans.objects.all()
    context = {
        'isortak':isortak
    }
    return render(request,'referans.html',context)

def urunSayfasi(request):
    product = SatilikUrun.objects.all()
    
    context = {
        'product':product
    }
    return render(request,'urunler.html',context)

def detay(request,id):
    card = SatilikUrun.objects.get(id=id)
    comments = Comment.objects.filter(card=card)
    if request.method =="POST":
        yorum = request.POST["yorum"]
        comment = Comment(user=request.user,text=yorum,card=card)
        comment.save()
        return redirect("/detay/" + id + "/")
       
    context = {
        'card':card,
        'comments':comments
    }
    
    return render(request,'detay.html',context)

def register(request):
    context= {}
    if request.method =="POST":
         name = request.POST["name"]
         surname= request.POST["surname"]
         email = request.POST["email"]
         username = request.POST["username"]
         password1 = request.POST["password1"]
         password2 = request.POST["password2"]
         if password1 == password2: 
             if not User.objects.filter(username=username).exists():
                 if not User.objects.filter(email=email).exists():
                     user = User.objects.create_user(first_name=name,last_name=surname,email=email,username=username,password=password1)
                     user.save()
                     return redirect('index')
                 else:
                     hata= "Bu Email Daha Önce Kullanılmış"
                     context.update({'hata':hata})
             else:
                hata= "Kullanıcı adı Daha Önce Kullanılmış"
                context.update({'hata':hata})
         else:
              hata= "Şifreler aynı Değil"
              context.update({'hata':hata})
         
         
    
    return render(request,'users/register.html',context)

def logoutt(request):
    logout(request)
    return redirect('index')
