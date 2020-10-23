from django import forms

class BuscaForm(forms.Form):
    busca = forms.CharField(label='Busca', max_length=100)