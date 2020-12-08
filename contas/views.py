from django.shortcuts import render,redirect
from .models import Transacao
from .forms import TransacaoForm

# Create your views here.

#from django.http import HttpResponse
#import datetime

def home(request): #parametro request obrigatorio
 #now = datetime.datetime.now() #pega a hora do sistema
 #html = "<html><body>It is now %s.</body></html>" % now
 #return HttpResponse(html)
 
 data = {}
 data['transcoes'] = ['t1','t2','t3']
 #data['now'] = datetime.datetime.now()
 return render(request, 'contas/home.html',data)
 #retorna a request, template e a variavel
 #renderiza/envia a variavel no template

def listagem(request):
 data = {}
 data['transacoes'] = Transacao.objects.all() #seleciona do banco tudo de Transacao
 return render(request, 'contas/listagem.html',data)
 
def nova_transacao(request):
 data = {}
 formnovo = TransacaoForm(request.POST or None)# objeto, verifica se ja ha dados salvos
 if formnovo.is_valid():#verifica se é valido
  formnovo.save()
  return redirect('listagem_url')
 #preenche a pagina form se já haver dados 
 data['form'] = formnovo
 return render(request, 'contas/form.html',data)
 
def update(request, pk):
 data = {}
 transacao = Transacao.objects.get(pk = pk)#pk = primary key
 formnovo = TransacaoForm(request.POST or None, instance=transacao)
 
 if formnovo.is_valid():#verifica se é valido
  formnovo.save()
  return redirect('listagem_url')
  
 data['form'] = formnovo
 data['transacao'] = transacao
 return render(request, 'contas/form.html',data)
 
def delete(request, pk):
 transacao = Transacao.objects.get(pk = pk)
 transacao.delete()
 return redirect('listagem_url')
 
