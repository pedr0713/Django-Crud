from django.forms import ModelForm
from .models import Transacao

#vai ler os campos de acordo com o Transacao
class TransacaoForm(ModelForm):
 class Meta:
  model = Transacao #chama o Transacao
  fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']


