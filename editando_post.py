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
    if "municipio" in post.title.lower():
        return True
    else:        
        return False
    
def es_revision(post):
    if post.slug.endswith("-revision-v1"):
        return True
    else:
        return False
    
def es_imagen(post):
    if post.slug.endswith("-webp"):
        return True
    else:
        return False
    
def obten_nombre_provincia(post):
    return post.title.split("provincia de ")[1].strip()

    

def es_palabra_conexion(palabra):
    if palabra=="de" or palabra=="la" or palabra=="el" or palabra=="los" or palabra=="las" or palabra=="y" or palabra=="en" or palabra=="a" or palabra=="sa" or palabra=="del":
        return True
    else:
        return False

def obten_nombre_municipio(post):
    return post.title.split("municipio de ")[1].strip()
   

def obten_nombre_negocio(post):
    return post.title.strip()
   
    
'''
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
fichero = open("posts.txt", 'w')
post_id=7001
while post_id<10000:
    try:
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

        fichero.write(f"post: {post_id}\n")
        if es_imagen(post)==False and es_revision(post)==False:
            if es_provincia(post):
                print(" -> Provincia\n")
                post.excerpt = f"¿Buscas alquiler de maquinaria en la provincia de {obten_nombre_provincia(post)}? Descubre empresas locales y tipos de maquinaria para tu obra cerca de ti."
                client.call(posts.EditPost(post_id, post))
                      
            elif es_municipio(post):
                print(f"{post.id}-> Localidad\n")
                post.excerpt = f"¿Buscas alquiler de maquinaria en {obten_nombre_municipio(post)}? Descubre empresas locales y tipos de maquinaria para tu obra cerca de ti."
                
                client.call(posts.EditPost(post_id, post))    
            else:
                print(f"{post.id}-> Negocio\n")
                post.excerpt = f"Alquila maquinaria en {obten_nombre_negocio(post)}. ¡Consigue los mejores precios y la mejor calidad para tu obra!"
                client.call(posts.EditPost(post_id, post))
            
        
        
    except Exception as e:
        print(f"Error al obtener el post con ID {post_id}: {e}")
    #client.call(posts.EditPost(post_id, post))
    post_id+=1
    
fichero.close()