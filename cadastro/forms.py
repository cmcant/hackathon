# -*- coding:utf-8 -*-
from django import forms
from django.forms import CharField, Form, PasswordInput
from django.contrib.auth.models import User,Group
from cadastro.models import *


class GrupoForm(forms.ModelForm):
    class Meta:
    	model = Group
    	exclude = ['permissions']

class MateriaForm(forms.ModelForm):
    class Meta:
    	model = Materia
    	
class PessoaForm(forms.ModelForm):
    class Meta:
    	model = Pessoa
