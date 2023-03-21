from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError,EmailMultiAlternatives
from django.template import RequestContext
from django.template.context import Context
from django.views.generic import TemplateView
from django.db import models
from string import Template
import base64

#from django.template.loader import get_template

#from django.core.mail import EmailMultiAlternatives
#from configuracion.configuracion import settings


from django.views.generic import DetailView

from proyecto_app.models import BiomasEspecies, Especies, Familias, Flora, FloraBiomas, FloraImagen, Genero, GeneroFlora, ImagenesAbundancia, ImagenesBiomas, Locaciones, Ordenes, Subfamilias, EstadoConservacion
from proyecto_app.models import Biomas,Imagenes
from proyecto_app.contexto import obtener_id



# Create your views here.

def index(request):
    print("hola")
    return render(request, 'index.html')   

def administracion(request):
    return render(request, "administracion.html")
    
        
   

def inicio(request):
    return render(request, "inicio.html")

#fauna_solo = fauna.objects.all()


def flora(request):
    return render(request, "flora.html")
#-------------

#-------------
'''
def fauna(request, id_bioma):
    bioma_solo = bioma.objects.get(id=id_bioma)
    return render(request, "fauna.html", {'bioma_solo' : bioma_solo})
'''
def areasnat(request):
    return render(request, "areasnat.html")

def infoweb(request):
    return render(request, "infoweb.html")

def contacto(request):
  return render(request, "contacto.html")

#def agradecimientos(request):
 #   return render(request, "agradecimientos.html")

def familia(request):
    return render(request, "familia.html")

def subfamilia(request):
    return render(request, "subFamilia.html")

def galeria_general(request):
    anfibios = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i  left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.tipo='anfibio');")
    aves = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.tipo='ave');")
    mamiferos = Imagenes.objects.raw("SELECT    id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.tipo='mamifero');")
    
    peces = Imagenes.objects.raw("SELECT    id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i  left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.tipo='pez');")
    reptiles = Imagenes.objects.raw("SELECT   id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i  left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.tipo='reptil');")
  
    bromelias = FloraImagen.objects.raw("SELECT id_flora_imagen, fl.nom_flora, imf.imagenflora, g.nom_genero FROM flora_imagen as imf LEFT JOIN flora as fl ON (imf.id_flora = fl.id_flora) LEFT JOIN genero_flora as gf ON (fl.id_flora = gf.id_flora) LEFT JOIN genero as g ON (gf.id_genero = g.id_genero) WHERE fl.tipo_flora = 'Bromelia' ORDER BY fl.id_flora;")
    
    orquideas = FloraImagen.objects.raw("SELECT id_flora_imagen, fl.nom_flora, imf.imagenflora, g.nom_genero FROM flora_imagen as imf LEFT JOIN flora as fl ON (imf.id_flora = fl.id_flora) LEFT JOIN genero_flora as gf ON (fl.id_flora = gf.id_flora) LEFT JOIN genero as g ON (gf.id_genero = g.id_genero) WHERE fl.tipo_flora = 'orquídea' ORDER BY fl.id_flora;")
    
    macroinvertebrados = ImagenesAbundancia.objects.raw("SELECT id_imagen,ia.imagen_abundancia , a.tax_abundancia, f.nom_familia from imagenes_abundancia as ia LEFT JOIN abundancias as a on (ia.id_abundancia = a.id_abundancia ) LEFT JOIN familias as f on (f.id_familia = a.id_familia)")
    
    #bromelias = Imagenes.objects.raw("SELECT   id_flora_imagen, i.imagenflora, fl.nom_flora, fl.etimologia_flora, fl.diagnosis_flora,fl.distribucion_composicion_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_bioma as fb on (i.id_flora = i.id_flora ) where (fl.tipo_flora='Bromelia');")
    #orquideas = Imagenes.objects.raw("SELECT  id_flora_imagen, i.imagenflora, fl.nom_flora , fl.etimologia_flora,  fl.diagnosis_flora,fl.distribucion_composicion_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_biomas as fb on (fb.id_flora = i.id_flora ) where  (fl.tipo_flora='orquídea');")
    
    return render(request, "galeria_general.html", {  "anfibios":anfibios, "aves":aves, "mamiferos":mamiferos , "peces":peces , "reptiles":reptiles , "bromelias":bromelias , "orquideas":orquideas,"macroinvertebrados": macroinvertebrados})

#nuevo
def El_Oro(request):
    return render(request, "AreaNat_El_Oro.html")
def Protegidas(request):
    return render(request, "AreaNat_Protegidas.html")
def Sistemas(request):
    return render(request, "AreaNat_Sis_Biomas.html")

#biomas = bioma.objects.all()

class fauna_(TemplateView):
    template_name = 'fauna.html'

    def get_message(self):
        return u'Fauna'

    def get_context_data(self, **kwargs):
        context = super(fauna, self).get_context_data(**kwargs)
        context = dict()

    
         #context['id'] = id_bioma
        context['bioma_solo'] = Biomas.objects.get(id_bioma=kwargs['id_bioma'])
        
        return context
#def fauna(request, id_bioma):
  #bioma_solo = Biomas.objects.get(id_bioma=id_bioma)
 # print("             hola")
  #obtener_id(request)


  #return render(request, "fauna.html", {'bioma_solo' : bioma_solo})
 # if 'ce' in request.GET:
   # print("----")
    #obtener_id(request,1)        
  
  #return render(request, "fauna.html")


#def fauna(request):
#    return render(request, "fauna.html")


def areasnat(request):
    return render(request, "areasnat.html")

def infoweb(request):
    return render(request, "infoweb.html")


def familia(request):
    return render(request, "familia.html")

def subfamilia(request):
    return render(request, "subFamilia.html")

def contacto(request):
  return render(request, "contacto.html")


#def busquedaflora (request):
#    flora = Flora.objects.all()
#    return render(request, "busquedaavanzada.html", { "flora":flora })

#id_flora, nom_flora, tipo_flora, etimologia_flora, diagnosis_flora, comentarios_taxomicos_flora, distribucion_composicion_flora 

# ------------------- BUSQUEDA AVANZADA GENERAL --------------------------------------

# LLamando a html de pagina para busqueda avanzada.


def busquedaavanzada(request):

  # Data Fauna
  data_fauna = Especies.objects.raw("SELECT es.id_especie ,es.nom_cientifico, es.nom_especie, lower(es.tipo) as tipo, es.rango_altitudinal, es.ubicacion, b.nom_bioma ,es.descripcion, es.nom_ingles , estado.categoria, nicho.nom_nicho, per.ape_persona , fam.nom_familia, sub.nom_subfamilia, ord.nom_orden, cl.nom_clase, es.anio_descubrimiento, mi.nom_migracion  FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) LEFT JOIN personas as per ON (es.id_persona = per.id_persona) LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) ")


  tipo = {'tipo_1':'anfibio', 'tipo_2':'mamífero','tipo_3':'ave','tipo_4':'reptil','tipo_5':'pez'}
  
  estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
  especies = Especies.objects.distinct()
  ordenes = Ordenes.objects.filter().order_by('nom_orden')
  familias = Familias.objects.filter()
  subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
  genero = Genero.objects.filter().order_by('nom_genero')
  biomas = Biomas.objects.filter().order_by('nom_bioma')


  contar_flora = Flora.objects.filter().count()
  contar_fauna = Especies.objects.filter().count()
  contar_localidades = Locaciones.objects.filter().count()

  autores_flora = Flora.objects.filter().count()
  autores_fauna = Especies.objects.filter().count()

  contar_autores = autores_flora + autores_fauna

  contar_biomas = Biomas.objects.filter().count()

  #c = A.objects.filter(username='myname', status=0).count()

  ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")

  # Data Flora
  data_flora = Flora.objects.raw("SELECT fl.id_flora, fl.nom_flora, ge.nom_genero , b.nom_bioma, lower(fl.tipo_flora) as tipo_flora, fl.etimologia_flora, fl.diagnosis_flora, fl.distribucion_composicion_flora, fl.autor_flora FROM flora as fl INNER JOIN genero_flora as ge_f on (fl.id_flora = ge_f.id_flora) INNER JOIN genero as ge on (ge_f.id_genero = ge.id_genero) INNER JOIN flora_biomas as fb ON (fb.id_flora = fl.id_flora) INNER JOIN biomas as b ON (fb.id_bioma = b.id_bioma);")
  tipo_flora = {'tipo_1':'orquídea', 'tipo_2':'bromelia'}

  return render(request, "busquedaavanzada.html", { "contar_flora": contar_flora ,"contar_fauna": contar_fauna , "contar_localidades": contar_localidades ,"ubicacion":ubicacion,"contar_autores": contar_autores, "contar_biomas": contar_biomas,"tipo": tipo ,"tipo_flora": tipo_flora ,"data_flora": data_flora,"estado_conservacion": estado_conservacion, "especies":especies, "ordenes":ordenes, "data_fauna":data_fauna , "familias":familias , "subfamilias":subfamilias, "genero":genero, "biomas":biomas})


#------------------------------------------------------------------------------------
#-----------  Galerias 
def galeriabioma(request):
  biomas = ImagenesBiomas.objects.all()
  return render(request, "Galería_bioma.html", { 'bioma' : biomas })

def galeriabiomaFlora(request):
  biomas = ImagenesBiomas.objects.all()
  return render(request, "Flora/Galeria_biomaFlora.html", { 'bioma' : biomas })


def galeriabiomaFauna(request):
    biomasfaunas = ImagenesBiomas.objects.all()
    return render (request, "Fauna/Galeria")

              
# ----------- variable global para hacer los filtros ----------

id_bioma_ = 0

# ------ PARA FLORA --------
def flora(request, id_bioma):

  global id_bioma_
  id_bioma_ = id_bioma
  
  bioma_solo = Biomas.objects.get(id_bioma=id_bioma)
  return render(request, "flora.html", {'bioma_solo' : bioma_solo})


# ------ PARA FAUNA -----------
def fauna(request, id_bioma):
 
  global id_bioma_
  id_bioma_ = id_bioma
  
  bioma_solo = Biomas.objects.get(id_bioma=id_bioma)

  return render(request, "fauna.html", {'bioma_solo' : bioma_solo})
#
# //
# ------------------------------ FAUNA Y FLORA ------------------------------------------------------ DESDE AQUÍ

# Anfibios
def base(request):
    return render(request, "Fauna/Anfibios/dashboard.html" )

def busqueda_anfibio(request):
    consulta = " SELECT es.id_especie , \
	ifnull(es.nom_cientifico, 'Desconocido') as nom_cientifico, \
	ifnull(es.nom_especie, 'Desconocido') as nom_especie, \
	ifnull(lower(es.tipo) , 'Desconocido')  as tipo ,  \
	ifnull(es.rango_altitudinal,'Desconocido') as rango_altitudinal, \
	ifnull( es.ubicacion, 'Desconocido') as ubicacion, \
	ifnull(b.nom_bioma , 'Desconocido') as nom_bioma, \
	ifnull(es.descripcion, 'Desconocido') as descripcion, \
	ifnull( es.nom_ingles , 'Desconocido') as nom_ingles, \
	ifnull(lower(estado.categoria),'Desconocido') as categoria,  \
    ifnull(nicho.nom_nicho, 'Desconocido') as nom_nicho, \
    ifnull(per.ape_persona , 'Desconocido') as ape_persona, \
    ifnull(fam.nom_familia, 'Desconocido') as nom_familia, \
    ifnull(sub.nom_subfamilia, 'Desconocido') as nom_subfamilia, \
	ifnull(ord.nom_orden, 'Desconocido') as nom_orden, \
	ifnull(cl.nom_clase, 'Desconocido') as nom_clase , \
	ifnull(es.anio_descubrimiento,'Desconocido') as anio_descubrimiento, \
	ifnull(mi.nom_migracion , 'Desconocido') as nom_migracion  \
    FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) \
    LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) \
    LEFT JOIN personas as per ON (es.id_persona = per.id_persona) \
    LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) \
    LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) \
    LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) \
    LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) \
    LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) \
    LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) \
    LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) \
    where (b.id_bioma = "+str(id_bioma_)+" ) AND (lower(es.tipo) ='anfibio');"

    data_fauna = Especies.objects.raw(consulta)

    estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
    ordenes = Ordenes.objects.filter().order_by('nom_orden')
    familias = Familias.objects.filter()
    subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
    ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")

    if data_fauna is object:
        print() 

    return render(request, "Fauna/Anfibios/busqueda.html", { "data_fauna":data_fauna,"estado_conservacion":estado_conservacion, "ubicacion":ubicacion, "ordenes":ordenes,"familias":familias , "subfamilias":subfamilias})


def intro_anfibio(request):
 
    return render(request,"Fauna/Anfibios/intro.html")

def galeria_anfibio(request) :
    
    
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='anfibio'));")

    return render(request,"Fauna/Anfibios/galeria.html",{ 'imagen' : imagenes })

    

def noticias_anfibio(request):
    noticias = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.descripcion, es.nom_especie, es.anio_descubrimiento  FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+" ) AND (es.tipo='anfibio')) ORDER BY es.anio_descubrimiento DESC;") 

    return render(request,"Fauna/Anfibios/noticias.html",{ 'noticias' : noticias })

def lista_especies_anfibios(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen FROM imagenes AS i LEFT JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='anfibio'));")
    
    return render(request,"Fauna/Anfibios/lista_especie.html",{ 'imagen' : imagenes })

def ficha_tenica_anfibio(request,id_especie):
    #SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.id_especie=539) ;
    consulta = "SELECT  id_imagen, \
		 ifnull(i.imagen, 'Desconocido') as imagen, \
		 ifnull(es.tipo , 'Desconocido') as tipo, \
		 ifnull(f.nom_familia, 'Desconocido') as nom_familia, \
		 ifnull(es.nom_especie ,'Desconocido') as nom_especie \
        FROM imagenes AS i  \
        left JOIN especies as es on (i.id_especie = es.id_especie )  \
        left JOIN familias as f on (f.id_familia = es.id_familia ) \
        where (es.id_especie="+str(id_especie)+") ;" 

    imagenes = Imagenes.objects.raw(consulta)
    imagen=Imagenes.objects.filter(id_especie=id_especie)
    for i in imagen:
        imagen = Imagenes.objects.filter(id_imagen= i.id_imagen)
        break
    

    return render(request,"Fauna/Anfibios/ficha_tecnica.html",{ 'imagen' : imagen ,'imagenes':imagenes})

def como_citar_anfibio(request):
    return render(request,"Fauna/Anfibios/como_citar.html")

def uso_datos_anfibio(request):
    return render(request,"Fauna/Anfibios/uso_datos.html")

def agradecimientos_anfibio(request):
    return render(request,"Fauna/Anfibios/agradecimientos.html")

def quienes_somos_anfibio(request):
    return render(request,"Fauna/Anfibios/quienes_somos.html")

#reptiles

def basereptil(request):
    return render(request, "Fauna/Reptiles/dashboard.html")

def busqueda_reptil(request):

    consulta = " SELECT es.id_especie , \
	ifnull(es.nom_cientifico, 'Desconocido') as nom_cientifico, \
	ifnull(es.nom_especie, 'Desconocido') as nom_especie, \
	ifnull(lower(es.tipo) , 'Desconocido')  as tipo ,  \
	ifnull(es.rango_altitudinal,'Desconocido') as rango_altitudinal, \
	ifnull( es.ubicacion, 'Desconocido') as ubicacion, \
	ifnull(b.nom_bioma , 'Desconocido') as nom_bioma, \
	ifnull(es.descripcion, 'Desconocido') as descripcion, \
	ifnull( es.nom_ingles , 'Desconocido') as nom_ingles, \
	ifnull(lower(estado.categoria),'Desconocido') as categoria,  \
    ifnull(nicho.nom_nicho, 'Desconocido') as nom_nicho, \
    ifnull(per.ape_persona , 'Desconocido') as ape_persona, \
    ifnull(fam.nom_familia, 'Desconocido') as nom_familia, \
    ifnull(sub.nom_subfamilia, 'Desconocido') as nom_subfamilia, \
	ifnull(ord.nom_orden, 'Desconocido') as nom_orden, \
	ifnull(cl.nom_clase, 'Desconocido') as nom_clase , \
	ifnull(es.anio_descubrimiento,'Desconocido') as anio_descubrimiento, \
	ifnull(mi.nom_migracion , 'Desconocido') as nom_migracion  \
    FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) \
    LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) \
    LEFT JOIN personas as per ON (es.id_persona = per.id_persona) \
    LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) \
    LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) \
    LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) \
    LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) \
    LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) \
    LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) \
    LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) \
    where (b.id_bioma = "+str(id_bioma_)+" ) AND (lower(es.tipo) ='reptil');"

    data_fauna = Especies.objects.raw(consulta)
    estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
    ordenes = Ordenes.objects.filter().order_by('nom_orden')
    familias = Familias.objects.filter()
    subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
    ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")

    return render(request,"Fauna/Reptiles/busqueda.html", { "data_fauna":data_fauna,"estado_conservacion":estado_conservacion, "ubicacion":ubicacion, "ordenes":ordenes,"familias":familias , "subfamilias":subfamilias})

def intro_reptil(request):
    return render(request,"Fauna/Reptiles/intro.html")

def galeria_reptil(request):

    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='reptil'));")

    return render(request,"Fauna/Reptiles/galeria.html",{ 'imagen' : imagenes })
    

def noticias_reptil(request):
    noticias = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.descripcion, es.nom_especie, es.anio_descubrimiento  FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+" ) AND (es.tipo='reptil')) ORDER BY es.anio_descubrimiento DESC;") 

    return render(request,"Fauna/Reptiles/noticias.html",{ 'noticias' : noticias })

def lista_especies_reptil(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen FROM imagenes AS i LEFT JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='reptil'));")
    return render(request,"Fauna/Reptiles/lista_especie.html",{ 'imagen' : imagenes })


def ficha_tecnica_reptil(request,id_especie):
    imagenes = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.id_especie="+str(id_especie)+") ;")
    imagen=Imagenes.objects.filter(id_especie=id_especie)
    for i in imagen:
        imagen = Imagenes.objects.filter(id_imagen= i.id_imagen)
        break
    return render(request,"Fauna/Reptiles/ficha_tecnica.html",{ 'imagen' : imagen,'imagenes':imagenes })

def como_citar_reptil(request):
    return render(request,"Fauna/Reptiles/como_citar.html")

def uso_datos_reptil(request):
    return render(request,"Fauna/Reptiles/uso_datos.html")

def agradecimientos_reptil(request):
    return render(request,"Fauna/Reptiles/agradecimientos.html")

def quienes_somos_reptil(request):
    return render(request,"Fauna/Reptiles/quienes_somos.html")

#aves

def baseave(request):
    return render(request, "Fauna/Aves/dashboard.html")

def busqueda_ave(request):

    consulta = " SELECT es.id_especie , \
	ifnull(es.nom_cientifico, 'Desconocido') as nom_cientifico, \
	ifnull(es.nom_especie, 'Desconocido') as nom_especie, \
	ifnull(lower(es.tipo) , 'Desconocido')  as tipo ,  \
	ifnull(es.rango_altitudinal,'Desconocido') as rango_altitudinal, \
	ifnull( es.ubicacion, 'Desconocido') as ubicacion, \
	ifnull(b.nom_bioma , 'Desconocido') as nom_bioma, \
	ifnull(es.descripcion, 'Desconocido') as descripcion, \
	ifnull( es.nom_ingles , 'Desconocido') as nom_ingles, \
	ifnull(lower(estado.categoria),'Desconocido') as categoria,  \
    ifnull(nicho.nom_nicho, 'Desconocido') as nom_nicho, \
    ifnull(per.ape_persona , 'Desconocido') as ape_persona, \
    ifnull(fam.nom_familia, 'Desconocido') as nom_familia, \
    ifnull(sub.nom_subfamilia, 'Desconocido') as nom_subfamilia, \
	ifnull(ord.nom_orden, 'Desconocido') as nom_orden, \
	ifnull(cl.nom_clase, 'Desconocido') as nom_clase , \
	ifnull(es.anio_descubrimiento,'Desconocido') as anio_descubrimiento, \
	ifnull(mi.nom_migracion , 'Desconocido') as nom_migracion  \
    FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) \
    LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) \
    LEFT JOIN personas as per ON (es.id_persona = per.id_persona) \
    LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) \
    LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) \
    LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) \
    LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) \
    LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) \
    LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) \
    LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) \
    where (b.id_bioma = "+str(id_bioma_)+" ) AND (lower(es.tipo) ='ave');"

    data_fauna = Especies.objects.raw(consulta)
    estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
    ordenes = Ordenes.objects.filter().order_by('nom_orden')
    familias = Familias.objects.filter()
    subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
    ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")

    return render(request,"Fauna/Aves/busqueda.html", { "data_fauna":data_fauna,"estado_conservacion":estado_conservacion, "ubicacion":ubicacion, "ordenes":ordenes,"familias":familias , "subfamilias":subfamilias})

def intro_ave(request):
    return render(request,"Fauna/Aves/intro.html")

def galeria_ave(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='ave'));")
    return render(request,"Fauna/Aves/galeria.html",{ 'imagen' : imagenes })

def noticias_ave(request):
    noticias = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.descripcion, es.nom_especie, es.anio_descubrimiento  FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+" ) AND (es.tipo='ave')) ORDER BY es.anio_descubrimiento DESC;") 

    return render(request,"Fauna/Aves/noticias.html",{ 'noticias' : noticias })

def lista_especies_ave(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen FROM imagenes AS i LEFT JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='ave'));")
    return render(request,"Fauna/Aves/lista_especie.html",{ 'imagen' : imagenes })

def ficha_tecnica_ave(request,id_especie):
    imagenes = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.id_especie="+str(id_especie)+") ;")
    imagen=Imagenes.objects.filter(id_especie=id_especie)
    for i in imagen:
        imagen = Imagenes.objects.filter(id_imagen= i.id_imagen)
        break
    return render(request,"Fauna/Aves/ficha_tecnica.html",{ 'imagen' : imagen,'imagenes':imagenes })

def como_citar_ave(request):
    return render(request,"Fauna/Aves/como_citar.html")

def uso_datos_ave(request):
    return render(request,"Fauna/Aves/uso_datos.html")

def agradecimientos_ave(request):
    return render(request,"Fauna/Aves/agradecimientos.html")

def quienes_somos_ave(request):
    return render(request,"Fauna/Aves/quienes_somos.html")

#peces

def basepeces(request):
    return render(request, "Fauna/Peces/dashboard.html")

def busqueda_peces(request):

    consulta = " SELECT es.id_especie , \
	ifnull(es.nom_cientifico, 'Desconocido') as nom_cientifico, \
	ifnull(es.nom_especie, 'Desconocido') as nom_especie, \
	ifnull(lower(es.tipo) , 'Desconocido')  as tipo ,  \
	ifnull(es.rango_altitudinal,'Desconocido') as rango_altitudinal, \
	ifnull( es.ubicacion, 'Desconocido') as ubicacion, \
	ifnull(b.nom_bioma , 'Desconocido') as nom_bioma, \
	ifnull(es.descripcion, 'Desconocido') as descripcion, \
	ifnull( es.nom_ingles , 'Desconocido') as nom_ingles, \
	ifnull(lower(estado.categoria),'Desconocido') as categoria,  \
    ifnull(nicho.nom_nicho, 'Desconocido') as nom_nicho, \
    ifnull(per.ape_persona , 'Desconocido') as ape_persona, \
    ifnull(fam.nom_familia, 'Desconocido') as nom_familia, \
    ifnull(sub.nom_subfamilia, 'Desconocido') as nom_subfamilia, \
	ifnull(ord.nom_orden, 'Desconocido') as nom_orden, \
	ifnull(cl.nom_clase, 'Desconocido') as nom_clase , \
	ifnull(es.anio_descubrimiento,'Desconocido') as anio_descubrimiento, \
	ifnull(mi.nom_migracion , 'Desconocido') as nom_migracion  \
    FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) \
    LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) \
    LEFT JOIN personas as per ON (es.id_persona = per.id_persona) \
    LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) \
    LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) \
    LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) \
    LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) \
    LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) \
    LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) \
    LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) \
    where (b.id_bioma = "+str(id_bioma_)+" ) AND (lower(es.tipo) ='Pez');"

    data_fauna = Especies.objects.raw(consulta)
    estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
    ordenes = Ordenes.objects.filter().order_by('nom_orden')
    familias = Familias.objects.filter()
    subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
    ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")

    return render(request,"Fauna/Peces/busqueda.html", { "data_fauna":data_fauna,"estado_conservacion":estado_conservacion, "ubicacion":ubicacion, "ordenes":ordenes,"familias":familias , "subfamilias":subfamilias})

def intro_peces(request):
    return render(request,"Fauna/Peces/intro.html")

def galeria_peces(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='Pez'));")    
    return render(request,"Fauna/Peces/galeria.html",{ 'imagen' : imagenes })

def noticias_peces(request):
    noticias = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.descripcion, es.nom_especie, es.anio_descubrimiento  FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+" ) AND (es.tipo='Pez')) ORDER BY es.anio_descubrimiento DESC;") 

    return render(request,"Fauna/Peces/noticias.html",{ 'noticias' : noticias })

def lista_especies_peces(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen FROM imagenes AS i LEFT JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='Pez'));")
    return render(request,"Fauna/Peces/lista_especie.html",{ 'imagen' : imagenes })

def ficha_tecnica_peces(request,id_especie):
    imagenes = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.id_especie="+str(id_especie)+") ;")
    imagen=Imagenes.objects.filter(id_especie=id_especie)
    for i in imagen:
        imagen = Imagenes.objects.filter(id_imagen= i.id_imagen)
        break
    return render(request,"Fauna/Peces/ficha_tecnica.html",{ 'imagen' : imagen,'imagenes':imagenes })

def como_citar_peces(request):
    return render(request,"Fauna/Peces/como_citar.html")

def uso_datos_peces(request):
    return render(request,"Fauna/Peces/uso_datos.html")

def agradecimientos_peces(request):
    return render(request,"Fauna/Peces/agradecimientos.html")

def quienes_somos_peces(request):
    return render(request,"Fauna/Peces/quienes_somos.html")


#mamiferos - galeria listo




def basemamifero(request):
    return render(request, "Fauna/Mamiferos/dashboard.html")

def busqueda_mamifero(request):
    consulta = " SELECT es.id_especie , \
	ifnull(es.nom_cientifico, 'Desconocido') as nom_cientifico, \
	ifnull(es.nom_especie, 'Desconocido') as nom_especie, \
	ifnull(lower(es.tipo) , 'Desconocido')  as tipo ,  \
	ifnull(es.rango_altitudinal,'Desconocido') as rango_altitudinal, \
	ifnull( es.ubicacion, 'Desconocido') as ubicacion, \
	ifnull(b.nom_bioma , 'Desconocido') as nom_bioma, \
	ifnull(es.descripcion, 'Desconocido') as descripcion, \
	ifnull( es.nom_ingles , 'Desconocido') as nom_ingles, \
	ifnull(lower(estado.categoria),'Desconocido') as categoria,  \
    ifnull(nicho.nom_nicho, 'Desconocido') as nom_nicho, \
    ifnull(per.ape_persona , 'Desconocido') as ape_persona, \
    ifnull(fam.nom_familia, 'Desconocido') as nom_familia, \
    ifnull(sub.nom_subfamilia, 'Desconocido') as nom_subfamilia, \
	ifnull(ord.nom_orden, 'Desconocido') as nom_orden, \
	ifnull(cl.nom_clase, 'Desconocido') as nom_clase , \
	ifnull(es.anio_descubrimiento,'Desconocido') as anio_descubrimiento, \
	ifnull(mi.nom_migracion , 'Desconocido') as nom_migracion  \
    FROM especies as es LEFT JOIN estado_conservacion as estado ON (es.id_estado_conservacion = estado.id_estado_conservacion) \
    LEFT JOIN nichotrofico as nicho ON (es.id_nicho_trofico = nicho.id_nicho_trofico) \
    LEFT JOIN personas as per ON (es.id_persona = per.id_persona) \
    LEFT JOIN familias as fam ON (es.id_familia = fam.id_familia ) \
    LEFT JOIN subfamilias as sub ON (es.id_subfamilia = sub.id_subfamilia) \
    LEFT JOIN ordenes as ord ON (es.id_orden = ord.id_orden) \
    LEFT JOIN clases as cl ON (es.id_clase = cl.id_clase) \
    LEFT JOIN biomas_especies as be ON (be.id_especie = es.id_especie) \
    LEFT JOIN biomas as b ON (b.id_bioma = be.id_bioma) \
    LEFT JOIN migracion_aves as mi ON (es.id_migracion = mi.id_migracion) \
    where (b.id_bioma = "+str(id_bioma_)+" ) AND (lower(es.tipo) ='mamífero');"

    data_fauna = Especies.objects.raw(consulta)
    estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
    ordenes = Ordenes.objects.filter().order_by('nom_orden')
    familias = Familias.objects.filter()
    subfamilias = Subfamilias.objects.filter().order_by('nom_subfamilia')
    ubicacion = Especies.objects.raw("SELECT DISTINCT id_especie, ubicacion FROM especies where ubicacion is not null")
    

    return render(request,"Fauna/Mamiferos/busqueda.html", { "data_fauna":data_fauna,"estado_conservacion":estado_conservacion, "ubicacion":ubicacion, "ordenes":ordenes,"familias":familias , "subfamilias":subfamilias})

def intro_mamifero(request):
    return render(request,"Fauna/Mamiferos/intro.html")


def galeria_mamifero(request):
  
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='mamífero'));")

    #imagenes = Imagenes.objects.all()

    return render(request,"Fauna/Mamiferos/galeria.html",{ 'imagen' : imagenes })

def noticias_mamifero(request):

    noticias = Imagenes.objects.raw("SELECT id_imagen, i.imagen, es.descripcion, es.nom_especie, es.anio_descubrimiento  FROM imagenes AS i left JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+" ) AND (es.tipo='mamífero')) ORDER BY es.anio_descubrimiento DESC;") 

    return render(request,"Fauna/Mamiferos/noticias.html",{ 'noticias' : noticias })

def lista_especies_mamifero(request):
    imagenes = Imagenes.objects.raw("SELECT id_imagen, i.imagen FROM imagenes AS i LEFT JOIN biomas_especies as d on (i.id_especie = d.id_especie ) left JOIN especies as es on (i.id_especie = es.id_especie ) where ((d.id_bioma = "+str(id_bioma_)+") AND (es.tipo='mamífero'));")
    for i in imagenes:
        print(i)

    return render(request,"Fauna/Mamiferos/lista_especie.html",{ 'imagen' : imagenes })

def ficha_tecnica_mamifero(request,id_especie):
    imagenes = Imagenes.objects.raw("SELECT  id_imagen, i.imagen, es.tipo , f.nom_familia, es.nom_especie FROM imagenes AS i left JOIN especies as es on (i.id_especie = es.id_especie ) left JOIN familias as f on (f.id_familia = es.id_familia ) where (es.id_especie="+str(id_especie)+") ;")
    imagen=Imagenes.objects.filter(id_especie=id_especie)
    for i in imagen:
        imagen = Imagenes.objects.filter(id_imagen= i.id_imagen)
        break
        
    return render(request,"Fauna/Mamiferos/ficha_tecnica.html",{ 'imagen' : imagen ,'imagenes' : imagenes } )
    

def como_citar_mamifero(request):
    return render(request,"Fauna/Mamiferos/como_citar.html")

def uso_datos_mamifero(request):
    return render(request,"Fauna/Mamiferos/uso_datos.html")

def agradecimientos_mamifero(request):
    return render(request,"Fauna/Mamiferos/agradecimientos.html")

def quienes_somos_mamifero(request):
    return render(request,"Fauna/Mamiferos/quienes_somos.html")

#Bromelias

def basebromelia(request):
    return render(request, "Flora/Bromelia/dashboard.html")

def busqueda_bromelia(request):


    bromelias = FloraImagen.objects.raw("SELECT id_flora_imagen,fl.id_flora, fl.nom_flora, imf.imagenflora, g.nom_genero FROM flora_imagen as imf LEFT JOIN flora as fl ON (imf.id_flora = fl.id_flora) LEFT JOIN genero_flora as gf ON (fl.id_flora = gf.id_flora) LEFT JOIN genero as g ON (gf.id_genero = g.id_genero) LEFT JOIN flora_biomas as fb ON (fl.id_flora = fb.id_flora) LEFT JOIN biomas as b ON (fb.id_bioma = b.id_bioma) WHERE fl.tipo_flora = 'Bromelia' AND (b.id_bioma = 2) ORDER BY fl.id_flora");

    data = Flora.objects.raw("SELECT fl.id_flora, fl.nom_flora, ge.nom_genero , b.nom_bioma, lower(fl.tipo_flora) as tipo_flora, fl.etimologia_flora, fl.diagnosis_flora, fl.distribucion_composicion_flora, fl.autor_flora FROM flora as fl INNER JOIN genero_flora as ge_f on (fl.id_flora = ge_f.id_flora) INNER JOIN genero as ge on (ge_f.id_genero = ge.id_genero) INNER JOIN flora_biomas as fb ON (fb.id_flora = fl.id_flora) INNER JOIN biomas as b ON (fb.id_bioma = b.id_bioma) WHERE( fl.tipo_flora = 'Bromelia' ) and (b.id_bioma="+str(id_bioma_)+");")
   
    genero = Genero.objects.filter().order_by('nom_genero')
    
    return render(request,"Flora/Bromelia/busqueda.html", { 'data' : data , 'genero' : genero})

def intro_bromelia(request):
    return render(request,"Flora/Bromelia/intro.html")

def galeria_bromelia(request):

    bromelias = FloraImagen.objects.raw("SELECT id_flora_imagen,fl.id_flora, fl.nom_flora, imf.imagenflora, g.nom_genero FROM flora_imagen as imf LEFT JOIN flora as fl ON (imf.id_flora = fl.id_flora) LEFT JOIN genero_flora as gf ON (fl.id_flora = gf.id_flora) LEFT JOIN genero as g ON (gf.id_genero = g.id_genero) LEFT JOIN flora_biomas as fb ON (fl.id_flora = fb.id_flora) LEFT JOIN biomas as b ON (fb.id_bioma = b.id_bioma) WHERE fl.tipo_flora = 'Bromelia' AND (b.id_bioma = "+str(id_bioma_)+") ORDER BY fl.id_flora;")
    return render(request,"Flora/Bromelia/galeria.html", { 'bromelias' : bromelias})

def noticias_bromelia(request):
    noticias = FloraImagen.objects.raw("SELECT id_flora_imagen, i.imagenflora, fl.nom_flora, fl.etimologia_flora, fl.diagnosis_flora,fl.distribucion_composicion_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_biomas as fb on (fb.id_flora = i.id_flora ) where ((fb.id_bioma = "+str(id_bioma_)+" ) AND (fl.tipo_flora='Bromelia')) ORDER BY  fl.id_flora DESC;") 

    return render(request,"Flora/Bromelia/noticias.html",{ 'noticias' : noticias })

def lista_especies_bromelia(request):
    imagenes = FloraImagen.objects.raw("SELECT id_flora_imagen, i.imagenflora, fl.nom_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_biomas as fb on (fb.id_flora = i.id_flora ) where ((fb.id_bioma = "+str(id_bioma_)+" ) AND (fl.tipo_flora='Bromelia')) ORDER BY  fl.id_flora DESC;") 
    return render(request,"Flora/Bromelia/lista_especie.html",{ 'imagen' :imagenes})

def ficha_tecnica_bromelia(request,id_flora):
    imagenes = FloraImagen.objects.raw("SELECT  id_flora_imagen, i.imagenflora, es.nom_flora FROM flora_imagen AS i left JOIN flora as es on (i.id_flora = es.id_flora )  where (es.id_flora="+str(id_flora)+") ;")
    imagen = FloraImagen.objects.filter(id_flora= id_flora)
    for i in imagen:
        imagen = FloraImagen.objects.filter(id_flora_imagen= i.id_flora_imagen)
        break
        
   
    return render(request,"Flora/Bromelia/ficha_tecnica.html",{ 'imagen' :imagen,'imagenes':imagenes} )

def como_citar_bromelia(request):
    return render(request,"Flora/Bromelia/como_citar.html")

def uso_datos_bromelia(request):
    return render(request,"Flora/Bromelia/uso_datos.html")

def agradecimientos_bromelia(request):
    return render(request,"Flora/Bromelia/agradecimientos.html")

def quienes_somos_bromelia(request):
    return render(request,"Flora/Bromelia/quienes_somos.html")

#Orquideas
def baseorquidea(request):
    return render(request, "Flora/Orquidea/dashboard.html")

def busqueda_orquidea(request):

    data = Flora.objects.raw("SELECT fl.id_flora, fl.nom_flora, ge.nom_genero , b.nom_bioma, lower(fl.tipo_flora) as tipo_flora, fl.etimologia_flora, fl.diagnosis_flora, fl.distribucion_composicion_flora, fl.autor_flora FROM flora as fl INNER JOIN genero_flora as ge_f on (fl.id_flora = ge_f.id_flora) INNER JOIN genero as ge on (ge_f.id_genero = ge.id_genero) INNER JOIN flora_biomas as fb ON (fb.id_flora = fl.id_flora) INNER JOIN biomas as b ON (fb.id_bioma = b.id_bioma) WHERE( fl.tipo_flora = 'orquídea' ) and (b.id_bioma="+str(id_bioma_)+");")
   
    genero = Genero.objects.filter().order_by('nom_genero')

    return render(request,"Flora/Orquidea/busqueda.html", { 'data' : data , 'genero' : genero})

def intro_orquidea(request):
    return render(request,"Flora/Orquidea/intro.html")

def galeria_orquidea(request):
    orquidea = FloraImagen.objects.raw("SELECT id_flora_imagen,fl.id_flora, fl.nom_flora, imf.imagenflora, g.nom_genero FROM flora_imagen as imf LEFT JOIN flora as fl ON (imf.id_flora = fl.id_flora) LEFT JOIN genero_flora as gf ON (fl.id_flora = gf.id_flora) LEFT JOIN genero as g ON (gf.id_genero = g.id_genero) LEFT JOIN flora_biomas as fb ON (fl.id_flora = fb.id_flora) LEFT JOIN biomas as b ON (fb.id_bioma = b.id_bioma) WHERE fl.tipo_flora = 'orquídea' AND (b.id_bioma = "+str(id_bioma_)+") ORDER BY fl.id_flora;")
    return render(request,"Flora/Orquidea/galeria.html" , { 'orquidea' : orquidea})

def noticias_orquidea(request):
    noticias = FloraImagen.objects.raw("SELECT id_flora_imagen, i.imagenflora, fl.nom_flora, fl.etimologia_flora, fl.diagnosis_flora,fl.distribucion_composicion_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_biomas as fb on (fb.id_flora = i.id_flora ) where ((fb.id_bioma = "+str(id_bioma_)+" ) AND (fl.tipo_flora='orquídea')) ORDER BY  fl.id_flora DESC;") 
    for i in noticias:
        print(i.id_flora_imagen)
    

    return render(request,"Flora/Orquidea/noticias.html",{ 'noticias' : noticias })

def lista_especies_orquidea(request):
    imagenes = FloraImagen.objects.raw("SELECT id_flora_imagen, i.imagenflora, fl.nom_flora FROM flora_imagen AS i left JOIN flora as fl on (i.id_flora = fl.id_flora ) left JOIN flora_biomas as fb on (fb.id_flora = i.id_flora ) where ((fb.id_bioma = "+str(id_bioma_)+" ) AND (fl.tipo_flora='orquídea')) ORDER BY  fl.id_flora DESC;") 
    
    for i in imagenes:
        print(i.id_flora_imagen)
    return render(request,"Flora/Orquidea/lista_especie.html",{'imagen' : imagenes})

def ficha_tecnica_orquidea(request,id_flora):
    imagenes = FloraImagen.objects.raw("SELECT  id_flora_imagen, i.imagenflora, es.nom_flora FROM flora_imagen AS i left JOIN flora as es on (i.id_flora = es.id_flora )  where (es.id_flora="+str(id_flora)+") ;")
    imagen = FloraImagen.objects.filter(id_flora= id_flora)
    for i in imagen:
        imagen = FloraImagen.objects.filter(id_flora_imagen= i.id_flora_imagen)
        break
        
    return render(request,"Flora/Orquidea/ficha_tecnica.html",{'imagen' : imagen,'imagenes':imagenes})

def como_citar_orquidea(request):
    return render(request,"Flora/Orquidea/como_citar.html")

def uso_datos_orquidea(request):
    return render(request,"Flora/Orquidea/uso_datos.html")

def agradecimientos_orquidea(request):
    return render(request,"Flora/Orquidea/agradecimientos.html")

def quienes_somos_orquidea(request):
    return render(request,"Flora/Orquidea/quienes_somos.html")



















#-------------

class GaleAve(TemplateView):
    template_name = 'Busquedas/Aves/Especies_GaleriaAve.html'

    def get_message(self):
        return u'AVES'

    def get_context_data(self, **kwargs):
        context = super(GaleAve, self).get_context_data(**kwargs)
        context = dict()
        context['id'] = 100
        context['AV'] = self.get_message()
        context['bioma_solo'] = Biomas.objects.get(id_bioma=kwargs['id_bioma'])
        
        return context
#def GaleAve(request):
   # return render(request, "Busquedas/Aves/Especies_GaleriaAve.html")

#-------------



class GaleReptil(TemplateView):
    template_name = 'Busquedas/Reptiles/Especies_GaleriaReptil.html'

    def get_message(self):
        return u'REPTIL'

    def get_context_data(self, **kwargs):
        context = super(GaleReptil, self).get_context_data(**kwargs)
        context = dict()
        context['id'] = 100
        context['R'] = self.get_message()
        context['bioma_solo'] = Biomas.objects.get(id_bioma=kwargs['id_bioma'])
        return context
#def GaleReptil(request):
    #print("REPTIL")
    #ctx={"R":"2"}
    #obtener_id(ctx)
 #   return render(request, "Busquedas/Reptiles/Especies_GaleriaReptil.html")

#-------------

#-------------

#-------------

#-------------

#-------------



def IntroAves(request):
    return render(request, "Busquedas/Ave/Intro_Aves.html")


#-------------

  

def page_not_found404(request, exception):
    return render(request, "404.html")






#------------

def LateralD(request, id_bioma, tipo):
  
    return render(request, "Block_MLateral.html", {'id_bioma':id_bioma,'tipo' : tipo } )



#----------

def sugerencias(request):
    if request.method == "POST":
        print(request.POST["asunto"])
        print(request.POST["nombre"])
        print(request.POST["comentario"])
        print(request.POST["email"])
        print(request.POST["celular"])
        doc = request.FILES
        print(doc['file'].name)

        #encoded_string = base64.b64encode(doc['file'].read())
        #imagen_b64='data:image/%s;base64,%s' % (format, encoded_string)
        #print(encoded_string)
        nombre=request.POST["nombre"]
        subject =request.POST["asunto"]
        message =request.POST["comentario"]
        email_from = settings.EMAIL_HOST_USER
        to = request.POST["email"]
        celular=request.POST["celular"]
        
        html_content = """
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" style="font-family:arial, 'helvetica neue', helvetica, sans-serif">
 <head> 
  <meta charset="UTF-8"> 
  <meta content="width=device-width, initial-scale=1" name="viewport"> 
  <meta name="x-apple-disable-message-reformatting"> 
  <meta http-equiv="X-UA-Compatible" content="IE=edge"> 
  <meta content="telephone=no" name="format-detection"> 
  <title>Nueva plantilla</title> 
  <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]--> 
  <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> 
  <!--[if gte mso 9]>
<xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG></o:AllowPNG>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
</xml>
<![endif]--> 
  <style type="text/css">
#outlook a {
	padding:0;
}
.es-button {
	mso-style-priority:100!important;
	text-decoration:none!important;
}
a[x-apple-data-detectors] {
	color:inherit!important;
	text-decoration:none!important;
	font-size:inherit!important;
	font-family:inherit!important;
	font-weight:inherit!important;
	line-height:inherit!important;
}
.es-desk-hidden {
	display:none;
	float:left;
	overflow:hidden;
	width:0;
	max-height:0;
	line-height:0;
	mso-hide:all;
} 
[data-ogsb] .es-button {
	border-width:0!important;
	padding:10px 30px 10px 30px!important;
}
@media only screen and (max-width:600px) {p, ul li, ol li, a { line-height:150%!important } h1, h2, h3, h1 a, h2 a, h3 a { line-height:120% } h1 { font-size:36px!important; text-align:center } h2 { font-size:26px!important; text-align:center } h3 { font-size:20px!important; text-align:center } .es-header-body h1 a, .es-content-body h1 a, .es-footer-body h1 a { font-size:36px!important } .es-header-body h2 a, .es-content-body h2 a, .es-footer-body h2 a { font-size:26px!important } .es-header-body h3 a, .es-content-body h3 a, .es-footer-body h3 a { font-size:20px!important } .es-menu td a { font-size:14px!important } .es-header-body p, .es-header-body ul li, .es-header-body ol li, .es-header-body a { font-size:14px!important } .es-content-body p, .es-content-body ul li, .es-content-body ol li, .es-content-body a { font-size:16px!important } .es-footer-body p, .es-footer-body ul li, .es-footer-body ol li, .es-footer-body a { font-size:14px!important } .es-infoblock p, .es-infoblock ul li, .es-infoblock ol li, .es-infoblock a { font-size:12px!important } *[class="gmail-fix"] { display:none!important } .es-m-txt-c, .es-m-txt-c h1, .es-m-txt-c h2, .es-m-txt-c h3 { text-align:center!important } .es-m-txt-r, .es-m-txt-r h1, .es-m-txt-r h2, .es-m-txt-r h3 { text-align:right!important } .es-m-txt-l, .es-m-txt-l h1, .es-m-txt-l h2, .es-m-txt-l h3 { text-align:left!important } .es-m-txt-r img, .es-m-txt-c img, .es-m-txt-l img { display:inline!important } .es-button-border { display:block!important } a.es-button, button.es-button { font-size:20px!important; display:block!important; border-left-width:0px!important; border-right-width:0px!important } .es-adaptive table, .es-left, .es-right { width:100%!important } .es-content table, .es-header table, .es-footer table, .es-content, .es-footer, .es-header { width:100%!important; max-width:600px!important } .es-adapt-td { display:block!important; width:100%!important } .adapt-img { width:100%!important; height:auto!important } .es-m-p0 { padding:0!important } .es-m-p0r { padding-right:0!important } .es-m-p0l { padding-left:0!important } .es-m-p0t { padding-top:0!important } .es-m-p0b { padding-bottom:0!important } .es-m-p20b { padding-bottom:20px!important } .es-mobile-hidden, .es-hidden { display:none!important } tr.es-desk-hidden, td.es-desk-hidden, table.es-desk-hidden { width:auto!important; overflow:visible!important; float:none!important; max-height:inherit!important; line-height:inherit!important } tr.es-desk-hidden { display:table-row!important } table.es-desk-hidden { display:table!important } td.es-desk-menu-hidden { display:table-cell!important } .es-menu td { width:1%!important } table.es-table-not-adapt, .esd-block-html table { width:auto!important } table.es-social { display:inline-block!important } table.es-social td { display:inline-block!important } .es-m-p5 { padding:5px!important } .es-m-p5t { padding-top:5px!important } .es-m-p5b { padding-bottom:5px!important } .es-m-p5r { padding-right:5px!important } .es-m-p5l { padding-left:5px!important } .es-m-p10 { padding:10px!important } .es-m-p10t { padding-top:10px!important } .es-m-p10b { padding-bottom:10px!important } .es-m-p10r { padding-right:10px!important } .es-m-p10l { padding-left:10px!important } .es-m-p15 { padding:15px!important } .es-m-p15t { padding-top:15px!important } .es-m-p15b { padding-bottom:15px!important } .es-m-p15r { padding-right:15px!important } .es-m-p15l { padding-left:15px!important } .es-m-p20 { padding:20px!important } .es-m-p20t { padding-top:20px!important } .es-m-p20r { padding-right:20px!important } .es-m-p20l { padding-left:20px!important } .es-m-p25 { padding:25px!important } .es-m-p25t { padding-top:25px!important } .es-m-p25b { padding-bottom:25px!important } .es-m-p25r { padding-right:25px!important } .es-m-p25l { padding-left:25px!important } .es-m-p30 { padding:30px!important } .es-m-p30t { padding-top:30px!important } .es-m-p30b { padding-bottom:30px!important } .es-m-p30r { padding-right:30px!important } .es-m-p30l { padding-left:30px!important } .es-m-p35 { padding:35px!important } .es-m-p35t { padding-top:35px!important } .es-m-p35b { padding-bottom:35px!important } .es-m-p35r { padding-right:35px!important } .es-m-p35l { padding-left:35px!important } .es-m-p40 { padding:40px!important } .es-m-p40t { padding-top:40px!important } .es-m-p40b { padding-bottom:40px!important } .es-m-p40r { padding-right:40px!important } .es-m-p40l { padding-left:40px!important } }
</style> 
 </head> 
 <body style="width:100%;font-family:arial, 'helvetica neue', helvetica, sans-serif;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;padding:0;Margin:0"> 
  <div class="es-wrapper-color" style="background-color:#FAFAFA"> 
   <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#fafafa"></v:fill>
			</v:background>
		<![endif]--> 
   <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;padding:0;Margin:0;width:100%;height:100%;background-repeat:repeat;background-position:center top;background-color:#FAFAFA"> 
     <tr> 
      <td valign="top" style="padding:0;Margin:0"> 
       <table cellpadding="0" cellspacing="0" class="es-header" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"> 
         <tr> 
          <td align="center" style="padding:0;Margin:0"> 
           <table bgcolor="#ffffff" class="es-header-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px"> 
             <tr> 
              <td align="left" style="Margin:0;padding-top:10px;padding-bottom:10px;padding-left:20px;padding-right:20px"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                 <tr> 
                  <td class="es-m-p0r" valign="top" align="center" style="padding:0;Margin:0;width:560px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;display:none"></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table></td> 
         </tr> 
       </table> 
       <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
         <tr> 
          <td align="center" style="padding:0;Margin:0"> 
           <table bgcolor="#a5e7ab" class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:#a5e7ab;background-repeat:no-repeat;width:600px;background-image:url(https://kcsfin.stripocdn.email/content/guids/CABINET_4811abad29a97d688dae7b89e75be5a1/images/whatsapp_image_20211012_at_115148.jpeg);background-position:center top" background="https://kcsfin.stripocdn.email/content/guids/CABINET_4811abad29a97d688dae7b89e75be5a1/images/whatsapp_image_20211012_at_115148.jpeg"> 
             <tr> 
              <td align="left" style="Margin:0;padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:30px"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                 <tr> 
                  <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;padding-top:10px;padding-bottom:10px;font-size:0px"><img src="https://kcsfin.stripocdn.email/content/guids/CABINET_4811abad29a97d688dae7b89e75be5a1/images/whatsapp_image_20211012_at_115148_1.jpeg" alt style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="100" height="100"></td> 
                     </tr> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;padding-bottom:10px"><h1 style="Margin:0;line-height:46px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:46px;font-style:normal;font-weight:bold;color:#333333">Nueva Sugerencia</h1></td> 
                     </tr> 
                     <tr> 
                      <td align="center" class="es-m-p0r es-m-p0l" style="Margin:0;padding-top:5px;padding-bottom:5px;padding-left:40px;padding-right:40px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:21px;color:#333333;font-size:14px"><strong>Nombre:$nombre<br>Celular: $celular<br>Correo: $correo</strong><br><br><br></p></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
             <tr> 
              <td align="left" style="Margin:0;padding-top:10px;padding-bottom:10px;padding-left:20px;padding-right:20px"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                 <tr> 
                  <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:separate;border-spacing:0px;border-left:2px dashed #cccccc;border-right:2px dashed #cccccc;border-top:2px dashed #cccccc;border-bottom:2px dashed #cccccc;border-radius:5px" role="presentation"> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;padding-top:20px;padding-left:20px;padding-right:20px"><h2 style="Margin:0;line-height:31px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:26px;font-style:normal;font-weight:bold;color:#333333">Comentario:</h2></td> 
                     </tr> 
                     <tr> 
                      <td align="center" style="Margin:0;padding-top:10px;padding-bottom:20px;padding-left:20px;padding-right:20px"><h1 style="Margin:0;line-height:17px;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;font-size:14px;font-style:normal;font-weight:bold;color:#5c68e2">$message</h1></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table></td> 
         </tr> 
       </table> 
       <table cellpadding="0" cellspacing="0" class="es-footer" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%;background-color:transparent;background-repeat:repeat;background-position:center top"> 
         <tr> 
          <td align="center" style="padding:0;Margin:0"> 
           <table class="es-footer-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:640px"> 
             <tr> 
              <td align="left" style="Margin:0;padding-top:20px;padding-bottom:20px;padding-left:20px;padding-right:20px"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                 <tr> 
                  <td align="left" style="padding:0;Margin:0;width:600px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;padding-top:15px;padding-bottom:15px;font-size:0"> 
                       <table cellpadding="0" cellspacing="0" class="es-table-not-adapt es-social" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr> 
                          <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><img title="Facebook" src="https://kcsfin.stripocdn.email/content/assets/img/social-icons/logo-black/facebook-logo-black.png" alt="Fb" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></td> 
                          <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><img title="Twitter" src="https://kcsfin.stripocdn.email/content/assets/img/social-icons/logo-black/twitter-logo-black.png" alt="Tw" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></td> 
                          <td align="center" valign="top" style="padding:0;Margin:0;padding-right:40px"><img title="Instagram" src="https://kcsfin.stripocdn.email/content/assets/img/social-icons/logo-black/instagram-logo-black.png" alt="Inst" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></td> 
                          <td align="center" valign="top" style="padding:0;Margin:0"><img title="Youtube" src="https://kcsfin.stripocdn.email/content/assets/img/social-icons/logo-black/youtube-logo-black.png" alt="Yt" width="32" height="32" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic"></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                     <tr> 
                      <td align="center" style="padding:0;Margin:0;padding-bottom:35px"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:18px;color:#333333;font-size:12px">Style Casual&nbsp;© 2021 Style Casual, Inc. All Rights Reserved.</p><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:18px;color:#333333;font-size:12px">4562 Hazy Panda Limits, Chair Crossing, Kentucky, US, 607898</p></td> 
                     </tr> 
                     <tr> 
                      <td style="padding:0;Margin:0"> 
                       <table cellpadding="0" cellspacing="0" width="100%" class="es-menu" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                         <tr class="links"> 
                          <td align="center" valign="top" width="33.33%" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:5px;padding-bottom:5px;border:0"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#999999;font-size:12px">Visit Us </a></td> 
                          <td align="center" valign="top" width="33.33%" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:5px;padding-bottom:5px;border:0;border-left:1px solid #cccccc"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#999999;font-size:12px">Privacy Policy</a></td> 
                          <td align="center" valign="top" width="33.33%" style="Margin:0;padding-left:5px;padding-right:5px;padding-top:5px;padding-bottom:5px;border:0;border-left:1px solid #cccccc"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:none;display:block;font-family:arial, 'helvetica neue', helvetica, sans-serif;color:#999999;font-size:12px">Terms of Use</a></td> 
                         </tr> 
                       </table></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table></td> 
         </tr> 
       </table> 
       <table cellpadding="0" cellspacing="0" class="es-content" align="center" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;table-layout:fixed !important;width:100%"> 
         <tr> 
          <td class="es-info-area" align="center" style="padding:0;Margin:0"> 
           <table class="es-content-body" align="center" cellpadding="0" cellspacing="0" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px;background-color:transparent;width:600px" bgcolor="#FFFFFF"> 
             <tr> 
              <td align="left" style="padding:20px;Margin:0"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                 <tr> 
                  <td align="center" valign="top" style="padding:0;Margin:0;width:560px"> 
                   <table cellpadding="0" cellspacing="0" width="100%" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;border-collapse:collapse;border-spacing:0px"> 
                     <tr> 
                      <td align="center" class="es-infoblock" style="padding:0;Margin:0;line-height:14px;font-size:12px;color:#CCCCCC"><p style="Margin:0;-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;font-family:arial, 'helvetica neue', helvetica, sans-serif;line-height:14px;color:#CCCCCC;font-size:12px"><a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:12px"></a>No longer want to receive these emails?&nbsp;<a href="" target="_blank" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:12px">Unsubscribe</a>.<a target="_blank" href="" style="-webkit-text-size-adjust:none;-ms-text-size-adjust:none;mso-line-height-rule:exactly;text-decoration:underline;color:#CCCCCC;font-size:12px"></a></p></td> 
                     </tr> 
                   </table></td> 
                 </tr> 
               </table></td> 
             </tr> 
           </table></td> 
         </tr> 
       </table></td> 
     </tr> 
   </table> 
  </div>  
 </body>
</html>
"""
        s = Template(html_content).safe_substitute(message=message,celular=celular,correo=to,nombre=nombre)
       # print(html_content % (message))

        try:
             print("hola")
             msg = EmailMultiAlternatives(subject, s , email_from, [email_from])
             msg.attach_alternative(s, "text/html")
             msg.attach(doc['file'].name,doc['file'].read(), doc['file'].content_type)
             msg.attach(doc['file'].name,doc['file'].read(), doc['file'].content_type)
             msg.send()
             post = "si"
           #  mailresult = send_mail(subject, "Enviado desde: " + email_from + "\n\n" + message,settings.DEFAULT_FROM_EMAIL, [to], fail_silently=False)
             #print(mailresult)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

       # recipient_list = ["gadpeoeloro@gmail.com"]
       # send_mail(subject,message,email_from,recipient_list)

        return render(request, "sugerencias.html",{'post' : post})

        
    return render(request, "sugerencias.html")
     

#alternativo
'''def send_user_mail(user):
    subject = 'Titulo del correo'
    template = get_template('templates/mi_template_correo.html')

    content = template.render({
        'user': user,
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    ''",
                                    settings..EMAIL_HOST_USER, #Remitente
                                    [user.email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()
'''

"""
 
  class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = familia.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
 
 
 
 
 """



