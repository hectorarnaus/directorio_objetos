from Utilidades import ProcesadorTexto
from configuracion import *
from Vista.elementos_web import *

class Vista_Provincia:
    def __init__(self, provincia,imagen):
        self.provincia=provincia
        self.imagen=imagen
    
    def crea_migas(self):
        res=(   
            '<!-- wp:html -->\n'
            f'<nav aria-label="Breadcrumb" class="breadcrumb">\n'
            '<ul>\n'
            '<li>\n'
            f'<a href="{dominio}/">Inicio</a>\n'
            '</li>\n'
            f'<li class="breadcrumb-separador">></li>\n'
            f'<li class="breadcrumb-destacado">{self.provincia.nombre}</li>\n'
            '</ul>\n'
            '</nav>\n'
            '<!-- /wp:html -->\n\n\n'
        )
        return res
    
    def crea_contenido_articulo_provincia(self):
        
        parrafos=ProcesadorTexto.extraer_parrafos(self.provincia.cuerpo)
        aux=ProcesadorTexto.dividir_parrafo(parrafos[0])
        primero=aux[0]
        segundo=aux[1]
        res=self.crea_migas()


        res+=(
            '<div class="bloque-intro-imagen">\n'
            f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{self.imagen.get_id()},"mediaType":"image"}} -->\n'
	        '\t\t<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile">\n'
	    	'\t\t\t<div class="wp-block-media-text__content">\n'
	    		f'\t\t\t\t<span class="badge-intro">{tipo_negocio}</span>\n'
                f'\t\t\t\t<h2>Directorio de {tipo_negocio} en la provincia de {self.provincia.nombre}</h2>'
                f'\t\t\t\t{ElementosWeb.crea_parrafo(primero)}\n'
                f'\t\t\t\t{ElementosWeb.crea_parrafo(segundo)}\n'
                f'{ElementosWeb.crea_bloque_anuncio_manual()}'
	    		'\t\t\t\t<a class="intro-cta" href="#empresas">Ver empresas destacadas</a>\n'
	    	'\t\t\t</div>\n'
	    	'\t\t\t<figure class="wp-block-media-text__media">\n'
	    		f'\t\t\t\t<img src="{self.imagen.get_url()}" alt="Vista de {self.provincia.nombre} para el directorio de {tipo_negocio}" class="{self.imagen.get_id()} size-full"/>\n'
	    	'\t\t\t</figure>\n'
	    '\t\t</div>\n'
	    '\t<!-- /wp:media-text -->\n'
        '</div>\n'
        )


        res+=(
            '<div class="bloque-parrafo-normal">\n'
            f'\t<h3>Ventajas estratégicas en la provincia de {self.provincia.nombre}</h3>\n'
        )
        for i in range(1,len(parrafos)-1)         :
            res+=f'\t\t{ElementosWeb.crea_parrafo(parrafos[i])}\n'
            i+=1
        res+="</div>\n"
        res+=(     
            '<a id="#empresas">'
            '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
            '\t<div class="wp-block-group">\n'
            '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
            f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las {tipo_negocio} de {self.provincia.nombre} ordenadas por nombre de municipio</h2>\n'
            '\t\t<!-- /wp:heading -->\n'
            f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["Provincia de {self.provincia.nombre}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
            '\t</div>\n'
            '\t<!-- /wp:group -->\n')
        return res