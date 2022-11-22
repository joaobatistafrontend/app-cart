from django.urls import path,include
from .views import Home,SingUPView
from .crud import CriarProduto,ListaProduto,EditarProduto,DeletarProduto



urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('cadastro',SingUPView.as_view(),name='cadastro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('creat',CriarProduto.as_view(),name='creat'),
    path('list',ListaProduto.as_view(),name='list'),
    path('update/<int:pk>',EditarProduto.as_view(),name='update'),
    path('delete/<int:pk>',DeletarProduto.as_view(),name='deleta'),

]
