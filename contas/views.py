from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# View que cuida do registro de novos usúarios no sistema 
class RegistroView(View):

    def get(self, request):
        user_form = UserCreationForm()
        return render(
            request,
            'registro.html',
            {'user_form': user_form}
        )
    
    def post(self, request):
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')


        return render(
            request,
            'registro.html',
            {'user_form': user_form}
        )


# View que cuida do login de usúarios já cadastrados
class LoginView(View):

    def get(self, request):
        login_form = AuthenticationForm()
        return render(
            request,
            'login.html',
            {'login_form': login_form}
        )
    

    def post(self, request):
        usuario = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            login_form = AuthenticationForm(data=request.POST)
            login_form.add_error(None, '') 

        
        return render(
            request,
            'login.html',
            {'login_form': login_form}
        )
    
# View usada para possibilidar a saida da conta logada
class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')
