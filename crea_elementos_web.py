from ficheros_datos.constantes_configuracion import *
from Modelo.negocio import *



def crea_lista_direccion(direccion):
    res=('<!-- wp:shortcode -->\n'
        f'\t[su_list icon="icon: map-marker" icon_color="{color_contrast}"  indent="15" class="lista"]\n'
        '\t\t<ul style="margin:0;">\n'
        f'\t\t\t<li><strong>Dirección postal:</strong> {direccion}</li>\n'
        '\t\t</ul>'
        f'\t[/su_list]'
        '<!-- /wp:shortcode -->\n'
    )
    return res
def crea_lista_telefono(telefono):
    res=('<!-- wp:shortcode -->\n'
         f'\t[su_list icon="icon: phone" icon_color="{color_contrast}" indent="15" class="lista"]\n'
         '\t\t<ul style="margin:0;">\n'
        f'\t\t\t<li><strong>Teléfono:</strong> <a href="tel:{telefono}">{telefono}</a></li>\n'
        '\t\t</ul>\n'
        '\t[/su_list]\n'
        '<!-- /wp:shortcode -->\n'
    )
    return res
    
def crea_lista_web(web):
    if web!=None:
        res=('<!-- wp:shortcode -->\n'
            f'\t[su_list icon="icon: external-link" icon_color="{color_contrast}" indent="15" class="lista"]\n'
            '\t\t<ul style="margin:0;">\n'
            f'\t\t\t<li><strong>Sitio web:</strong> <a href="{web}">{web}</a></li>\n'
            '\t\t</ul>\n'
            '\t[/su_list]\n'
            '<!-- /wp:shortcode -->\n'
        )
        return res

def crea_botones_datos_contacto(telefono,web):
    if web!=None:
        res=(
            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="tel:{telefono}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]¡Llama ahora![/su_button]\n'
            '<!-- /wp:shortcode -->\n'

            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="{web}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]Visitar web[/su_button]\n'
            '<!-- /wp:shortcode -->\n'
        )
        
    else:
        res=(
            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="tel:{telefono}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]¡Llama ahora![/su_button]\n'
            '<!-- /wp:shortcode -->\n'

            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="{dominio}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]Visitar web[/su_button]\n'
            '<!-- /wp:shortcode -->\n'
        )
    return res


def crea_heading(texto,numero,alineacion="center"):
    if alineacion=="left":
        res=('<!-- wp:heading {"textAlign":"left"} -->\n'
            f'\t<h{numero} class="wp-block-heading has-text-align-left">{texto}</h{numero}>\n'
            '<!-- /wp:heading -->\n'
        )
    elif alineacion=="right":
        res=('<!-- wp:heading {"textAlign":"right"} -->\n'
            f'\t<h{numero} class="wp-block-heading has-text-align-right">{texto}</h{numero}>\n'
            '<!-- /wp:heading -->\n'
        )
    else:
        res=('<!-- wp:heading {"textAlign":"center"} -->\n'
            f'\t<h{numero} class="wp-block-heading has-text-align-center">{texto}</h{numero}>\n'
            '<!-- /wp:heading -->\n'
        )
    return res
def crea_lista_horario(horario):
    res=('<!-- wp:shortcode -->\n'
        f'\t[su_list icon="icon: clock-o" icon_color="{color_contrast}" indent="15" class="lista lista-horario"]\n{horario}\n'
            '\t[/su_list]\n'
        '<!-- /wp:shortcode -->\n'
    )
    return res

def crea_mapa(negocio):
    res=('<!-- wp:html -->\n'
        f'\t<div class="map-wraper">\n'
        f'\t\t<iframe src="{negocio.mapa}" width="600" height="450"  style="border:1px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
        f'\t</div>\n'
        '<!-- /wp:html -->\n'
    )
    return res

def crea_imagen(negocio):
    res=('<!-- wp:image {"sizeSlug":"large","align":"center","className":"is-style-default"} -->\n'
        f'\t<figure class="wp-block-image aligncenter size-large is-style-default"><img src="{negocio.imagen}" alt="{negocio.nombre}"></figure>\n'
        '<!-- /wp:image -->\n'
    )
    return res




def crea_reviews(negocio):
    res=('[su_row class="bloque-opiniones"]'
         '\t[su_column size="1/2" center="no" class=""]'
        '\t\t<!-- wp:shortcode -->'
        f'\t\t\t[site_reviews_summary   assigned_posts="post_id" id="rating-summary" hide="percentage,bar"]'
        '\t\t<!-- /wp:shortcode -->'        
        '\t</su_column>'
        '\t[su_column size="1/2" center="no" class=""]'
        '\t\t<!-- wp:shortcode -->'
        f'\t\t\t[site_reviews_form  assigned_posts="post_id" summary_id="rating-summary" hide="content,email,terms,title,name"]'
        '\t\t<!-- /wp:shortcode -->'
        '\t</su_column>'
        '</su_row>'
    )
    return res
def crea_contenedor(contenido):
    res=(
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group bloque-intro-imagen">'
        f'\t\t{contenido}'
        '</div>\n'
        '<!-- /wp:group -->\n\n'
    )
    return res

def crea_contenedor_contacto(contenido):
    res=(
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        f'\t<div class="wp-block-group focus-contacto" style="background-color: {color_base3}; border-radius:12px; padding:24px 20px; box-shadow:0 2px 8px rgba(15,23,42,0.06);">'
        f'\t\t{contenido}'
        '</div>\n'
        '<!-- /wp:group -->\n\n'
    )
    return res



def crea_bloque_contacto(negocio):
    res=(f'{crea_heading("Datos de contacto",2)}'    
        f'{crea_lista_direccion(negocio.direccion)}'
        f'{crea_lista_telefono(negocio.telefono)}'
    )
    if negocio.web!=None:
        res+=f'{crea_lista_web(negocio.web)}'

    res+=crea_bloque_anuncio_manual()
    res+=f'{crea_botones_datos_contacto(negocio.telefono,negocio.web)}'
    return crea_contenedor(res)

def crea_bloque_horario(negocio):
    res=f'{crea_heading("Horario",2)}'
    res+=f'{crea_lista_horario(negocio.obten_horario_lista_html())}'
    return crea_contenedor(res)

def crea_bloque_mapa(negocio):
    res=f'{crea_heading("Localización",2)}'
    res+=f'{crea_mapa(negocio)}'
    return crea_contenedor(res)

def crea_bloque_imagen(negocio):
    res=f'{crea_heading("Fotografía",2)}'
    res+=f'{crea_imagen(negocio)}'
    return crea_contenedor(res)

def crea_bloque_reviews(negocio):
    res=f'{crea_heading(f"¿Qué opinan los usuarios de {negocio.nombre}?",2)}'
    res+=f'{crea_parrafo("Aquí puedes leer las opiniones y valoraciones de otros usuarios que han visitado "+negocio.nombre+". Si has estado aquí, no dudes en dejar tu propia reseña más abajo para ayudar a otros usuarios a conocer mejor este negocio.")}'
    res+=f'{crea_reviews(negocio)}'
    return crea_contenedor(res)

def crea_bloque_descripcion_seo(negocio):
    res=f'{crea_heading("Información",2)}'
    res+=f'{crea_parrafo(negocio.descripcion_seo)}'
    return crea_contenedor(res)

def crea_bloque_otros_negocios(negocio):
    res=crea_heading(f'Todas las {tipo_negocio.lower()} en {negocio.ciudad}',2)
    res+=(
        '<!-- wp:dpt/display-post-types {"taxonomy":"category","terms":['
        f'"{sluguiza(negocio.ciudad)}"'
        '],"number":100,"orderBy":"title","order":"ASC","styles":"dpt-list2","styleSup":["title"],"imgAspect":"land1","textPosHor":"center"}\n'
        '/-->'
    
        )
    return crea_contenedor(res)

def crea_tagline(mensaje):
    res=('<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"16px"},"spacing":{"margin":{"top":"20px","bottom":"30px"}}}} -->'
        f'<p class="has-text-align-center" style="margin-top:20px;margin-bottom:30px;font-size:16px;color:{color_contrast2}">'
        f'{mensaje}'
        '</p>'
        '<!-- /wp:paragraph -->'
    )
    return res


def crea_migas_negocio(negocio):
    res=(
        '<!-- wp:html -->\n'
        f'\t<nav aria-label="Breadcrumb" class="breadcrumb">\n'
        '\t\t<ul>\n'
        '\t\t\t<li>\n'
        f'\t\t\t\t<a href="{dominio}/">Inicio</a>\n'
        '\t\t\t</li>\n'
        f'\t\t\t<li class="breadcrumb-separador">></li>\n'
        '\t\t\t<li>\n'
        f'\t\t\t\t<a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">Provincia de {negocio.provincia}</a>\n'
        '\t\t\t</li>\n'
        f'\t\t\t<li class="breadcrumb-separador">></li>\n'
        '\t\t\t<li>\n'
        f'\t\t\t\t<a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a>\n'
        '\t\t\t</li>\n'
        f'\t\t\t<li class="breadcrumb-separador">></li>\n'
        f'\t\t\t<li class="breadcrumb-destacado">{negocio.nombre}</li>\n'
        '\t\t</ul>\n'
        '\t</nav>\n'
        '<!-- /wp:html -->\n\n\n'
    )
    return res

def crea_migas_ciudad(ciudad,provincia):
    res=(
        '<!-- wp:html -->\n'
        f'\t<nav aria-label="Breadcrumb" class="breadcrumb">\n'
        '\t\t<ul>\n'
        '\t\t\t<li>\n'
        f'\t\t\t\t<a href="{dominio}/">Inicio</a>\n'
        '\t\t\t</li>\n'
        f'\t\t\t<li class="breadcrumb-separador">></li>\n'
        '\t\t\t<li>\n'
        f'\t\t\t\t<a href="{dominio}/{sluguiza("Provincia de "+provincia)}">Provincia de {provincia}</a>\n'
        '\t\t\t</li>\n'
        f'\t\t\t<li class="breadcrumb-separador">></li>\n'
        f'\t\t\t<li class="breadcrumb-destacado">{ciudad}</li>\n'
        '\t\t</ul>\n'
        '\t</nav>\n'
        '<!-- /wp:html -->\n\n\n'
    )
    return res



