from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView,View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produto
from .crud import ListaProduto
import json
from rest_framework import viewsets
from .serializers import ProdutoSerializer



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
            if user.is_authenticated:
                user.user_permissions.add(20)
                return redirect('home')
            # user.user_permissions.add(20)
            return redirect('login')
        else:
            fomr = UserCreationForm()
 
class DadosJson(View):
    def get(self,request):  
        dados = list(ListaProduto.objects.values())
        formatados_dados = json.dump(dados, ensure_ascii = False)
        return HttpResponse(formatados_dados, content_type = 'aplication/json')

    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
        


def error404(request,exception):
    return render(request,'404.html')


def error500(request,exception):
    return render(request,'500.html')