from django.contrib import admin
from django.contrib.admin.actions import delete_selected

#from .models import familia
#admin.site.register(familia)

# Register your models here.

"""mensaje de errror usuario/contrasena"""





"""
class biomaAdmin (admin.ModelAdmin):
    list_display = ("nom_bioma","sigla_bioma","des_altitudinal_bioma","has_altitudinal_bioma","remanencia","ext_bioma")

from .models import bioma
admin.site.register(bioma, biomaAdmin)




class locacionAdmin (admin.ModelAdmin):
    list_display = ("nom_locacion","sigla_locacion","alt_locacion","nombre_parroquia","nombre_canton","longitud")
    

from .models import locacion
admin.site.register(locacion, locacionAdmin)




class estadoAdmin (admin.ModelAdmin):
    list_display = ("categoria","sigla","descripcion")

from .models import estadoconservacion
admin.site.register(estadoconservacion, estadoAdmin)



class faunaAdmin (admin.ModelAdmin):
    list_display = ("nom_especie","nom_cientifico","nom_ingles","tipo","rango_altitudinal","ubicacion","descripcion")
    #list_filter = ("id_estado_conservacion")
    search_fields = ("nom_especie","nom_cientifico","nom_ingles")
    
from .models import fauna
admin.site.register(fauna, faunaAdmin)


class imagenAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","id_especie","autor","imagen")
    
from .models import imagen_fauna
admin.site.register(imagen_fauna, imagenAdmin)


class faunaLocacionAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_locacion")
    list_filter = (
        ('id_locacion', admin.RelatedOnlyFieldListFilter),
    )
    #list_filter = ("id_locacion")

from .models import fauna_locacion
admin.site.register(fauna_locacion, faunaLocacionAdmin)

class faunaBiomaAdmin (admin.ModelAdmin):
    list_display = ("id_especie","id_bioma")
    list_filter = (
        ('id_bioma', admin.RelatedOnlyFieldListFilter),
    )
    #list_filter = ('fauna','bioma')
  

from .models import fauna_biomas
admin.site.register(fauna_biomas, faunaBiomaAdmin)


"""

class clasesAdmin (admin.ModelAdmin):
    list_display = ("id_clase","nom_clase","tipo","abund_clase","num_ord_clase")

    def get_actions(self, request):
        actions = super(clasesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_clase"),
    )
  
from .models import Clases
admin.site.register(Clases, clasesAdmin)

class ordenesAdmin (admin.ModelAdmin):
    list_display = ("id_orden","nom_orden","tipo","id_clase")

    def get_actions(self, request):
        actions = super(ordenesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_orden"),
    )
  
from .models import Ordenes
admin.site.register(Ordenes, ordenesAdmin)

#---guachamin

class familiasAdmin (admin.ModelAdmin):
    list_display = ("id_familia","nom_familia","tipo","id_orden","id_clase")

    def get_actions(self, request):
        actions = super(familiasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_familia"),
    )
  
from .models import Familias
admin.site.register(Familias, familiasAdmin)

class abundanciasAdmin (admin.ModelAdmin):
    list_display = ("id_abundancia","tax_abundancia","num_abundancia","ran_abundancia","id_familia")
    
    def get_actions(self, request):
        actions = super(abundanciasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    #search_fields = (
      #  ("tax_abundancia"),
    #)
  
from .models import Abundancias
admin.site.register(Abundancias, abundanciasAdmin)

class pisos_zeogeograficosAdmin (admin.ModelAdmin):
    list_display = ("id_pisozeogeografico","nom_pisozeogeografico","sigla_pisozeogeografico")

    def get_actions(self, request):
        actions = super(pisos_zeogeograficosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_pisozeogeografico"),
    )
  
from .models import PisosZeogeograficos
admin.site.register(PisosZeogeograficos, pisos_zeogeograficosAdmin)

class provinciasAdmin (admin.ModelAdmin):
    list_display = ("id_provincia","nom_provincia")

    def get_actions(self, request):
        actions = super(provinciasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import Provincias
admin.site.register(Provincias, provinciasAdmin)

class biomasAdmin (admin.ModelAdmin):
    list_display = ("id_bioma","nom_bioma","sigla_bioma","des_altitudinal_bioma","has_altitudinal_bioma",
    "remanencia","ext_bioma","id_provincia")
    
    def get_actions(self, request):
        actions = super(biomasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_bioma"),
    )
  
from .models import Biomas
admin.site.register(Biomas, biomasAdmin)

class ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id_ecosistema","nom_ecosistema","cod_ecosistema","id_pisozeogeografico","id_bioma")
    
    def get_actions(self, request):
        actions = super(ecosistemasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_ecosistema"),
    )
  
from .models import Ecosistemas
admin.site.register(Ecosistemas, ecosistemasAdmin)

class abundancias_ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id","id_ecosistema","id_abundancia")

    def get_actions(self, request):
        actions = super(abundancias_ecosistemasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_ecosistema"),
    )
  
from .models import AbundanciasEcosistemas
admin.site.register(AbundanciasEcosistemas, abundancias_ecosistemasAdmin)

class unidades_hidrograficasAdmin (admin.ModelAdmin):
    list_display = ("id_uh","nom_uh","cod_uh","riqueza_uh","abundancia_uh")
    
    def get_actions(self, request):
        actions = super(unidades_hidrograficasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_uh"),
    )
  
from .models import UnidadesHidrograficas
admin.site.register(UnidadesHidrograficas, unidades_hidrograficasAdmin)

class abundancias_uhAdmin (admin.ModelAdmin):
    list_display = ("id","id_abundancia","id_uh")

    def get_actions(self, request):
        actions = super(abundancias_uhAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_abundancia"),
    )
  
from .models import AbundanciasUh
admin.site.register(AbundanciasUh, abundancias_uhAdmin)

class actividadesAdmin (admin.ModelAdmin):
    list_display = ("id_actividad","nom_actividad","sigla_actividad")
    
    def get_actions(self, request):
        actions = super(actividadesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_actividad"),
    )
  
from .models import Actividades
admin.site.register(Actividades, actividadesAdmin)

class riosAdmin (admin.ModelAdmin):
    list_display = ("id_rio","nom_rio","categoria")
    
    def get_actions(self, request):
        actions = super(riosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_rio"),
    )
  
from .models import Rios
admin.site.register(Rios, riosAdmin)

class bosquesAdmin (admin.ModelAdmin):
    list_display = ("id_bosque","nom_bosque","pro_administrador_bosque","localizacion_area","micro_cuencas",
    "reg_oficial_bosque","hec_bosque","vegetacion_remanente","altitud_max","altitud_min")

    def get_actions(self, request):
        actions = super(bosquesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_bosque"),
    )
  
from .models import Bosques
admin.site.register(Bosques, bosquesAdmin)

'''''
class bosques_riosAdmin (admin.ModelAdmin):
    list_display = ("id_rio","id_bosque")
  
from .models import bosques_rios
admin.site.register(bosques_rios, bosques_riosAdmin)

class arbolesAdmin (admin.ModelAdmin):
    list_display = ("id_arbol","nom_arbol","esp_arbol","alt_arbol","tip_arbol","id_bosque")
  
from .models import arboles
admin.site.register(arboles, arbolesAdmin)

'''''

class areasAdmin (admin.ModelAdmin):
    list_display = ("id_area","cat_area","nom_area","fec_creacion","acu_resolucion_area","aut_competente_area",
     "superfici_area","tipo")

    def get_actions(self, request):
        actions = super(areasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_area"),
    )
  
from .models import Areas
admin.site.register(Areas, areasAdmin)

class areas_naturales_corredor_ecologAdmin (admin.ModelAdmin):
    list_display = ("id_area_corredor","asp_min_cap_inst","analisis","observaciones")
    
    def get_actions(self, request):
        actions = super(areas_naturales_corredor_ecologAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

from .models import AreasNaturalesCorredorEcolog
admin.site.register(AreasNaturalesCorredorEcolog, areas_naturales_corredor_ecologAdmin)

class cantonesAdmin (admin.ModelAdmin):
    list_display = ("id_canton","nom_canton","id_provincia")

    def get_actions(self, request):
        actions = super(cantonesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_canton"),
    )
  
from .models import Cantones
admin.site.register(Cantones, cantonesAdmin)

class biomas_cantonesAdmin (admin.ModelAdmin):
    list_display = ("id","id_bioma","id_canton")

    def get_actions(self, request):
        actions = super(biomas_cantonesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import BiomasCantones
admin.site.register(BiomasCantones, biomas_cantonesAdmin)

class biomas_ecosistemasAdmin (admin.ModelAdmin):
    list_display = ("id","id_bioma","id_ecosistema")

    def get_actions(self, request):
        actions = super(biomas_ecosistemasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import BiomasEcosistemas
admin.site.register(BiomasEcosistemas, biomas_ecosistemasAdmin)

class estado_conservacionAdmin (admin.ModelAdmin):
    list_display = ("id_estado_conservacion","categoria","sigla","descripcion")

    def get_actions(self, request):
        actions = super(estado_conservacionAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EstadoConservacion
admin.site.register(EstadoConservacion, estado_conservacionAdmin)


'''''
class clasificacionAdmin (admin.ModelAdmin):
    list_display = ("id_clasificacion","nom_clasificacion","id_estado_conservacion")

from .models import clasificacion
admin.site.register(clasificacion, clasificacionAdmin)

'''''

class distribucionesAdmin (admin.ModelAdmin):
    list_display = ("id_distribucion","nom_distribucion","sigla_distribucion")

    def get_actions(self, request):
        actions = super(distribucionesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_distribucion"),
    )
  
from .models import Distribuciones
admin.site.register(Distribuciones, distribucionesAdmin)

class nichotroficoAdmin (admin.ModelAdmin):
    list_display = ("id_nicho_trofico","nom_nicho","sigla_nicho","descripcion")

    def get_actions(self, request):
        actions = super(nichotroficoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_nicho"),
    )
  
from .models import Nichotrofico
admin.site.register(Nichotrofico, nichotroficoAdmin)

class personasAdmin (admin.ModelAdmin):
    list_display = ("id_persona","nom_persona","ape_persona","tipo")

    def get_actions(self, request):
        actions = super(personasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_persona"),
    )
  
from .models import Personas
admin.site.register(Personas, personasAdmin)


class migracion_avesAdmin (admin.ModelAdmin):
    list_display = ("id_migracion","nom_migracion","sigla")

    def get_actions(self, request):
        actions = super(migracion_avesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_migracion"),
    )
  
from .models import MigracionAves
admin.site.register(MigracionAves, migracion_avesAdmin)

class especiesAdmin (admin.ModelAdmin):
    list_display = ("id_especie","nom_especie","tipo","rango_altitudinal","ubicacion","descripcion","nom_cientifico",
    "nom_ingles","id_estado_conservacion","id_nicho_trofico","id_persona",'id_subfamilia',"id_familia","id_orden",
    "id_clase","anio_descubrimiento","id_migracion")

    def get_actions(self, request):
        actions = super(especiesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_especie"),
    )

    list_filter = (
        ("tipo"),
        ("id_estado_conservacion"),
        ("id_clase"),
    )
  
from .models import Especies
admin.site.register(Especies, especiesAdmin)

class canton_areaAdmin (admin.ModelAdmin):
    list_display = ("id","id_area","id_canton")

    def get_actions(self, request):
        actions = super(canton_areaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import CantonArea
admin.site.register(CantonArea, canton_areaAdmin)

class canton_bosqueAdmin (admin.ModelAdmin):
    list_display = ("id","id_bosque","id_canton")

    def get_actions(self, request):
        actions = super(canton_bosqueAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import CantonBosque
admin.site.register(CantonBosque, canton_bosqueAdmin)

class canton_ecosistemaAdmin (admin.ModelAdmin):
    list_display = ("id","id_canton","id_ecosistema")

    def get_actions(self, request):
        actions = super(canton_ecosistemaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import CantonEcosistema
admin.site.register(CantonEcosistema, canton_ecosistemaAdmin)



#--figueroa

class cantones_rios_Admin (admin.ModelAdmin):
    list_display = ("id","id_canton","id_rio")

    def get_actions(self, request):
        actions = super(cantones_rios_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import CantonesRios
admin.site.register(CantonesRios, cantones_rios_Admin)



class cantones_unidades_hidrograficas_Admin (admin.ModelAdmin):
    list_display = ("id","id_uh","id_canton","id_provincia")

    def get_actions(self, request):
        actions = super(cantones_unidades_hidrograficas_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import CantonesUnidadesHidrograficas
admin.site.register(CantonesUnidadesHidrograficas, cantones_unidades_hidrograficas_Admin)



class circuitos_integracion_biolog_Admin (admin.ModelAdmin):
    list_display = ("id_circuito","nombre_circuito","desc_circuito")

    def get_actions(self, request):
        actions = super(circuitos_integracion_biolog_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_circuito"),
    )
  
from .models import CircuitosIntegracionBiolog
admin.site.register(CircuitosIntegracionBiolog, circuitos_integracion_biolog_Admin)



class endemismos_Admin (admin.ModelAdmin):
    list_display = ("id_endemismo","nom_endemismo","sigla_endemismo")

    def get_actions(self, request):
        actions = super(endemismos_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_endemismo"),
    )
  
from .models import Endemismos
admin.site.register(Endemismos, endemismos_Admin)



class registros_Admin (admin.ModelAdmin):
    list_display = ("id_registro","nom_registro","literal")

    def get_actions(self, request):
        actions = super(registros_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_registro"),
    )
  
from .models import Registros
admin.site.register(Registros, registros_Admin)



class parroquias_Admin (admin.ModelAdmin):
    list_display = ("id_parroquia","nom_parroquia","id_canton","id_provincia")

    def get_actions(self, request):
        actions = super(parroquias_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_parroquia"),
    )
  
from .models import Parroquias
admin.site.register(Parroquias, parroquias_Admin)



class locaciones_Admin (admin.ModelAdmin):
    list_display = ("id_locacion","nom_locacion","sigla_locacion","alt_locacion",
    "id_parroquia","id_canton","id_provincia","coordenadas","id_bioma","latitud_locacion",
    "longitud_locacion")

    def get_actions(self, request):
        actions = super(locaciones_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_locacion"),
    )
  
from .models import Locaciones
admin.site.register(Locaciones, locaciones_Admin)



class estaciones_muestreos_Admin (admin.ModelAdmin):
    list_display = ("id_em","nom_em","nom_formal_em","cod_em","id_rio","ind_shannon_em")

    def get_actions(self, request):
        actions = super(estaciones_muestreos_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_em"),
    )
  
from .models import EstacionesMuestreos
admin.site.register(EstacionesMuestreos, estaciones_muestreos_Admin)



class localidades_muestreo_Admin (admin.ModelAdmin):
    list_display = ("id_muestreo","num_muestreo","nom_muestreo","des_muestreo","log_muestreo",
    "lat_muestreo", "alt_muestreo","tipo_animal_muestreo","id_em")

    def get_actions(self, request):
        actions = super(localidades_muestreo_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_muestreo"),
    )
  
from .models import LocalidadesMuestreo
admin.site.register(LocalidadesMuestreo, localidades_muestreo_Admin)



class especie_locaciones_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_locacion")

    def get_actions(self, request):
        actions = super(especie_locaciones_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspecieLocaciones
admin.site.register(EspecieLocaciones, especie_locaciones_Admin)



class especie_registros_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_registro")

    def get_actions(self, request):
        actions = super(especie_registros_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspecieRegistros
admin.site.register(EspecieRegistros, especie_registros_Admin)



class especies_actividades_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_actividad")

    def get_actions(self, request):
        actions = super(especies_actividades_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspeciesActividades
admin.site.register(EspeciesActividades, especies_actividades_Admin)



class especies_distribucion_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_distribucion")

    def get_actions(self, request):
        actions = super(especies_distribucion_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspeciesDistribucion
admin.site.register(EspeciesDistribucion, especies_distribucion_Admin)



class especies_localidades_muestreo_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_muestreo")

    def get_actions(self, request):
        actions = super(especies_localidades_muestreo_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspeciesLocalidadesMuestreo
admin.site.register(EspeciesLocalidadesMuestreo, especies_localidades_muestreo_Admin)



class tipos_vegetacion_Admin (admin.ModelAdmin):
    list_display = ("id_tipovegetacion","nom_tipovegetacion","sigla_tipovegetacion")
    
    def get_actions(self, request):
        actions = super(tipos_vegetacion_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_tipovegetacion"),
    )

from .models import TiposVegetacion
admin.site.register(TiposVegetacion, tipos_vegetacion_Admin)



class especies_tiposvegetacion_Admin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_tipovegetacion")

    def get_actions(self, request):
        actions = super(especies_tiposvegetacion_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import EspeciesTiposvegetacion
admin.site.register(EspeciesTiposvegetacion, especies_tiposvegetacion_Admin)



class flora_Admin (admin.ModelAdmin):
    list_display = ("id_flora","nom_flora","tipo_flora","etimologia_flora","diagnosis_flora",
    "comentarios_taxonomicos_flora","distribucion_composicion_flora","autor_flora")

    def get_actions(self, request):
        actions = super(flora_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_flora"),
    )
  
from .models import Flora
admin.site.register(Flora, flora_Admin)



class flora_biomas_Admin (admin.ModelAdmin):
    list_display = ("id","id_flora","id_bioma")

    def get_actions(self, request):
        actions = super(flora_biomas_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import FloraBiomas
admin.site.register(FloraBiomas, flora_biomas_Admin)


#--id_flora y uicn_cites tienen # en el modelo
class flora_endemica_amenazada_Admin (admin.ModelAdmin):
    list_display = ("id_flora","nombre_cientifico_endemica_amenaza","uicn_cites_endemica_amenaza")
    
    def get_actions(self, request):
        actions = super(flora_endemica_amenazada_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_cientifico_endemica_amenaza"),
    )

from .models import FloraEndemicaAmenazada
admin.site.register(FloraEndemicaAmenazada, flora_endemica_amenazada_Admin)



class flora_imagen_Admin (admin.ModelAdmin):
    list_display = ("id_flora_imagen","imagenflora","tipo_flora_imagen","autor_flora_imagen","id_flora")
    
    
    def get_actions(self, request):
        actions = super(flora_imagen_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions


    list_filter = (
        ("id_flora"),
    )



from .models import FloraImagen
admin.site.register(FloraImagen, flora_imagen_Admin)




class flora_locaciones_Admin (admin.ModelAdmin):
    list_display = ("id","id_flora","id_locacion")
    
    def get_actions(self, request):
        actions = super(flora_locaciones_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

from .models import FloraLocaciones
admin.site.register(FloraLocaciones, flora_locaciones_Admin)



class genero_Admin (admin.ModelAdmin):
    list_display = ("id_genero","nom_genero", "etimologia_genero","diagnosis_genero",
    "comentarios_taxonomico_genero","distribucion_composicion_genero")
    
    def get_actions(self, request):
        actions = super(genero_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_genero"),
    )

from .models import Genero
admin.site.register(Genero, genero_Admin)



class genero_flora_Admin (admin.ModelAdmin):
    list_display = ("id","id_flora","id_genero")

    def get_actions(self, request):
        actions = super(genero_flora_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions
  
from .models import GeneroFlora
admin.site.register(GeneroFlora, genero_flora_Admin)



class microcuencas_por_zonas_protecciAdmin (admin.ModelAdmin):
    list_display = ("id_microcuenca","nombre_microcuenca", "superficie_microcuenca","zona1_micro","zona2_micro",
    "zona3_micro","zona4_micro","zona5_micro","zona6_micro")
    
    def get_actions(self, request):
        actions = super(microcuencas_por_zonas_protecciAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_microcuenca"),
    )

from .models import MicrocuencasPorZonasProtecci
admin.site.register(MicrocuencasPorZonasProtecci, microcuencas_por_zonas_protecciAdmin)



class ordenes_biomas_Admin (admin.ModelAdmin):
    list_display = ("id","id_ordenes","id_biomas")
    
    def get_actions(self, request):
        actions = super(ordenes_biomas_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

from .models import OrdenesBiomas
admin.site.register(OrdenesBiomas, ordenes_biomas_Admin)



class ordenes_familias_Admin (admin.ModelAdmin):
    list_display = ("id","id_orden","id_familia","num_generos","num_especies","porcentaje")
    
    def get_actions(self, request):
        actions = super(ordenes_familias_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

from .models import OrdenesFamilias
admin.site.register(OrdenesFamilias, ordenes_familias_Admin)



class actividades_no_permitidas_zona_resAdmin (admin.ModelAdmin):
    list_display = ("id_zona_restauracion","actividades_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_no_permitidas_zona_resAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_permitidas"),
    )
  
from .models import ActividaNoPermitidaZonasRes
admin.site.register(ActividaNoPermitidaZonasRes, actividades_no_permitidas_zona_resAdmin)



class actividades_no_permitidad_macro_Admin (admin.ModelAdmin):
    list_display = ("id_zona_macrona","actividades_no_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_no_permitidad_macro_Admin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_no_permitidas"),
    )
  
from .models import ActividadesNoPermitidadMacro
admin.site.register(ActividadesNoPermitidadMacro, actividades_no_permitidad_macro_Admin)



class actividades_no_permitidas_zonaAdmin (admin.ModelAdmin):
    list_display = ("id_zona_prot_est","actividades_no_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_no_permitidas_zonaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_no_permitidas"),
    )
  
from .models import ActividadesNoPermitidasZona
admin.site.register(ActividadesNoPermitidasZona, actividades_no_permitidas_zonaAdmin)



class actividades_permitidad_macronaAdmin (admin.ModelAdmin):
    list_display = ("id_zona_macrona","actividades_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_permitidad_macronaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_permitidas"),
    )
  
from .models import ActividadesPermitidadMacrona
admin.site.register(ActividadesPermitidadMacrona, actividades_permitidad_macronaAdmin)



#--ricky

class actividades_permitidad_zonas_coAdmin (admin.ModelAdmin):
    list_display = ("id_zona_conservacion","actividades_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_permitidad_zonas_coAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    search_fields = (
        ("actividades_permitidas"),
    )
  
from .models import ActividadesPermitidadZonasCo
admin.site.register(ActividadesPermitidadZonasCo, actividades_permitidad_zonas_coAdmin)

class actividades_permitidad_zonas_prAdmin (admin.ModelAdmin):
    list_display = ("id_zona_prot_est","actividades_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_permitidad_zonas_prAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_permitidas"),
    )
  
from .models import ActividadesPermitidadZonasPr
admin.site.register(ActividadesPermitidadZonasPr, actividades_permitidad_zonas_prAdmin)

class actividades_permitidad_zonas_reAdmin (admin.ModelAdmin):
    list_display = ("id_zona_restauracion","actividades_permitidas")
    
    def get_actions(self, request):
        actions = super(actividades_permitidad_zonas_reAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("actividades_permitidas"),
    )
  
from .models import ActividadesPermitidadZonasRe
admin.site.register(ActividadesPermitidadZonasRe, actividades_permitidad_zonas_reAdmin)

class arbol_alimento_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_arbol","especie_arbol","mes_epoca")
    
    def get_actions(self, request):
        actions = super(arbol_alimento_pericosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("especie_arbol"),
    )
  
from .models import ArbolAlimentoPericos
admin.site.register(ArbolAlimentoPericos, arbol_alimento_pericosAdmin)

class area_naturales_conservacionAdmin (admin.ModelAdmin):
    list_display = ("id_areanatural","nombre_area","desc_area")
    
    def get_actions(self, request):
        actions = super(area_naturales_conservacionAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_area"),
    )
  
from .models import AreasNaturalesConservacion
admin.site.register(AreasNaturalesConservacion, area_naturales_conservacionAdmin)

class area_vegetalAdmin (admin.ModelAdmin):
    list_display = ("id","id_areanatural","covertura_vegetal","hectareas","porcentaje")

    def get_actions(self, request):
        actions = super(area_vegetalAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("covertura_vegetal"),
    )
  
from .models import AreaVegetal
admin.site.register(AreaVegetal, area_vegetalAdmin)

class geologiasAdmin (admin.ModelAdmin):
    list_display = ("id_geologia","nom_geologia")
    
    def get_actions(self, request):
        actions = super(geologiasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_geologia"),
    )
  
from .models import Geologias
admin.site.register(Geologias, geologiasAdmin)

class geomorfologiaAdmin (admin.ModelAdmin):
    list_display = ("id_geomorfologia","nom_geomorfologia")
    
    def get_actions(self, request):
        actions = super(geomorfologiaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_geomorfologia"),
    )
  
from .models import Geomorfologia
admin.site.register(Geomorfologia, geomorfologiaAdmin)

class areanatural_geologiaAdmin (admin.ModelAdmin):
    list_display = ("id","id_areanatural","id_geologia","hec_geologia","porcentaje")
    
    def get_actions(self, request):
        actions = super(areanatural_geologiaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_geologia"),
    )
  
from .models import AreanaturalGeologia
admin.site.register(AreanaturalGeologia, areanatural_geologiaAdmin)

class areanatural_geomorfologiaAdmin (admin.ModelAdmin):
    list_display = ("id","id_areanatural","id_geomorfologia","hec_geologia","porcentaje")
    
    def get_actions(self, request):
        actions = super(areanatural_geomorfologiaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_geomorfologia"),
    )

from .models import AreanaturalGeomorfologia
admin.site.register(AreanaturalGeomorfologia, areanatural_geomorfologiaAdmin)

class areanatural_locacionAdmin (admin.ModelAdmin):
    list_display = ("id","id_areanatural","id_canton","id_parroquia","km_cuadrados","porcentaje")
    
    def get_actions(self, request):
        actions = super(areanatural_locacionAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_canton"),
    )
  
from .models import AreanaturalLocacion
admin.site.register(AreanaturalLocacion, areanatural_locacionAdmin)

class suelosAdmin (admin.ModelAdmin):
    list_display = ("id_suelos","nom_suelos")
    
    def get_actions(self, request):
        actions = super(suelosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_suelos"),
    )
    list_filter = (
        ("nom_suelos"),
    )
  
from .models import Suelos
admin.site.register(Suelos, suelosAdmin)

class areanatural_sueloAdmin (admin.ModelAdmin):
    list_display = ("id","id_suelos","id_areanatural","hec_geologia","porcentaje")

    def get_actions(self, request):
        actions = super(areanatural_sueloAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_suelos"),
    )

    
  
from .models import AreanaturalSuelo
admin.site.register(AreanaturalSuelo, areanatural_sueloAdmin)

class ben_corredores_ecologicosAdmin (admin.ModelAdmin):
    list_display = ("id_beneficio","nombre_beneficio","descripcion_beneficio")
    
    def get_actions(self, request):
        actions = super(ben_corredores_ecologicosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_beneficio"),
    )
  
from .models import BenCorredoresEcologicos
admin.site.register(BenCorredoresEcologicos, ben_corredores_ecologicosAdmin)

class biomas_especiesAdmin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_bioma")
    
    def get_actions(self, request):
        actions = super(biomas_especiesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    list_filter = (
        ("id_bioma"),
    )
  
from .models import BiomasEspecies
admin.site.register(BiomasEspecies, biomas_especiesAdmin)

class gremio_alimentarioAdmin (admin.ModelAdmin):
    list_display = ("id_gremio_alimentario","nom_gremio_alimentario","sigla_gremio_alimentario")
    
    def get_actions(self, request):
        actions = super(gremio_alimentarioAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_gremio_alimentario"),
    )
  
from .models import GremioAlimentario
admin.site.register(GremioAlimentario, gremio_alimentarioAdmin)

class especie_gremioalimentarioAdmin (admin.ModelAdmin):
    list_display = ("id","id_especie","id_gremio_alimentario")
    
    def get_actions(self, request):
        actions = super(especie_gremioalimentarioAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_gremio_alimentario"),
    )
  
from .models import EspecieGremioalimentario
admin.site.register(EspecieGremioalimentario, especie_gremioalimentarioAdmin)

class estado_conservacion_cuerpos_aguAdmin (admin.ModelAdmin):
    list_display = ("id_rio","codigo","bmwp_col","calidad_agua")
    
    def get_actions(self, request):
        actions = super(estado_conservacion_cuerpos_aguAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    list_filter = (
        ("codigo"),
    )
  
from .models import EstadoConservacionCuerposAgu
admin.site.register(EstadoConservacionCuerposAgu, estado_conservacion_cuerpos_aguAdmin)

class estudios_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_estudioperico","id_provincia","localidad_especie",
    "numero_pericos_especie","grupo_especie","anio_estudio")

    def get_actions(self, request):
        actions = super(estudios_pericosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_provincia"),
    )

  
from .models import EstudiosPericos
admin.site.register(EstudiosPericos, estudios_pericosAdmin)

class fisiotopicoAdmin (admin.ModelAdmin):
    list_display = ("id_fisiotopico","nombre_fisiotopico","descripcion","recomendacion_y_uso")
    
    def get_actions(self, request):
        actions = super(fisiotopicoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    search_fields = (
        ("nombre_fisiotopico"),
    )
    list_filter = (
        ("nombre_fisiotopico"),
    )
  
from .models import Fisiotopico
admin.site.register(Fisiotopico, fisiotopicoAdmin)

class imagenesAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","imagen","tipo_imagen","autor_imagen","id_especie")
    
    def get_actions(self, request):
        actions = super(imagenesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("tipo_imagen"),
    )

    list_filter = (
        ("tipo_imagen"),
        ("id_especie"),
    )
  
from .models import Imagenes
admin.site.register(Imagenes, imagenesAdmin)

class imagenes_abundanciaAdmin (admin.ModelAdmin):
    list_display = ("id_imagen","imagen_abundancia","id_abundancia")
    
    def get_actions(self, request):
        actions = super(imagenes_abundanciaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_abundancia"),
    )
  
from .models import ImagenesAbundancia
admin.site.register(ImagenesAbundancia, imagenes_abundanciaAdmin)

class infraordenesAdmin (admin.ModelAdmin):
    list_display = ("id_infraorden","nom_infraorden","id_clase")
    
    def get_actions(self, request):
        actions = super(infraordenesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    search_fields = (
        ("nom_infraorden"),
    )

    list_filter = (
        ("id_clase"),
    )
  
from .models import Infraordenes
admin.site.register(Infraordenes, infraordenesAdmin)

class linea_corredores_ecologicosAdmin (admin.ModelAdmin):
    list_display = ("id_linea","nom_linea_corredores_ecologicos","descripcion_linea_corredores_ecologicos")
    
    def get_actions(self, request):
        actions = super(linea_corredores_ecologicosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    search_fields = (
        ("nom_linea_corredores_ecologicos"),
    )

    list_filter = (
        ("nom_linea_corredores_ecologicos"),
    )
  
from .models import LineaCorredoresEcologicos
admin.site.register(LineaCorredoresEcologicos, linea_corredores_ecologicosAdmin)

class paisajesAdmin (admin.ModelAdmin):
    list_display = ("id_paisaje","nom_paisaje")
    
    def get_actions(self, request):
        actions = super(paisajesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_paisaje"),
    )
  
from .models import Paisajes
admin.site.register(Paisajes, paisajesAdmin)

class parroquias_riosAdmin (admin.ModelAdmin):
    list_display = ("id","id_rio","id_parroquia","id_canton","id_provincia")

    def get_actions(self, request):
        actions = super(parroquias_riosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_parroquia"),
    )

from .models import ParroquiasRios
admin.site.register(ParroquiasRios, parroquias_riosAdmin)

class imagenes_biomasAdmin (admin.ModelAdmin):
    list_display = ("id_imagenbioma","id_bioma","url_imagen","autor")

    def get_actions(self, request):
        actions = super(imagenes_biomasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("autor"),
    )
  
from .models import ImagenesBiomas
admin.site.register(ImagenesBiomas, imagenes_biomasAdmin)


class regiones_naturalezAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nombre_zona")
    
    def get_actions(self, request):
        actions = super(regiones_naturalezAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_zona"),
    )
  
from .models import RegionesNaturalez
admin.site.register(RegionesNaturalez, regiones_naturalezAdmin)

class relievesAdmin (admin.ModelAdmin):
    list_display = ("id_relieve","ubicacion_relieve","longitud_min","longitud_max","territorio_relieve")

    def get_actions(self, request):
        actions = super(relievesAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("ubicacion_relieve"),
    )
  
from .models import Relieves
admin.site.register(Relieves, relievesAdmin)

class servicios_ecosistemicosAdmin (admin.ModelAdmin):
    list_display = ("id_servicioecosistemico","nom_servicioecosistemico",
    "hec_servicioecosistemico","por_servicioecosistemico")
    
    def get_actions(self, request):
        actions = super(servicios_ecosistemicosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_servicioecosistemico"),
    )
  
from .models import ServiciosEcosistemicos
admin.site.register(ServiciosEcosistemicos, servicios_ecosistemicosAdmin)

class sitios_muestreo_bioecologiaAdmin (admin.ModelAdmin):
    list_display = ("id_sitio","id_canton","id_locacion","bioma","coordenadas")
    
    def get_actions(self, request):
        actions = super(sitios_muestreo_bioecologiaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_canton"),
    )
  
from .models import SitiosMuestreoBioecologia
admin.site.register(SitiosMuestreoBioecologia, sitios_muestreo_bioecologiaAdmin)

class subfamiliasAdmin (admin.ModelAdmin):
    list_display = ("id_subfamilia","nom_subfamilia","tipo","id_familia")
    
    def get_actions(self, request):
        actions = super(subfamiliasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_subfamilia"),
    )

    list_filter = (
        ("tipo"),
    )
  
from .models import Subfamilias
admin.site.register(Subfamilias, subfamiliasAdmin)

class tribuAdmin (admin.ModelAdmin):
    list_display = ("id_tribu","nom_tribu","id_subfamilia")
    
    def get_actions(self, request):
        actions = super(tribuAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
    
    search_fields = (
        ("nom_tribu"),
    )

    list_filter = (
        ("id_subfamilia"),
    )
  
from .models import Tribu
admin.site.register(Tribu, tribuAdmin)

class subtribuAdmin (admin.ModelAdmin):
    list_display = ("id_subtribu","nom_subtribu","id_tribu")
    
    def get_actions(self, request):
        actions = super(subtribuAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nom_subtribu"),
    )

    list_filter = (
        ("id_tribu"),
    )
  
from .models import Subtribu
admin.site.register(Subtribu, subtribuAdmin)

class telemetria_pericosAdmin (admin.ModelAdmin):
    list_display = ("id_telemetria","num_pericos","cant_telemetrica",
    "estado_grupo_perico","distancia_vuelo_max","distancia_vuelo_promedio",
    "tiempo_estancia_bosques_max","tiempo_estancia_bosques_pro","tiempo_estancia_pastos_max",
    "tiempo_estancia_pastos_pro","habitat_bosques","habitat_pasto_arbolado",
    "habitat_area_vida_semanal","habitat_area_vida_diaria")

    def get_actions(self, request):
        actions = super(telemetria_pericosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("estado_grupo_perico"),
    )
  
from .models import TelemetriaPericos
admin.site.register(TelemetriaPericos, telemetria_pericosAdmin)

#TiposVegetacion

class unidades_fisiotopicosAdmin (admin.ModelAdmin):
    list_display = ("id","id_areanatural","id_fisiotopico","hectareas","porcentaje")

    def get_actions(self, request):
        actions = super(unidades_fisiotopicosAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    list_filter = (
        ("id_areanatural"),
    )
  
from .models import UnidadesFisiotopicos
admin.site.register(UnidadesFisiotopicos, unidades_fisiotopicosAdmin)


#UnidadesHidrograficas

class usersAdmin (admin.ModelAdmin):
    list_display = ("id_user","email_user","image_user","password_user",
    "estado_user","create_at_user","modif_at_user")
    
    def get_actions(self, request):
        actions = super(usersAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

from .models import Users
admin.site.register(Users, usersAdmin)

class usuarios_appAdmin (admin.ModelAdmin):
    list_display = ("idusuario","username","email","password")
    
    def get_actions(self, request):
        actions = super(usuarios_appAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("username"),
    )

    list_filter = (
        ("username"),
    )
  
from .models import UsuariosApp
admin.site.register(UsuariosApp, usuarios_appAdmin)

class variables_climaticasAdmin (admin.ModelAdmin):
    list_display = ("id_variable","codigo","variable","porcentaje","importancia")
    
    def get_actions(self, request):
        actions = super(variables_climaticasAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("variable"),
    )
  
from .models import VariablesClimaticas
admin.site.register(VariablesClimaticas, variables_climaticasAdmin)

class zonas_corredor_ecologicoAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nombre_zona","hectarias_zona","porcentaje_zona")
    
    def get_actions(self, request):
        actions = super(zonas_corredor_ecologicoAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_zona"),
    )

    list_filter = (
        ("nombre_zona"),
    )
  
from .models import ZonasCorredorEcologico
admin.site.register(ZonasCorredorEcologico, zonas_corredor_ecologicoAdmin)

class zonas_vidaAdmin (admin.ModelAdmin):
    list_display = ("id_zona","nombre_zona")
    
    def get_actions(self, request):
        actions = super(zonas_vidaAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    search_fields = (
        ("nombre_zona"),
    )

    list_filter = (
        ("nombre_zona"),
    )
  
from .models import ZonasVida
admin.site.register(ZonasVida, zonas_vidaAdmin)

class zonificacion_microcuenca_rio_caAdmin (admin.ModelAdmin):
    list_display = ("id","id_macrozonas","nom_macrozonas","recomendacion_de_uso","hectara","porcentaje")
    
    def get_actions(self, request):
        actions = super(zonificacion_microcuenca_rio_caAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions
        
    search_fields = (
        ("nom_macrozonas"),
    )

    list_filter = (
        ("nom_macrozonas"),
    )
  
from .models import ZonificacionMicrocuencaRioCa
admin.site.register(ZonificacionMicrocuencaRioCa, zonificacion_microcuenca_rio_caAdmin)


