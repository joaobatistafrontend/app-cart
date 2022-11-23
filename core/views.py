from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Home(TemplateView):
    template_name = 'home.html'


class SingUPView(TemplateView):
    def get(self,request):
        form = UserCreationForm()
        return render(request,'registration/singup.html',{'form':form})
    
    def post(self,request):
        fomr = UserCreationForm(request.POST)
        if fomr.is_valid():
            user = fomr.save()
            # user.user_permissions.add(20)
            return redirect('login')
        else:
            fomr = UserCreationForm()
