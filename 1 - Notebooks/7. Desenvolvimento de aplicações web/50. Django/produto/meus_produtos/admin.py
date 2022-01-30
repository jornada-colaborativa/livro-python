from django.contrib import admin
from meus_produtos.models import Produto

class ProdutoModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produto, ProdutoModelAdmin)
