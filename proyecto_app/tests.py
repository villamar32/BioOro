from django.test import TestCase

from proyecto_app.models import Biomas, Imagenes
from proyecto_app.models import Especies
from proyecto_app.models import Familias , Ordenes , Subfamilias, Flora, EstadoConservacion

#from configuracion.wsgi import *



# Create your tests here.


# Para testear los filtros
#listar_biomas = bioma.objects.all()
#print(listar_biomas)

f = Biomas.objects.filter(sigla_bioma="BPCA")
print(f)


# Probando busqueda avanzada filtros

#busqueda = 
"""
# De referencia

def my_view(request):
    doctors = GP.objects.all()
    periods = get_time_periods() # however it is you do this...
    smallest_date = get_smallest_date(time_periods)
    largest_date = get_largest_date(time_periods)
    deaths = Death.objects.select_related(depth=1).filter(date__range=(smallest_date, largest_date))
    # build the results table with initial count of 0 to account for all doctors
    # {period: {doctor: count}}
    results = dict((period,{doctor: 0}) for doctor in doctors for period in periods) 
    for death in deaths:
        for period in time_periods: # I'm assuming this is a small range of values
            if death.date > period['start_date'] and death.date < period['end_date']:
                results[period][death.current_gp] += 1 # add a death to the count


"""
"""



print(consulta)


def consulta_general(request):
    biomas = Biomas.objects.all();
    clases = Clases.objects.all();
    familias = Familias.objects.all();
    estado_conservacion = objects.all();
    migracion_aves = objects.all();
    nichotrofico = objects.all();
    personas = objects.all();
    subfamilias = objects.all();
    estado_conservacion = objects.all();
    ordenes = objects.all();


    periods = get_time_periods() # however it is you do this...
    smallest_date = get_smallest_date(time_periods)
    largest_date = get_largest_date(time_periods)

    deaths = Death.objects.select_related(depth=1).filter(date__range=(smallest_date, largest_date))
    
    
    # build the results table with initial count of 0 to account for all doctors
    # {period: {doctor: count}}
    results = dict((period,{doctor: 0}) for doctor in doctors for period in periods) 
    for death in deaths:
        for period in time_periods: # I'm assuming this is a small range of values
            if death.date > period['start_date'] and death.date < period['end_date']:
                results[period][death.current_gp] += 1 # add a death to the count


"""
#lineas_factura = linea_factura.objects.select_related(‘factura’).select_relate(‘articulo’).filter(factura__no = 89)

#consulta = Especies.objects.select_related('clases', 'familias', 'estado_conservacion', 'migracion_aves','nichotrofico','personas','subfamilias','estado_conservacion','ordenes')
#consulta = Especies.objects.select_related('familias')

#consulta = Especies.objects.select_related('familias')
# print(consulta.query)

#consu = Especies.objects.filter(familias__nom_familia='Phyllostomidae')
#print(consu)
#print(consulta.Familias.nom_familia)
#for p in consulta:
#    print(p.Familias.nom_familia)

#consulta = Especies.objects.select_related('id_especie','id_estado_conservacion','id_nicho_trofico','id_persona','id_subfamilia','id_familia','id_orden','id_clase','id_migracion')
#consulta = Imagenes.objects.select_related('id_especie')


contar_flora = Flora.objects.filter().count()
print(contar_flora)

estado_conservacion = EstadoConservacion.objects.filter().order_by('categoria')
print(estado_conservacion)

#ordenes = Ordenes.objects.filter()
#for ord in ordenes:
#    print(ord.nom_orden)


#familias = Familias.objects.filter()
#subfamilia = Subfamilias.objects.filter()