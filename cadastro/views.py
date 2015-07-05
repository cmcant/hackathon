# -*- coding: utf 8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login
from django.template import Context, loader, RequestContext 
from django.db.models import Max, Sum, Min
from cadastro.models import *
from cadastro.forms import *
from django.contrib.auth.models import User,Group
from datetime import datetime
from reportlab.pdfgen import canvas
import shutil

def conteudo(request,id_grupo):
	gp = Group.objects.get(pk = id_grupo)
	ps = Pessoa.pessoa.all()
	mt = Materia.materia.all()
	return render(request,'conteudo.html',{
		'grupo':gp,
		'pessoa':ps,
		'materia':mt
		})

def consulta(request):
	gp = Group.objects.all().order_by('name')
	return render(request,'consulta.html',{
		'grupo': gp
		})


def index(request):
	return render(request,'index.html',{

		})

def listargrupo(request):
	gp = Group.objects.all()
	return render(request,'listargrupo.html',{
		'grupo' : gp
		})

def inserirgrupo(request):
	if request.method == 'POST':
		form = GrupoForm(request.POST)
		if form.is_valid():
			form.save()
			gp = Group.objects.all()
			return render(request,'listargrupo.html',{
            	'grupo':gp
            	})

	else:
		form = GrupoForm()
	return render(request, 'inserirgrupo.html', {
    	'form': form
    	})

def deletargrupo(request,id_grupo):
	gp = Group.objects.get(id = id_grupo).delete()
	gp = Group.objects.all()
	return render(request, 'listargrupo.html', {
    	'grupo': gp
    	})

def editargrupo(request,id_grupo):
	gp = Group.objects.get(id = id_grupo)
	if request.method == 'POST':
		form = GrupoForm(request.POST, instance=gp)
		if form.is_valid():
			form.save()
			gp = Group.objects.all()
			return render(request,'listargrupo.html',{
            	'grupo':gp
            	})

	else:
		form = GrupoForm(instance=gp)
	return render(request, 'editargrupo.html', {
    	'form': form
    	})

def listarmateria(request):
	mt = Materia.materia.all()
	return render(request,'listarmateria.html',{
		'materia' : mt
		})

def inserirmateria(request):
	if request.method == 'POST':
		form = MateriaForm(request.POST)
		if form.is_valid():
			form.save()
			mt = Materia.materia.all()
			return render(request,'listarmateria.html',{
            	'materia':mt
            	})

	else:
		form = MateriaForm()
	return render(request, 'inserirmateria.html', {
    	'form': form
    	})

def deletarmateria(request,id_materia):
	mt = Materia.materia.get(id = id_materia).delete()
	mt = Materia.materia.all()
	return render(request, 'listarmateria.html', {
    	'materia': mt
    	})

def editarmateria(request,id_materia):
	mt = Materia.materia.get(id = id_materia)
	if request.method == 'POST':
		form = MateriaForm(request.POST, instance=mt)
		if form.is_valid():
			form.save()
			mt = Materia.materia.all()
			return render(request,'listarmateria.html',{
            	'materia':mt
            	})

	else:
		form = MateriaForm(instance=mt)
	return render(request, 'editarmateria.html', {
    	'form': form
    	})

def listarpessoa(request):
	ps = Pessoa.pessoa.all()
	return render(request,'listarpessoa.html',{
		'pessoa' : ps
		})

def inserirpessoa(request):
	if request.method == 'POST':
		form = PessoaForm(request.POST)
		if form.is_valid():
			form.save()
			ps = Pessoa.pessoa.all()
			return render(request,'listarpessoa.html',{
            	'pessoa':ps
            	})

	else:
		form = PessoaForm()
	return render(request, 'inserirpessoa.html', {
    	'form': form
    	})

def deletarpessoa(request,id_pessoa):
	ps = Pessoa.pessoa.get(id = id_pessoa).delete()
	ps = Pessoa.pessoa.all()
	return render(request, 'listarpessoa.html', {
    	'pessoa': ps
    	})

def editarpessoa(request,id_pessoa):
	ps = Pessoa.pessoa.get(id = id_pessoa)
	if request.method == 'POST':
		form = PessoaForm(request.POST, instance=ps)
		if form.is_valid():
			form.save()
			ps = Pessoa.pessoa.all()
			return render(request,'listarpessoa.html',{
            	'pessoa':ps
            	})

	else:
		form = PessoaForm(instance=ps)
	return render(request, 'editarpessoa.html', {
    	'form': form
    	})
