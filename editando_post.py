from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from ficheros_datos.constantes_configuracion import *
import collections
import collections.abc

collections.Iterable = collections.abc.Iterable




client = Client(
    f"{dominio}//xmlrpc.php",
    'hector.arnaus@gmail.com',
    'bolo4o#Eresgay'
)

def es_provincia(post):
    return any(
        getattr(term, "taxonomy", "") == "category" and
        (
            getattr(term, "slug", "").strip().lower() == "provincia" or
            getattr(term, "name", "").strip().lower() == "provincia"
        )
        for term in getattr(post, "terms", [])
    )



def es_municipio(post):
    return any(
        getattr(term, "taxonomy", "") == "category" and
        (
            getattr(term, "slug", "").strip().lower() == "provincia-de" or
            getattr(term, "name", "").strip().lower() == "provincia-de"
        )
        for term in getattr(post, "terms", [])
    )
def obten_nombre_provincia(post):
    trozos=post.slug.split("-")
    res=""
    i=2
    while i<len(trozos):
        if trozos[i]!="de":
            trozos[i]=trozos[i].capitalize()
        res+=trozos[i]+" "
        i+=1
    return res.strip()



offset = 0
total=0
increment = 200
while True:
        lista_posts = client.call(posts.GetPosts({'number': increment, 'offset': offset}))
        print(len(lista_posts))
        if len(lista_posts) == 0:
                break  # no more posts returned
        for post in lista_posts:
                #print(post.slug)
                if es_provincia(post):
                    print(obten_nombre_provincia(post))
                    #post.excerpt = f"¿Buscas alquiler de maquinaria en la provincia de {provincia}? Descubre empresas locales y tipos de maquinaria para tu obra cerca de ti."
                total += 1
                offset = offset + increment


 



'''

post = client.call(posts.GetPost(post_id))
#

term=(post.terms)

#provincia -> Provincia
#provincia-de -> Localidad
#slug pueblo ->Negocio

categorias = [
    term for term in getattr(post, "terms", [])
    if getattr(term, "taxonomy", "") == "category"
]

for cat in categorias:
    print(cat.id, cat.name, cat.slug)

client.call(posts.EditPost(post_id, post))
'''