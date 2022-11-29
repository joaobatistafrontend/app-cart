from django.urls import path,include
from .views import Home,SingUPView,error404,error500,DadosJson,ProdutoViewSet
from .crud import CriarProduto,ListaProduto,EditarProduto,DeletarProduto
from django.conf.urls import handler404,handler500
from rest_framework import routers, serializers, viewsets



router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('api/', include(router.urls)),
    path('singup/',SingUPView.as_view(),name='singup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('creat/',CriarProduto.as_view(),name='creat'),
    path('list/',ListaProduto.as_view(),name='list'),
    path('update/<int:pk>',EditarProduto.as_view(),name='update'),
    path('delete/<int:pk>',DeletarProduto.as_view(),name='deleta'),
    path('dados/',DadosJson.as_view(),name='dados')
]
handler404 = 'core.views.error404'