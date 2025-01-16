from django import forms
from .models import Tecnico, Veiculo, Cliente, Servico

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nome', 'matricula']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca', 'modelo', 'cor']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cor': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'veiculo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
        }

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['peca', 'cliente', 'defeito', 'descricao_problema', 'tecnico', 'descricao_solucao']
        widgets = {
            'peca': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'defeito': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao_problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'tecnico': forms.Select(attrs={'class': 'form-control'}),
            'descricao_solucao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
