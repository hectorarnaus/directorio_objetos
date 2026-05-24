from funciones_excel import *
from ficheros_datos.constantes_configuracion import *
import os
from funciones import *


lista_provincias=obten_lista_provincias(excel_empresas)
lista_municipios=obten_lista_municipios(excel_empresas)
lista_negocios=obten_lista_negocios(excel_empresas)

print(len(lista_provincias))
print(len(lista_municipios))
print(len(lista_negocios))
fichero = open("/home/hector/urls.txt","w")
lista_provincias_sluguizada=[]
lista_municipios_sluguizada=[]
lista_negocios_sluguizada=[]
for provincia in lista_provincias:
    lista_provincias_sluguizada.append(dominio+sluguiza(provincia)+"\n")

for municipio in lista_municipios:
    lista_municipios_sluguizada.append(dominio+sluguiza(municipio)+"\n")

for negocio in lista_negocios:
    lista_negocios_sluguizada.append(dominio+sluguiza(negocio.nombre)+"\n")

for provincia in lista_provincias_sluguizada:
    print(provincia)
fichero.writelines(lista_provincias_sluguizada)
fichero.writelines(lista_municipios_sluguizada)
fichero.writelines(lista_negocios_sluguizada)

fichero.close()