# -*- coding: utf 8 -*-
from django.db import models
from django.contrib.auth.models import User,Group


class Materia(models.Model):
	class Meta: 
		verbose_name_plural = 'Materias' 
		verbose_name = 'Materia' 

	nome=models.CharField(max_length=100, verbose_name='Nome')
	tempo=models.TimeField(verbose_name='Tempo',null=True, blank=True)
	materia=models.Manager()

	def __unicode__(self):
		return self.nome	

class Pessoa(models.Model):
	class Meta: 
		verbose_name_plural = 'Pessoas' 
		verbose_name = 'Pessoa' 

	nome=models.CharField(max_length=100, verbose_name='Nome')
	foto=models.ImageField(upload_to='/fotos/',null=True,blank=True)
	grupo=models.ManyToManyField(Group, blank = True)
	materia=models.ManyToManyField(Materia, blank = True)
	pessoa=models.Manager()

	def __unicode__(self):
		return self.nome	

