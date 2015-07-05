from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cadastro.views.index'),

    url(r'^listargrupo/', 'cadastro.views.listargrupo'),
    url(r'^inserirgrupo/', 'cadastro.views.inserirgrupo'),
	url(r'^deletargrupo/(?P<id_grupo>\d+)/$', 'cadastro.views.deletargrupo'),
	url(r'^editargrupo/(?P<id_grupo>\d+)/$', 'cadastro.views.editargrupo'),


	url(r'^listarmateria/', 'cadastro.views.listarmateria'),
    url(r'^inserirmateria/', 'cadastro.views.inserirmateria'),
	url(r'^deletarmateria/(?P<id_materia>\d+)/$', 'cadastro.views.deletarmateria'),
	url(r'^editarmateria/(?P<id_materia>\d+)/$', 'cadastro.views.editarmateria'),

    url(r'^listarpessoa/', 'cadastro.views.listarpessoa'),
    url(r'^inserirpessoa/', 'cadastro.views.inserirpessoa'),
    url(r'^deletarpessoa/(?P<id_pessoa>\d+)/$', 'cadastro.views.deletarpessoa'),
    url(r'^editarpessoa/(?P<id_pessoa>\d+)/$', 'cadastro.views.editarpessoa'),
    url(r'^consulta/', 'cadastro.views.consulta'),

    url(r'^conteudo/(?P<id_grupo>\d+)/$', 'cadastro.views.conteudo'),
 
)