from django.contrib import admin
from .models import Categoria, Transacao

admin.site.site_header = 'Administrador' # muda cabecalho
admin.site.index_title = 'Tabelas' # titulo em cima das tabelas
admin.site.site_header = 'Python' # titulo da pagina

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Transacao)