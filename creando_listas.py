
from controlador import *
from editando_post import obten_nombre_provincia
from ficheros_datos.constantes_configuracion import *

c=Controlador(excel_empresas,excel_municipios,excel_provincias)
c.connect()
provincias=c.crea_lista_provincias()
municipios=c.crea_lista_municipios()
empresas=c.crea_lista_empresas()
for provincia in provincias:
    for municipio in municipios:
        if municipio.provincia==provincia.nombre:
            provincia.anyade_municipio(municipio)

for municipio in municipios:
    for empresa in empresas:
        if empresa.municipio==municipio.nombre:
            municipio.anyade_empresa(empresa)

lista_imagenes=c.crea_lista_imagenes_municipio(os.getcwd()+("/municipio"))
lista_municipios_sin_imagen=c.crea_lista_municipios_sin_imagen(municipios,lista_imagenes)
if len(lista_municipios_sin_imagen)>0:
    print("Los siguientes municipios no tienen imagen:")
    for municipio in lista_municipios_sin_imagen:
        print(municipio)
else:
    print("Todos los municipios tienen imagen")
    for provincia in provincias:
        print("Creando el artículo de la provincia de "+provincia.nombre)
        c.crea_articulo_provincia(provincia)