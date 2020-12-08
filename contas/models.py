from django.db import models

# Create your models here.

#cada classe individual é uma tabela
#sempre que ocorrer alteracoes:
#python manage.py makemigrations = transforma isso em um sql(Banco de Dados)
#python manage.py migrate = transfere para o DB da aplicacao
#depois deve registrar cada model no admin.py

class Categoria(models.Model):
 #models fields = campo de models
 nome = models.CharField(max_length=100)
 data = models.DateTimeField(auto_now_add=True)#pega a data da criacao desse model
 def __str__(self):
  return self.nome
 
class Transacao(models.Model):
 #data = models.DateTimeField(auto_now_add=True)#sem nada nos parametros funciona tambem
 data = models.DateTimeField()
 descricao = models.CharField(max_length=200)
 valor = models.DecimalField(max_digits=7,decimal_places=2)
 categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
 observacoes = models.TextField(null = True, blank=True) #declara item nao obrigatorio
 class Meta:
  verbose_name_plural = 'Transacoes'
 def __str__(self):
  return self.descricao #como vai aparecer o objeto da classe Transacao na tela do admin 
  #no caso so vai mostrar a descricao do objeto
