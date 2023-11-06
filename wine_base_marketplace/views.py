from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
 
# Create your views here.
def signup(request):
    if request.method == 'GET':
        print("Enviando formulario")
    else:
        from wine_base_marketplace.models import User
        print(request.POST)
        if User.objects.filter(username=request.POST['username'],password=request.POST['password']):
            return redirect('home')
        else:
            print("LO SIENTO NO ESTAS REGISTRADO AUN")    
      
    
    return render(request,"login.html",{
        
    })

def home(request):
    return render(request,'home.html')