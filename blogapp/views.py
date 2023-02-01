from django.shortcuts import render, redirect
from.models import blog,profile,feedback
from blogapp.form import blog_form,feedback_form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def show(request):
  data = blog.objects.all()
  return render(request,'fakeblog.html',{"data": data})

@login_required(login_url='login')
def add1(request):
  if request.method == 'GET':
    form = blog_form()
    return render(request,'add.html', {"form":form})
  else:
    form = blog_form(request.POST,request.FILES)
    if form.is_valid():
      form.save()
      return redirect('show')
    else:
      return redirect('/')

@login_required(login_url='login')
def MoreInfo(request,id):
  data = blog.objects.get(id = id)
  return render(request,'MoreInfo.html',{"data":data})

@login_required(login_url='login')
def delete(request,id):
    a= blog.objects.get(id = id)
    a.delete()
    return redirect('show')

@login_required(login_url='login')
def update(request,id):
    a= blog.objects.get(id=id)
    if request.method == 'GET':
        form = blog_form(instance=a)
        return render(request,'update.html',{'form':form})

    else:
        form = blog_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect("show")
    
    return render(request,'update.html',{'data':a})

def register(request):
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    comfirm_password = request.POST['comfirm_password']

    if password==comfirm_password:
      if User.objects.filter(username=username).exists():
        messages.info(request,"user already exits")

      elif User.objects.filter(email=email).exists():
        messages.info(request,"email already exits")
      else:
        data = User.objects.create_user(username=username,email=email,password=password)
        data.save()
        return redirect('show')
    else:
      messages.info(request,"your password did not match")
      return redirect('register')
  return render(request,'register.html')

        
def login(request):
  if request.method == "POST":
    username = request.POST['Username']
    password = request.POST['Password']

    user = auth.authenticate(username=username, password=password)
    if user is not None:
      auth.login(request,user)
      return redirect('show')
    else:
      messages.info(request,"wrong password")
      return redirect("login")
  return render(request,"log.html")
  
@login_required(login_url='login')
def logout(request):
  auth.logout(request)
  return redirect("login")

@login_required(login_url='login')
def search(request):
  search = request.POST['search']
  print(search)
  data = blog.objects.filter(title__contains=search)
  print(data)
  return render(request,'fakeblog.html',{'data':data})

def delete(request,id):
  data = blog.objects.get(id=id)
  data.delete()
  return redirect('show')
  
@login_required(login_url='login')
def edit(request,id):
  data = blog.objects.get(id=id)
  if request.method == "GET":
    form = blog_form(instance=data)
    return render(request, 'edit.html', {'form': form})

  else:
    form = blog_form(request.POST,request.FILES,instance=data)
    if form.is_valid():
      form.save()
      return redirect("show")
    return render(request, 'edit.html',{'data':data})

@login_required(login_url='login')
def profile_a(request):
  a = profile.objects.filter(user__exact=request.user).values("first_name")

  print(a)
  if a:
    d = request.user
    p = profile.objects.filter(user__exact =d)
    print(p)
    return render(request,'profile.html',{'p':p})
  else:
    if request.method == "POST":
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     user =request.user
     email = request.POST['email']
     profile_pic = request.FILES['img']
     about_me = request.POST['about_me']
     data = profile(first_name=first_name,last_name=last_name,user=user,email=email,profile_pic=profile_pic,about_me=about_me).save()
     
     return redirect('profile')
    return render(request,'profile.html')

@login_required(login_url='login')
def feedback1(request):
  if request.method == 'GET':
    form = feedback_form()
    return render(request,'feedback.html', {"form":form})
  else:
    form = feedback_form(request.POST)
    if form.is_valid():
      form.save()
      
      return redirect('feedback')
       


  


      


         

   




 

    

    




