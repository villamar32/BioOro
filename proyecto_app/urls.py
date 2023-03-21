from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
   
   # Inicio
   # path('', views.index, name='index'),

   # Enlaces pagina
    
    
    path('',views.inicio, name="inicio"),
    
    path('administrar/', views.index, name='index'),
    path("administracion/",views.administracion, name="administracion"),

    #path("especie/<int:id_fauna>",views.especie, name="especie"),

    

    #path("fauna",views.fauna, name="fauna"),
    #path("fauna/<int:id_bioma>/",views.fauna.as_view(), name="fauna"),
    
    path("areasnat/",views.areasnat, name="areasnat"),

    path("infoweb/",views.infoweb, name="infoweb"),
    
    path("sugerencias/",views.sugerencias, name="sugerencias"),

    path("galeria", views.galeria_general, name="galeriageneral"),

    #nuevo
    path("El_Oro", views.El_Oro, name="El_Oro"),
    path("Protegidas", views.Protegidas, name="Protegidas"),
    path("Sistemas", views.Sistemas, name="Sistemas"),
    
    path("galeriabioma/", views.galeriabioma, name="galeriabioma"),
    
    path("contacto/",views.contacto, name="contacto"),


    path("busquedaavanzada/",views.busquedaavanzada, name="busquedaavanzada"),
  


#-------------------------------------------------------
    path("galeriabiomaFlora/", views.galeriabiomaFlora, name="galeriabiomaFlora"),

    path("flora/<int:id_bioma>/",views.flora, name="flora"),

    path("fauna/<int:id_bioma>/",views.fauna, name="fauna"),

#-------------------------------------------------------
    
#-------------------------------------------------------

    path("LateralD/<int:id_bioma>/<int:tipo>",views.LateralD, name="LateralD"),
    
    #path("IntroAnfibios/",views.IntroAnfibios, name="IntroAnfibios"),
    path("IntroAves/",views.IntroAves, name="IntroAves"),


    # Anfibios
    path("base/", views.base, name="base"),
    path("busqueda_anfibios/", views.busqueda_anfibio, name="busqueda_anfibios"),
    path("intro_anfibios/", views.intro_anfibio, name="intro_anfibios"),
    path("galeria_anfibios/", views.galeria_anfibio, name="galeria_anfibios"),
    path("noticias_anfibios/", views.noticias_anfibio, name="noticias_anfibios"),
    path("lista_especies_anfibios/", views.lista_especies_anfibios, name="lista_especies_anfibios"),
    path("ficha_tecnica_anfibios/<int:id_especie>/", views.ficha_tenica_anfibio, name="ficha_tecnica_anfibios"),
    path("como_citar_anfibios/", views.como_citar_anfibio, name="como_citar_anfibios"),
    path("uso_datos_anfibios/", views.uso_datos_anfibio, name="uso_datos_anfibios"),
    path("agradecimientos_anfibios/", views.agradecimientos_anfibio, name="agradecimientos_anfibios"),
    path("quienes_somos_anfibios/", views.quienes_somos_anfibio, name="quienes_somos_anfibios"),
    #Reptiles
    path("basereptil/", views.basereptil, name="basereptil"),
    path("busqueda_reptil/", views.busqueda_reptil, name="busqueda_reptil"),
    path("intro_reptil/", views.intro_reptil, name="intro_reptil"),
    path("galeria_reptil/", views.galeria_reptil, name="galeria_reptil"),
    path("noticias_reptil/", views.noticias_reptil, name="noticias_reptil"),
    path("lista_especies_reptil/", views.lista_especies_reptil, name="lista_especies_reptil"),
    path("ficha_tecnica_reptil/<int:id_especie>/", views.ficha_tecnica_reptil, name="ficha_tecnica_reptil"),
    path("como_citar_reptil/", views.como_citar_reptil, name="como_citar_reptil"),
    path("uso_datos_reptil/", views.uso_datos_reptil, name="uso_datos_reptil"),
    path("agradecimientos_reptil/", views.agradecimientos_reptil, name="agradecimientos_reptil"),
    path("quienes_somos_reptil/", views.quienes_somos_reptil, name="quienes_somos_reptil"),
    #Aves
    path("baseave/", views.baseave, name="baseave"),
    path("busqueda_ave/", views.busqueda_ave, name="busqueda_ave"),
    path("intro_ave/", views.intro_ave, name="intro_ave"),
    path("galeria_ave/", views.galeria_ave, name="galeria_ave"),
    path("noticias_ave/", views.noticias_ave, name="noticias_ave"),
    path("lista_especies_ave/", views.lista_especies_ave, name="lista_especies_ave"),
    path("ficha_tecnica_ave/<int:id_especie>/", views.ficha_tecnica_ave, name="ficha_tecnica_ave"),
    path("como_citar_ave/", views.como_citar_ave, name="como_citar_ave"),
    path("uso_datos_ave/", views.uso_datos_ave, name="uso_datos_ave"),
    path("agradecimientos_ave/", views.agradecimientos_ave, name="agradecimientos_ave"),
    path("quienes_somos_ave/", views.quienes_somos_ave, name="quienes_somos_ave"),
    #Peces
    path("basepeces/", views.basepeces, name="basepeces"),
    path("busqueda_peces/", views.busqueda_peces, name="busqueda_peces"),
    path("intro_peces/", views.intro_peces, name="intro_peces"),
    path("galeria_peces/", views.galeria_peces, name="galeria_peces"),
    path("noticias_peces/", views.noticias_peces, name="noticias_peces"),
    path("lista_especies_peces/", views.lista_especies_peces, name="lista_especies_peces"),
    path("ficha_tecnica_peces/<int:id_especie>/", views.ficha_tecnica_peces, name="ficha_tecnica_peces"),
    path("como_citar_peces/", views.como_citar_peces, name="como_citar_peces"),
    path("uso_datos_peces/", views.uso_datos_peces, name="uso_datos_peces"),
    path("agradecimientos_peces/", views.agradecimientos_peces, name="agradecimientos_peces"),
    path("quienes_somos_peces/", views.quienes_somos_peces, name="quienes_somos_peces"),
    #Mamiferos
    path("basemamifero/", views.basemamifero, name="basemamifero"),
    path("busqueda_mamifero/", views.busqueda_mamifero, name="busqueda_mamifero"),
    path("intro_mamifero/", views.intro_mamifero, name="intro_mamifero"),
   
    path("galeria_mamifero/", views.galeria_mamifero, name="galeria_mamifero"),
    path("noticias_mamifero/", views.noticias_mamifero, name="noticias_mamifero"),
    path("lista_especies_mamifero/", views.lista_especies_mamifero, name="lista_especies_mamifero"),
    path("ficha_tecnica_mamifero/<int:id_especie>/", views.ficha_tecnica_mamifero, name="ficha_tecnica_mamifero"),
    path("como_citar_mamifero/", views.como_citar_mamifero, name="como_citar_mamifero"),
    path("uso_datos_mamifero/", views.uso_datos_mamifero, name="uso_datos_mamifero"),
    path("agradecimientos_mamifero/", views.agradecimientos_mamifero, name="agradecimientos_mamifero"),
    path("quienes_somos_mamifero/", views.quienes_somos_mamifero, name="quienes_somos_mamifero"),
    #Orquideas
    path("baseorquidea/", views.baseorquidea, name="baseorquidea"),
    path("busqueda_orquidea/", views.busqueda_orquidea, name="busqueda_orquidea"),
    path("intro_orquidea/", views.intro_orquidea, name="intro_orquidea"),
    path("galeria_orquidea/", views.galeria_orquidea, name="galeria_orquidea"),
    path("noticias_orquidea/", views.noticias_orquidea, name="noticias_orquidea"),
    path("lista_especies_orquidea/", views.lista_especies_orquidea, name="lista_especies_orquidea"),
    path("ficha_tecnica_orquidea/<int:id_flora>/", views.ficha_tecnica_orquidea, name="ficha_tecnica_orquidea"),
    path("como_citar_orquidea/", views.como_citar_orquidea, name="como_citar_orquidea"),
    path("uso_datos_orquidea/", views.uso_datos_orquidea, name="uso_datos_orquidea"),
    path("agradecimientos_orquidea/", views.agradecimientos_orquidea, name="agradecimientos_orquidea"),
    path("quienes_somos_orquidea/", views.quienes_somos_orquidea, name="quienes_somos_orquidea"),
    #Bromelias
    path("basebromelia/", views.basebromelia, name="basebromelia"),
    path("busqueda_bromelia/", views.busqueda_bromelia, name="busqueda_bromelia"),
    path("intro_bromelia/", views.intro_bromelia, name="intro_bromelia"),
    path("galeria_bromelia/", views.galeria_bromelia, name="galeria_bromelia"),
    path("noticias_bromelia/", views.noticias_bromelia, name="noticias_bromelia"),
    path("lista_especies_bromelia/", views.lista_especies_bromelia, name="lista_especies_bromelia"),
    path("ficha_tecnica_bromelia/<int:id_flora>/", views.ficha_tecnica_bromelia, name="ficha_tecnica_bromelia"),
    path("como_citar_bromelia/", views.como_citar_bromelia, name="como_citar_bromelia"),
    path("uso_datos_bromelia/", views.uso_datos_bromelia, name="uso_datos_bromelia"),
    path("agradecimientos_bromelia/", views.agradecimientos_bromelia, name="agradecimientos_bromelia"),
    path("quienes_somos_bromelia/", views.quienes_somos_bromelia, name="quienes_somos_bromelia"),

]



# Ejemplo para los enlaces pagina
"""
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('sample/', views.sample, name="sample"),
]


"""
