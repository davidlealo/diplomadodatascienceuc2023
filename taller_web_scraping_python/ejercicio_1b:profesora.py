# Taller de web scraping con Python
# Diplomado en Ciencia de Datos UC
# Sesión a cargo de Riva Quiroga (https://rivaquiroga.cl)

# Ejercicio 1

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Paso 0: Guardar la url del sitio en una variable
sitio = "https://rivaquiroga.github.io/taller-web-scraping-python-2023/ejercicio-1.html"

# Paso 1: Hacer una "solicitud" a la página web para traer el código fuente
respuesta = requests.get(sitio)

# Paso 2: 
contenido = respuesta.text

print(contenido)

# Paso 3: crear la "sopa"

soup = BeautifulSoup(contenido, "html.parser")

print(soup)

# Paso 4: buscar los datos que nos interesan dentro del código fuente de la página

# La función find() nos permite encontrar el primer elemento que tenga una determinada etiqueta/clase. Nos devuelve todo el elemento html (o sea, las etiquetas y el contenido)

soup.find("h1")

# Para quedarnos solo con el texto, usamos el método get_text()
soup.find("h1").get_text()

# Si queremos encontrar todos los elementos que tengan una determinada etiqueta/clase, usamos el método find_all(). Eso nos devuelve una lista con todos esos elementos. 
soup.find_all("h2")

# No podemos utilizar get_text() con find_all() porque ese método funciona con cada elemento de forma individual, no con una lista:
# Tenemos que aplicarlo a cada elemento de forma individual.
soup.find_all("h2")[0].get_text()

# La opción más rápida sería iterar. Los pasos entonces, serían:

# primero, guardar en  una variable la lista con todos los elementos h2:
elementos_h2 = soup.find_all("h2")

# luego, iterar por los elementos de esa lista, aplicarles get_text() y guardar el texto en la lista librerías

librerias = []
for elemento in elementos_h2:
    elemento = elemento.get_text()
    librerias.append(elemento)

# ¡Listo!
print(librerias)

# Ahora, extraigamos las descripciones:
# Como hay varias cosas etiquetadas como "p", tenemos que especificar la clase para que nos devuelva solo las que nos interesan

elementos_p = soup.find_all("p", class_ = "librerias")

# siempre es útil chequear con len() si la cantidad de elementos es la que esperábamos
len(elementos_p) 
print(elementos_p)

# Y ahora iteramos. En este caso agregamos "strip = True" a get_text(). Con esta opción podemos eliminar espacios antes y después del texto que nos interesa.

descripciones = []
for elemento in elementos_p:
    elemento = elemento.get_text(strip = True)
    descripciones.append(elemento)

print(descripciones)

# Finalmente, extraemos los enlaces.
# En este caso no nos sirve get_text(), porque nos devuelve el texto al que está asociado el enlace, no el enlace propiamente tal
soup.find("a").get_text()

# Para obtener el enlace usamos get() e indicamos que queremos el "href". Esto es igual para todos los sitios web.
soup.find("a").get("href")

# Ahora, repetimos el proceso: guardamos todo en una lista y luego iteramos para guardar solo los enlaces en una lista nueva.

elementos_a = soup.find_all("a")
len(elementos_a)

enlaces = []
for elemento in elementos_a:
    elemento = elemento.get("href")
    enlaces.append(elemento)

print(enlaces)

# Guardar todo en un data frame

web_scraping = {"libreria": librerias, "descripcion": descripciones, "enlace": enlaces}
print(web_scraping)

df_librerias = pd.DataFrame(web_scraping)
print(df_librerias)
df_librerias.info()

# guardar el data frame

df_librerias.to_csv("datos-extraidos/librerias-web-scraping.csv", index=False)