from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login ,logout
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm,LoginForm,Signup,CommentForm,PostForm,autherform, autherforms
from django.views.generic.edit import CreateView
from .models import Contact,Post,comment,auther
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.contrib.auth.models import User
def index(request):
    post=Post.objects.all()
    return render(request,'home.html', {'post':post})
def about(request):
    return render(request,'about.html', {})
@login_required(login_url='/login/')    
def gallery(request):
    fm=autherform(instance=request.user)
    fn= autherforms(instance=request.user.auther)
    return render(request,'gallery.html', {'form':fm,'forms':fn})  
    #Contact us form      
def contact(request):
    form=ContactForm()
    return render(request,'contact.html', {'form':form})  
class contact(CreateView):
    model =Contact
    template_name = "contact.html"
    fields=['name','email','subject','message']
    success_url='/'

def singlepost(request, id):
    post=Post.objects.get(id=id)
    comments=comment.objects.filter(Posts=post).order_by('-id')[:5]
    if request.method=='POST':
        com=CommentForm(request.POST)
        if com.is_valid():
            comme=request.POST.get('comment')
            
            c=comment.objects.create(comment=comme,Posts=post,user=request.user)
            c.save()
            return redirect(post.get_absolute_url())
    else:
        com=CommentForm()    
    context={
        'post':post,
        'comments':comments,
        'com':com
        
    }
    return render(request,'single-post.html',context)      
class Mylogin(LoginView):
    template_name='login.html'
    authentication_form=LoginForm
class singup(CreateView):
  template_name = 'signup.html'
  success_url = '/login/'
  form_class =Signup
  success_message = "Your profile was created successfully"    

def Mylogout(request):


    logout(request)

    return HttpResponseRedirect('/')    



@login_required(login_url='/login/') 
def PostCreateView(request):
    if request.user.is_authenticated:

        posts=Post.objects.filter(auther=request.user.auther)
        

        return render(request,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')    
    
@login_required(login_url='/login/') 
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(auther=request.user.auther)
        print(posts)


        return render(request,'dashboard.html',{'posts':posts})
    else:
        return HttpResponseRedirect('/login/')
@login_required(login_url='/login/') 
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=request.POST.get('title')
                desc=request.POST.get('desc')
                fm=Post.objects.create(title=title ,desc=desc,auther=request.user.auther)                
                fm.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            form =PostForm()
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
@login_required(login_url='/login/') 
def updatepost (request,id):

    if request.user.is_authenticated:
        if request.method =='POST':
            pi=Post.objects.get(pk=id)

            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
        return render(request,'updatepost.html',{'form':form})



    else:
        return HttpResponseRedirect('/login/')
@login_required(login_url='/login/') 
def deletepost (request,id):
    if request.user.is_authenticated:
        if request.method =='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')


    else:
        return HttpResponseRedirect('/login/')
@login_required(login_url='/login/') 
def updateprofile(request):
    if request.method=='POST':
        fm= autherform(request.POST, request.FILES,instance=request.user.auther)
        fn=autherforms(request.POST,instance=request.user)
      
        if fm.is_valid() and fn.is_valid():
            fm.save()
            fn.save()
            return HttpResponseRedirect('/gellery/')

            
    else:

        fm= autherform(instance=request.user.auther)
        fn=autherforms(instance=request.user)

    return render(request, 'updateprofile.html', {'form':fm,'for':fn})
def authername(request):

    if request.user.profession ==None:
        if request.method=='POST':

           
            form= autherform(request.POST,request.FILES)
       
            if form.is_valid():
                about=request.POST.get('about')
                profession=request.POST.get('profession')
                image=request.POST.get('image')
                fm=auther.objects.create(user=request.user,about=about,profession=profession )
                fm.save()
                
        else:

            form= autherform()
   
        return render(request,'auther.html', {'form':form})
    else:
        return HttpResponseRedirect('/gellery/')

