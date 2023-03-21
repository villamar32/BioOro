# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import db
from django.db.models.base import ModelState



class Abundancias(models.Model):
    id_abundancia = models.AutoField(primary_key=True, editable=False)
    tax_abundancia = models.TextField(blank=True, null=True)
    num_abundancia = models.FloatField(blank=True, null=True)
    ran_abundancia = models.TextField(blank=True, null=True)
    id_familia = models.ForeignKey('Familias', models.DO_NOTHING, db_column='id_familia', blank=True, null=True)

    def __str__(self):
        return self.tax_abundancia

    class Meta:
        managed = False
        db_table = 'abundancias'


class AbundanciasEcosistemas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_ecosistema = models.ForeignKey('Ecosistemas', models.DO_NOTHING, db_column='id_ecosistema', blank=True, null=True)
    id_abundancia = models.ForeignKey(Abundancias, models.DO_NOTHING, db_column='id_abundancia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abundancias_ecosistemas'


class AbundanciasUh(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_abundancia = models.ForeignKey(Abundancias, models.DO_NOTHING, db_column='id_abundancia', blank=True, null=True)
    id_uh = models.ForeignKey('UnidadesHidrograficas', models.DO_NOTHING, db_column='id_uh', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abundancias_uh'


class ActividaNoPermitidaZonasRes(models.Model):
    id_zona_restauracion = models.IntegerField(primary_key=True, editable=False)
    actividades_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activida_no_permitida_zonas_res'


class Actividades(models.Model):
    id_actividad = models.IntegerField(primary_key=True, editable=False)
    nom_actividad = models.CharField(max_length=100, blank=True, null=True)
    sigla_actividad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_actividad

    class Meta:
        managed = False
        db_table = 'actividades'


class ActividadesNoPermitidadMacro(models.Model):
    id_zona_macrona = models.IntegerField(primary_key=True, editable=False)
    actividades_no_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_no_permitidad_macro'


class ActividadesNoPermitidasZona(models.Model):
    id_zona_prot_est = models.IntegerField(primary_key=True, editable=False)
    actividades_no_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_no_permitidas_zona'


class ActividadesPermitidadMacrona(models.Model):
    id_zona_macrona = models.IntegerField(primary_key=True, editable=False)
    actividades_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_permitidad_macrona_'


class ActividadesPermitidadZonasCo(models.Model):
    id_zona_conservacion = models.IntegerField(primary_key=True, editable=False)
    actividades_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_permitidad_zonas_co'


class ActividadesPermitidadZonasPr(models.Model):
    id_zona_prot_est = models.IntegerField(primary_key=True, editable=False)
    actividades_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_permitidad_zonas_pr'


class ActividadesPermitidadZonasRe(models.Model):
    id_zona_restauracion = models.IntegerField(primary_key=True, editable=False)
    actividades_permitidas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actividades_permitidad_zonas_re'


class ArbolAlimentoPericos(models.Model):
    id_arbol = models.IntegerField(primary_key=True, editable=False)
    especie_arbol = models.TextField(blank=True, null=True)
    mes_epoca = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.especie_arbol

    class Meta:
        managed = False
        db_table = 'arbol_alimento_pericos'


class AreaVegetal(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_areanatural = models.ForeignKey('AreasNaturalesConservacion', models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    covertura_vegetal = models.TextField(blank=True, null=True)
    hectareas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area_vegetal'


class AreanaturalGeologia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_areanatural = models.ForeignKey('AreasNaturalesConservacion', models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    id_geologia = models.ForeignKey('Geologias', models.DO_NOTHING, db_column='id_geologia', blank=True, null=True)
    hec_geologia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'areanatural_geologia'


class AreanaturalGeomorfologia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_areanatural = models.ForeignKey('AreanaturalLocacion', models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    id_geomorfologia = models.ForeignKey('Geomorfologia', models.DO_NOTHING, db_column='id_geomorfologia', blank=True, null=True)
    hec_geologia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areanatural_geomorfologia'


class AreanaturalLocacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_areanatural = models.ForeignKey('AreasNaturalesConservacion', models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    id_canton = models.ForeignKey('Cantones', models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_parroquia = models.ForeignKey('Parroquias', models.DO_NOTHING, db_column='id_parroquia', blank=True, null=True)
    km_cuadrados = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areanatural_locacion'


class AreanaturalSuelo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_suelos = models.ForeignKey('Suelos', models.DO_NOTHING, db_column='id_suelos', blank=True, null=True)
    id_areanatural = models.ForeignKey('AreasNaturalesConservacion', models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    hec_geologia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areanatural_suelo'


class Areas(models.Model):
    id_area = models.IntegerField(primary_key=True, editable=False)
    cat_area = models.TextField(blank=True, null=True)
    nom_area = models.CharField(max_length=255, blank=True, null=True)
    fec_creacion = models.DateField(blank=True, null=True)
    acu_resolucion_area = models.TextField(blank=True, null=True)
    aut_competente_area = models.TextField(blank=True, null=True)
    superfici_area = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_area

    class Meta:
        managed = False
        db_table = 'areas'


class AreasNaturalesConservacion(models.Model):
    id_areanatural = models.IntegerField(primary_key=True, editable=False)
    nombre_area = models.TextField(blank=True, null=True)
    desc_area = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_area

    class Meta:
        managed = False
        db_table = 'areas_naturales_conservacion'


class AreasNaturalesCorredorEcolog(models.Model):
    id_area_corredor = models.IntegerField(primary_key=True, editable=False)
    asp_min_cap_inst = models.TextField(blank=True, null=True)
    analisis = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_naturales_corredor_ecolog'


class BenCorredoresEcologicos(models.Model):
    id_beneficio = models.IntegerField(primary_key=True, editable=False)
    nombre_beneficio = models.TextField(blank=True, null=True)
    descripcion_beneficio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_beneficio

    class Meta:
        managed = False
        db_table = 'ben_corredores_ecologicos'


class Biomas(models.Model):
    id_bioma = models.IntegerField(primary_key=True, editable=False)
    nom_bioma = models.CharField(max_length=100, blank=True, null=True)
    sigla_bioma = models.CharField(max_length=50, blank=True, null=True)
    des_altitudinal_bioma = models.FloatField(blank=True, null=True)
    has_altitudinal_bioma = models.FloatField(blank=True, null=True)
    remanencia = models.FloatField(blank=True, null=True)
    ext_bioma = models.FloatField(blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

   # def __str__(self):
       # return self.nom_bioma + " " + self.sigla_bioma

    def __str__(self):
        return self.nom_bioma
    
    class Meta:
        managed = False
        db_table = 'biomas'


class BiomasCantones(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma', blank=True, null=True)
    id_canton = models.ForeignKey('Cantones', models.DO_NOTHING, db_column='id_canton', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biomas_cantones'


class BiomasEcosistemas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma', blank=True, null=True)
    id_ecosistema = models.ForeignKey('Ecosistemas', models.DO_NOTHING, db_column='id_ecosistema', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biomas_ecosistemas'


class BiomasEspecies(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey('Especies', models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biomas_especies'


class Bosques(models.Model):
    id_bosque = models.IntegerField(primary_key=True, editable=False)
    nom_bosque = models.CharField(max_length=100, blank=True, null=True)
    pro_administrador_bosque = models.TextField(blank=True, null=True)
    localizacion_area = models.TextField(blank=True, null=True)
    micro_cuencas = models.TextField(blank=True, null=True)
    reg_oficial_bosque = models.TextField(blank=True, null=True)
    hec_bosque = models.FloatField(blank=True, null=True)
    vegetacion_remanente = models.FloatField(blank=True, null=True)
    altitud_max = models.FloatField(blank=True, null=True)
    altitud_min = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nom_bosque

    class Meta:
        managed = False
        db_table = 'bosques'


class CantonArea(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_area = models.ForeignKey(Areas, models.DO_NOTHING, db_column='id_area', blank=True, null=True)
    id_canton = models.ForeignKey('Cantones', models.DO_NOTHING, db_column='id_canton', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canton_area'


class CantonBosque(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_bosque = models.ForeignKey(Bosques, models.DO_NOTHING, db_column='id_bosque', blank=True, null=True)
    id_canton = models.ForeignKey('Cantones', models.DO_NOTHING, db_column='id_canton', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canton_bosque'


class CantonEcosistema(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_canton = models.ForeignKey('Cantones', models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_ecosistema = models.ForeignKey('Ecosistemas', models.DO_NOTHING, db_column='id_ecosistema', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canton_ecosistema'


class Cantones(models.Model):
    id_canton = models.IntegerField(primary_key=True, editable=False)
    nom_canton = models.CharField(max_length=100, blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    def __str__(self):
        return self.nom_canton

    class Meta:
        managed = False
        db_table = 'cantones'


class CantonesRios(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_rio = models.ForeignKey('Rios', models.DO_NOTHING, db_column='id_rio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantones_rios'


class CantonesUnidadesHidrograficas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_uh = models.ForeignKey('UnidadesHidrograficas', models.DO_NOTHING, db_column='id_uh', blank=True, null=True)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cantones_unidades_hidrograficas'


class CircuitosIntegracionBiolog(models.Model):
    id_circuito = models.AutoField(primary_key=True, editable=False)
    nombre_circuito = models.CharField(max_length=100, blank=True, null=True)
    desc_circuito = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_circuito

    class Meta:
        managed = False
        db_table = 'circuitos_integracion_biolog'


class Clases(models.Model):
    id_clase = models.IntegerField(primary_key=True, editable=False)
    nom_clase = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    abund_clase = models.CharField(max_length=100, blank=True, null=True)
    num_ord_clase = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nom_clase

    class Meta:
        managed = False
        db_table = 'clases'


class Distribuciones(models.Model):
    id_distribucion = models.IntegerField(primary_key=True, editable=False)
    nom_distribucion = models.CharField(max_length=200, blank=True, null=True)
    sigla_distribucion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_distribucion

    class Meta:
        managed = False
        db_table = 'distribuciones'


class Ecosistemas(models.Model):
    id_ecosistema = models.IntegerField(primary_key=True, editable=False)
    nom_ecosistema = models.CharField(max_length=250, blank=True, null=True)
    cod_ecosistema = models.CharField(max_length=100, blank=True, null=True)
    id_pisozeogeografico = models.ForeignKey('PisosZeogeograficos', models.DO_NOTHING, db_column='id_pisozeogeografico', blank=True, null=True)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma', blank=True, null=True)

    def __str__(self):
        return self.nom_ecosistema

    class Meta:
        managed = False
        db_table = 'ecosistemas'


class Endemismos(models.Model):
    id_endemismo = models.IntegerField(primary_key=True, editable=False)
    nom_endemismo = models.CharField(max_length=100, blank=True, null=True)
    sigla_endemismo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_endemismo
        
    class Meta:
        managed = False
        db_table = 'endemismos'


class EspecieGremioalimentario(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey('Especies', models.DO_NOTHING, db_column='id_especie')
    id_gremio_alimentario = models.ForeignKey('GremioAlimentario', models.DO_NOTHING, db_column='id_gremio_alimentario')

    class Meta:
        managed = False
        db_table = 'especie_gremioalimentario'


class EspecieLocaciones(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey('Especies', models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_locacion = models.ForeignKey('Locaciones', models.DO_NOTHING, db_column='id_locacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especie_locaciones'


class EspecieRegistros(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey('Especies', models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_registro = models.ForeignKey('Registros', models.DO_NOTHING, db_column='id_registro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especie_registros'



class Especies(models.Model):
    id_especie = models.IntegerField(primary_key=True, editable=False)
    nom_especie = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    rango_altitudinal = models.TextField(blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    nom_cientifico = models.CharField(max_length=100, blank=True, null=True)
    nom_ingles = models.CharField(max_length=100, blank=True, null=True)
    id_estado_conservacion = models.ForeignKey('EstadoConservacion', models.DO_NOTHING, db_column='id_estado_conservacion', blank=True, null=True)
    #nacional = models.ForeignKey('EstadoConservacion', models.DO_NOTHING, db_column='nacional', blank=True, null=True)
    id_nicho_trofico = models.ForeignKey('Nichotrofico', models.DO_NOTHING, db_column='id_nicho_trofico', blank=True, null=True)
    id_persona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='id_persona', blank=True, null=True)
    id_subfamilia = models.ForeignKey('Subfamilias', models.DO_NOTHING, db_column='id_subfamilia', blank=True, null=True)
    id_familia = models.ForeignKey('Familias', models.DO_NOTHING, db_column='id_familia', blank=True, null=True)
    id_orden = models.ForeignKey('Ordenes', models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    id_clase = models.ForeignKey(Clases, models.DO_NOTHING, db_column='id_clase', blank=True, null=True)
    anio_descubrimiento = models.IntegerField(blank=True, null=True)
    id_migracion = models.ForeignKey('MigracionAves', models.DO_NOTHING, db_column='id_migracion', blank=True, null=True)

    def __str__(self):
        return self.nom_especie

    class Meta:
        managed = False
        db_table = 'especies'
        ordering = ['nom_especie']


class EspeciesActividades(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_actividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='id_actividad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies_actividades'


class EspeciesDistribucion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_distribucion = models.ForeignKey(Distribuciones, models.DO_NOTHING, db_column='id_distribucion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies_distribucion'


class EspeciesLocalidadesMuestreo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_muestreo = models.ForeignKey('LocalidadesMuestreo', models.DO_NOTHING, db_column='id_muestreo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies_localidades_muestreo'


class EspeciesTiposvegetacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='id_especie', blank=True, null=True)
    id_tipovegetacion = models.ForeignKey('TiposVegetacion', models.DO_NOTHING, db_column='id_tipovegetacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especies_tiposvegetacion'


class EstacionesMuestreos(models.Model):
    id_em = models.IntegerField(primary_key=True, editable=False)
    nom_em = models.CharField(max_length=100, blank=True, null=True)
    nom_formal_em = models.CharField(max_length=255, blank=True, null=True)
    cod_em = models.CharField(max_length=100, blank=True, null=True)
    id_rio = models.ForeignKey('Rios', models.DO_NOTHING, db_column='id_rio', blank=True, null=True)
    ind_shannon_em = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nom_em

    class Meta:
        managed = False
        db_table = 'estaciones_muestreos'


class EstadoConservacion(models.Model):
    id_estado_conservacion = models.IntegerField(primary_key=True, editable=False)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.categoria

    class Meta:
        managed = False
        db_table = 'estado_conservacion'


class EstadoConservacionCuerposAgu(models.Model):
    id_rio = models.IntegerField(primary_key=True, editable=False)
    codigo = models.TextField(blank=True, null=True)
    bmwp_col = models.IntegerField(blank=True, null=True)
    calidad_agua = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado_conservacion_cuerpos_agu'


class EstudiosPericos(models.Model):
    id_estudioperico = models.IntegerField(primary_key=True, editable=False)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    localidad_especie = models.IntegerField(blank=True, null=True)
    numero_pericos_especie = models.IntegerField(blank=True, null=True)
    grupo_especie = models.IntegerField(blank=True, null=True)
    anio_estudio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudios_pericos'


class Familias(models.Model):
    id_familia = models.IntegerField(primary_key=True, editable=False)
    nom_familia = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    id_orden = models.ForeignKey('Ordenes', models.DO_NOTHING, db_column='id_orden', blank=True, null=True)
    id_clase = models.ForeignKey(Clases, models.DO_NOTHING, db_column='id_clase', blank=True, null=True)

    def __str__(self):
        return self.nom_familia
    
    class Meta:
        managed = False
        db_table = 'familias'
        ordering = ['nom_familia']


class Fisiotopico(models.Model):
    id_fisiotopico = models.IntegerField(primary_key=True, editable=False)
    nombre_fisiotopico = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    recomendacion_y_uso = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_fisiotopico
    
    class Meta:
        managed = False
        db_table = 'fisiotopico'
        ordering = ['nombre_fisiotopico']


class Flora(models.Model):
    id_flora = models.IntegerField(primary_key=True, editable=False)
    nom_flora = models.CharField(max_length=250, blank=True, null=True)
    tipo_flora = models.CharField(max_length=50, blank=True, null=True)
    etimologia_flora = models.TextField(blank=True, null=True)
    diagnosis_flora = models.TextField(blank=True, null=True)
    comentarios_taxonomicos_flora = models.TextField(blank=True, null=True)
    distribucion_composicion_flora = models.TextField(blank=True, null=True)
    autor_flora = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nom_flora
    
    class Meta:
        managed = False
        db_table = 'flora'
        ordering = ['nom_flora']


class FloraBiomas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_flora = models.ForeignKey(Flora, models.DO_NOTHING, db_column='id_flora')
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma')

    class Meta:
        managed = False
        db_table = 'flora_biomas'


class FloraEndemicaAmenazada(models.Model):
    id_flora = models.IntegerField(primary_key=True, editable=False)
    nombre_cientifico_endemica_amenaza = models.TextField(blank=True, null=True)
    uicn_cites_endemica_amenaza = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_cientifico_endemica_amenaza
    
    class Meta:
        managed = False
        db_table = 'flora_endemica_amenazada'


class FloraImagen(models.Model):
    id_flora_imagen = models.IntegerField(primary_key=True, editable=False)
    imagenflora = models.ImageField(upload_to='flora', null=True, blank=True)
    tipo_flora_imagen = models.CharField(max_length=100, blank=True, null=True)
    autor_flora_imagen = models.CharField(max_length=100, blank=True, null=True)
    id_flora = models.ForeignKey(Flora, models.DO_NOTHING, db_column='id_flora')

    #def __str__(self):
        #return self.tipo_flora_imagen

    
    class Meta:
        managed = False
        db_table = 'flora_imagen'


class FloraLocaciones(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_flora = models.ForeignKey(Flora, models.DO_NOTHING, db_column='id_flora')
    id_locacion = models.ForeignKey('Locaciones', models.DO_NOTHING, db_column='id_locacion')

    class Meta:
        managed = False
        db_table = 'flora_locaciones'


class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True, editable=False)
    nom_genero = models.CharField(max_length=45, blank=True, null=True)
    etimologia_genero = models.TextField(blank=True, null=True)
    diagnosis_genero = models.TextField(blank=True, null=True)
    comentarios_taxonomico_genero = models.TextField(blank=True, null=True)
    distribucion_composicion_genero = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_genero

    class Meta:
        managed = False
        db_table = 'genero'


class GeneroFlora(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_flora = models.ForeignKey(Flora, models.DO_NOTHING, db_column='id_flora')
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')

    class Meta:
        managed = False
        db_table = 'genero_flora'


class Geologias(models.Model):
    id_geologia = models.IntegerField(primary_key=True, editable=False)
    nom_geologia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_geologia
    
    class Meta:
        managed = False
        db_table = 'geologias'


class Geomorfologia(models.Model):
    id_geomorfologia = models.IntegerField(primary_key=True, editable=False)
    nom_geomorfologia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_geomorfologia
    
    class Meta:
        managed = False
        db_table = 'geomorfologia'


class GremioAlimentario(models.Model):
    id_gremio_alimentario = models.AutoField(primary_key=True, editable=False)
    nom_gremio_alimentario = models.CharField(max_length=200, blank=True, null=True)
    sigla_gremio_alimentario = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_gremio_alimentario

    class Meta:
        managed = False
        db_table = 'gremio_alimentario'


class Imagenes(models.Model):
    id_imagen = models.IntegerField(primary_key=True, editable=False)
    imagen = models.ImageField(upload_to='especies', null=True, blank=True)
    tipo_imagen = models.CharField(max_length=100, blank=True, null=True)
    autor_imagen = models.CharField(max_length=100, blank=True, null=True)
    id_especie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='id_especie')

    #def __str__(self):
        #return self.tipo_imagen
    
    class Meta:
        managed = False
        db_table = 'imagenes'


class ImagenesAbundancia(models.Model):
    
    id_imagen = models.AutoField(primary_key=True, editable=False)
    imagen_abundancia = models.ImageField(upload_to='abundancias', null=True, blank=True)
    id_abundancia = models.ForeignKey(Abundancias, models.DO_NOTHING, db_column='id_abundancia')

    class Meta:
        managed = False
        db_table = 'imagenes_abundancia'


class ImagenesBiomas(models.Model):
    id_imagenbioma = models.AutoField(primary_key=True, editable=False)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma')
    url_imagen = models.ImageField(upload_to='biomas', null=True, blank=True)
    autor = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'imagenes_biomas'


class Infraordenes(models.Model):
    id_infraorden = models.IntegerField(primary_key=True, editable=False)
    nom_infraorden = models.CharField(max_length=100, blank=True, null=True)
    id_clase = models.ForeignKey(Clases, models.DO_NOTHING, db_column='id_clase', blank=True, null=True)

    def __str__(self):
        return self.nom_infraorden
    
    class Meta:
        managed = False
        db_table = 'infraordenes'


class LineaCorredoresEcologicos(models.Model):
    id_linea = models.IntegerField(primary_key=True, editable=False)
    nom_linea_corredores_ecologicos = models.TextField(blank=True, null=True)
    descripcion_linea_corredores_ecologicos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_linea_corredores_ecologicos

    class Meta:
        managed = False
        db_table = 'linea_corredores_ecologicos'


class Locaciones(models.Model):
    id_locacion = models.IntegerField(primary_key=True, editable=False)
    nom_locacion = models.CharField(max_length=100, blank=True, null=True)
    sigla_locacion = models.CharField(max_length=50, blank=True, null=True)
    alt_locacion = models.FloatField(blank=True, null=True)
    id_parroquia = models.ForeignKey('Parroquias', models.DO_NOTHING, db_column='id_parroquia', blank=True, null=True)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)
    id_bioma = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_bioma', blank=True, null=True)
    latitud_locacion = models.FloatField(blank=True, null=True)
    longitud_locacion = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nom_locacion
    
    class Meta:
        managed = False
        db_table = 'locaciones'


class LocalidadesMuestreo(models.Model):
    id_muestreo = models.IntegerField(primary_key=True, editable=False)
    num_muestreo = models.FloatField(blank=True, null=True)
    nom_muestreo = models.CharField(max_length=200, blank=True, null=True)
    des_muestreo = models.TextField(blank=True, null=True)
    log_muestreo = models.FloatField(blank=True, null=True)
    lat_muestreo = models.FloatField(blank=True, null=True)
    alt_muestreo = models.FloatField(blank=True, null=True)
    tipo_animal_muestreo = models.CharField(max_length=100, blank=True, null=True)
    id_em = models.ForeignKey(EstacionesMuestreos, models.DO_NOTHING, db_column='id_em', blank=True, null=True)

    def __str__(self):
        return self.nom_muestreo

    class Meta:
        managed = False
        db_table = 'localidades_muestreo'


class MicrocuencasPorZonasProtecci(models.Model):
    id_microcuenca = models.AutoField(primary_key=True, editable=False)
    nombre_microcuenca = models.TextField(blank=True, null=True)
    superficie_microcuenca = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    zona1_micro = models.IntegerField(blank=True, null=True)
    zona2_micro = models.IntegerField(blank=True, null=True)
    zona3_micro = models.TextField(blank=True, null=True)
    zona4_micro = models.IntegerField(blank=True, null=True)
    zona5_micro = models.IntegerField(blank=True, null=True)
    zona6_micro = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_microcuenca
    
    class Meta:
        managed = False
        db_table = 'microcuencas_por_zonas_protecci'


class MigracionAves(models.Model):
    id_migracion = models.AutoField(primary_key=True, editable=False)
    nom_migracion = models.CharField(max_length=200, blank=True, null=True)
    sigla = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_migracion

    class Meta:
        managed = False
        db_table = 'migracion_aves'


class Nichotrofico(models.Model):
    id_nicho_trofico = models.IntegerField(primary_key=True, editable=False)
    nom_nicho = models.CharField(max_length=150, blank=True, null=True)
    sigla_nicho = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_nicho

    class Meta:
        managed = False
        db_table = 'nichotrofico'


class Ordenes(models.Model):
    id_orden = models.IntegerField(primary_key=True, editable=False)
    nom_orden = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    id_clase = models.ForeignKey(Clases, models.DO_NOTHING, db_column='id_clase', blank=True, null=True)

    def __str__(self):
        return self.nom_orden

    class Meta:
        managed = False
        db_table = 'ordenes'


class OrdenesBiomas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_ordenes = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_ordenes', blank=True, null=True)
    id_biomas = models.ForeignKey(Biomas, models.DO_NOTHING, db_column='id_biomas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenes_biomas'


class OrdenesFamilias(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_orden = models.ForeignKey(Ordenes, models.DO_NOTHING, db_column='id_orden')
    id_familia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='id_familia')
    num_generos = models.IntegerField(blank=True, null=True)
    num_especies = models.IntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ordenes_familias'


class Paisajes(models.Model):
    id_paisaje = models.IntegerField(primary_key=True, editable=False)
    nom_paisaje = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nom_paisaje
    
    class Meta:
        managed = False
        db_table = 'paisajes'


class Parroquias(models.Model):
    id_parroquia = models.IntegerField(primary_key=True, editable=False)
    nom_parroquia = models.CharField(max_length=200, blank=True, null=True)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    def __str__(self):
        return self.nom_parroquia
    
    class Meta:
        managed = False
        db_table = 'parroquias'


class ParroquiasRios(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_rio = models.ForeignKey('Rios', models.DO_NOTHING, db_column='id_rio', blank=True, null=True)
    id_parroquia = models.ForeignKey(Parroquias, models.DO_NOTHING, db_column='id_parroquia', blank=True, null=True)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='id_provincia', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parroquias_rios'


class Personas(models.Model):
    id_persona = models.IntegerField(primary_key=True, editable=False)
    nom_persona = models.CharField(max_length=255, blank=True, null=True)
    ape_persona = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.ape_persona
    
    class Meta:
        managed = False
        db_table = 'personas'


class PisosZeogeograficos(models.Model):
    id_pisozeogeografico = models.IntegerField(primary_key=True, editable=False)
    nom_pisozeogeografico = models.CharField(max_length=200, blank=True, null=True)
    sigla_pisozeogeografico = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_pisozeogeografico
    
    class Meta:
        managed = False
        db_table = 'pisos_zeogeograficos'


class Provincias(models.Model):
    id_provincia = models.IntegerField(primary_key=True, editable=False)
    nom_provincia = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nom_provincia

    class Meta:
        managed = False
        db_table = 'provincias'


class RegionesNaturalez(models.Model):
    id_zona = models.IntegerField(primary_key=True, editable=False)
    nombre_zona = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_zona
    
    class Meta:
        managed = False
        db_table = 'regiones_naturalez'


class Registros(models.Model):
    id_registro = models.IntegerField(primary_key=True, editable=False)
    nom_registro = models.CharField(max_length=100, blank=True, null=True)
    literal = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nom_registro
    
    class Meta:
        managed = False
        db_table = 'registros'


class Relieves(models.Model):
    id_relieve = models.IntegerField(primary_key=True, editable=False)
    ubicacion_relieve = models.TextField(blank=True, null=True)
    longitud_min = models.TextField(blank=True, null=True)
    longitud_max = models.TextField(blank=True, null=True)
    territorio_relieve = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relieves'


class Rios(models.Model):
    id_rio = models.IntegerField(primary_key=True, editable=False)
    nom_rio = models.CharField(max_length=100, blank=True, null=True)
    categoria = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_rio
    
    class Meta:
        managed = False
        db_table = 'rios'


class ServiciosEcosistemicos(models.Model):
    id_servicioecosistemico = models.IntegerField(primary_key=True, editable=False)
    nom_servicioecosistemico = models.TextField(blank=True, null=True)
    hec_servicioecosistemico = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    por_servicioecosistemico = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.nom_servicioecosistemico
    
    class Meta:
        managed = False
        db_table = 'servicios_ecosistemicos'


class SitiosMuestreoBioecologia(models.Model):
    id_sitio = models.IntegerField(primary_key=True, editable=False)
    id_canton = models.ForeignKey(Cantones, models.DO_NOTHING, db_column='id_canton', blank=True, null=True)
    id_locacion = models.ForeignKey(Locaciones, models.DO_NOTHING, db_column='id_locacion', blank=True, null=True)
    bioma = models.TextField(blank=True, null=True)
    coordenadas = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitios_muestreo_bioecologia'


class Subfamilias(models.Model):
    id_subfamilia = models.IntegerField(primary_key=True, editable=False)
    nom_subfamilia = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    id_familia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='id_familia', blank=True, null=True)

    def __str__(self):
        return self.nom_subfamilia

    class Meta:
        managed = False
        db_table = 'subfamilias'


class Subtribu(models.Model):
    id_subtribu = models.IntegerField(primary_key=True, editable=False)
    nom_subtribu = models.TextField(blank=True, null=True)
    id_tribu = models.ForeignKey('Tribu', models.DO_NOTHING, db_column='id_tribu', blank=True, null=True)

    def __str__(self):
        return self.nom_subtribu

    class Meta:
        managed = False
        db_table = 'subtribu'


class Suelos(models.Model):
    id_suelos = models.IntegerField(primary_key=True, editable=False)
    nom_suelos = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_suelos
    
    class Meta:
        managed = False
        db_table = 'suelos'


class TelemetriaPericos(models.Model):
    id_telemetria = models.IntegerField(primary_key=True, editable=False)
    num_pericos = models.IntegerField(blank=True, null=True)
    cant_telemetrica = models.IntegerField(blank=True, null=True)
    estado_grupo_perico = models.TextField(blank=True, null=True)
    distancia_vuelo_max = models.TextField(blank=True, null=True)
    distancia_vuelo_promedio = models.TextField(blank=True, null=True)
    tiempo_estancia_bosques_max = models.TextField(blank=True, null=True)
    tiempo_estancia_bosques_pro = models.TextField(blank=True, null=True)
    tiempo_estancia_pastos_max = models.TextField(blank=True, null=True)
    tiempo_estancia_pastos_pro = models.TextField(blank=True, null=True)
    habitat_bosques = models.TextField(blank=True, null=True)
    habitat_pasto_arbolado = models.TextField(blank=True, null=True)
    habitat_area_vida_semanal = models.TextField(blank=True, null=True)
    habitat_area_vida_diaria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telemetria_pericos'


class TiposVegetacion(models.Model):
    id_tipovegetacion = models.IntegerField(primary_key=True, editable=False)
    nom_tipovegetacion = models.CharField(max_length=100, blank=True, null=True)
    sigla_tipovegetacion = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nom_tipovegetacion
    
    class Meta:
        managed = False
        db_table = 'tipos_vegetacion'


class Tribu(models.Model):
    id_tribu = models.IntegerField(primary_key=True, editable=False)
    nom_tribu = models.TextField(blank=True, null=True)
    id_subfamilia = models.ForeignKey(Subfamilias, models.DO_NOTHING, db_column='id_subfamilia', blank=True, null=True)

    def __str__(self):
        return self.nom_tribu
    
    class Meta:
        managed = False
        db_table = 'tribu'


class UnidadesFisiotopicos(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_areanatural = models.ForeignKey(AreasNaturalesConservacion, models.DO_NOTHING, db_column='id_areanatural', blank=True, null=True)
    id_fisiotopico = models.ForeignKey(Fisiotopico, models.DO_NOTHING, db_column='id_fisiotopico', blank=True, null=True)
    hectareas = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidades_fisiotopicos'


class UnidadesHidrograficas(models.Model):
    id_uh = models.IntegerField(primary_key=True, editable=False)
    nom_uh = models.CharField(max_length=200, blank=True, null=True)
    cod_uh = models.IntegerField(blank=True, null=True)
    riqueza_uh = models.FloatField(blank=True, null=True)
    abundancia_uh = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nom_uh
    
    class Meta:
        managed = False
        db_table = 'unidades_hidrograficas'


class Users(models.Model):
    id_user = models.IntegerField(primary_key=True, editable=False)
    email_user = models.TextField(blank=True, null=True)
    image_user = models.TextField(blank=True, null=True)
    password_user = models.CharField(max_length=100, blank=True, null=True)
    estado_user = models.CharField(max_length=50, blank=True, null=True)
    create_at_user = models.DateTimeField(blank=True, null=True)
    modif_at_user = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UsuariosApp(models.Model):
    idusuario = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(unique=True, max_length=45)
    email = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    class Meta:
        managed = False
        db_table = 'usuarios_app'


class VariablesClimaticas(models.Model):
    id_variable = models.IntegerField(primary_key=True, editable=False)
    codigo = models.TextField(blank=True, null=True)
    variable = models.TextField(blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    importancia = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.codigo
    
    class Meta:
        managed = False
        db_table = 'variables_climaticas'


class ZonasCorredorEcologico(models.Model):
    id_zona = models.AutoField(primary_key=True, editable=False)
    nombre_zona = models.CharField(max_length=200, blank=True, null=True)
    hectarias_zona = models.FloatField(blank=True, null=True)
    porcentaje_zona = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nombre_zona
    
    class Meta:
        managed = False
        db_table = 'zonas_corredor_ecologico'


class ZonasVida(models.Model):
    id_zona = models.IntegerField(primary_key=True, editable=False)
    nombre_zona = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_zona

    class Meta:
        managed = False
        db_table = 'zonas_vida'


class ZonificacionMicrocuencaRioCa(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_macrozonas = models.ForeignKey(ZonasCorredorEcologico, models.DO_NOTHING, db_column='id_macrozonas', blank=True, null=True)
    nom_macrozonas = models.TextField(blank=True, null=True)
    recomendacion_de_uso = models.TextField(blank=True, null=True)
    hectara = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.nom_macrozonas

    class Meta:
        managed = False
        db_table = 'zonificacion_microcuenca_rio_ca'
