from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdm(admin.ModelAdmin):
    list_display = ['nome','dados','valor']