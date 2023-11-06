from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
 
# Create your views here.
def login(request):
    if request.method == 'GET':
        print("Enviando formulario")
    else:
        from wine_base_marketplace.models import User
        print(request.POST)
        if User.objects.filter(username=request.POST['username'],password=request.POST['password']):
            return redirect('home')
        else:
            return render(request,'errors/error_login.html')
      
    
    return render(request,"login.html")

def signup(request):
    if request.method == 'GET':
        print("Enviando Formulario")
    else:
        if request.POST['password1'] != request.POST['password2']:
             messages.add_message(request,messages.WARNING,"Las contraseñas son diferentes no es posible guardarlas.")
             messages_copy = messages.get_messages(request)

             return render(request,'signup.html',{'messages_copy': messages_copy})
        else:
            from wine_base_marketplace.models import User
            if User.objects.filter(username=request.POST['username']):
                messages.add_message(request,messages.WARNING,"Este usuario ya se encuentra registrado digita uno diferente.")
                messages_copy = messages.get_messages(request)

                return render(request,'signup.html',{'messages_copy': messages_copy})
            else:
                x = User()
                x.name = request.POST['name']
                x.last_name = request.POST['last_name']
                x.age = request.POST['age']
                x.username = request.POST['username']
                x.password = request.POST['password1']
                x.save()

                messages.add_message(request,messages.INFO,'Te has regisrado de manera exitosa ahora puedes ingresar.',extra_tags='class="alert-warning"')

                messages_copy = messages.get_messages(request)
                for message in messages_copy:
                    print(message.level, message.message)

                return render(request,'signup.html',{'messages_copy': messages_copy})  


    return render(request,'signup.html')
               

def home(request):
    return render(request,'home.html')