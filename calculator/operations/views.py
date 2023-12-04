from django.shortcuts import render
from django.views.generic import View
from operations.forms import Register,Book,MobileForm



class BookView(View):
    def get(self,request):
        form=Book()
        
        return render(request,"book.html",{"form":form})
    
     
    def post(self,request):
        print(request.POST)
        
        book = Book.objects.all
        return render(request,"book.html",{"book":book})


class HelloView(View):
    def get(self,request):
       return render(request,"hello.html")

class AddView(View):
    def get(self,request):
        return render(request,"add.html")
    
    def post(self,request):
        print(request.POST)
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        if n1<n2:
            res= n1 + n2
            print(res)
        else:
            res= n1 - n2
            print(res)    
        return render(request,"add.html",{"res":res})
    
class GreetView(View):
    def get(self,request):
        return render(request,"greet.html")
    
    def post(self,request):
         print(request.POST)
         name=request.POST.get('name')
         age=request.POST.get('age')
         greet="hello" + name + "you are "+ age+ "now"
         print(greet)
         return render(request,"greet.html",{"greet":greet})

class SigninView(View):
    def get(self,request):
        form=Register()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request):
        form=Register(request.POST)
        if form.is_valid():
            # name=form.cleaned_data.get('name')
            # pwd1=form.cleaned_data.get('password1')
            # pwd2=form.cleaned_data.get('password2')
            # if pwd1 == pwd2: 

              print(form.cleaned_data)
              print(form.request.POST)
            # else:
            #     print("passwords doesnt match")

        else:
            print("gud bye")

        return render(request,"signin.html",{"form":form})

    
class MobileView(View):

    def get(self,request):
        form = MobileForm()
        return render(request,"mob.html",{"form":form})


    