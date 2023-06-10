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


# Cómo buscamos elementos dentro de nuestra sopa (nuestro código fuente de la página)

soup.find("h1")
soup.find("h1").get_text()

soup.find_all("h2")
soup.find_all("h2").get_text() # esto no funciona
soup.find_all("h2")[0].get_text()

# extraer todos los nombres de las librerías

elementos_h2 = soup.find_all("h2")

librerias = []
for elemento in elementos_h2:
    elemento = elemento.get_text()
    librerias.append(elemento)

print(librerias)

# extraigamos las descripciones

elementos_p = soup.find_all("p", class_ = "librerias")
len(elementos_p)
print(elementos_p)


descripciones = []
for elemento in elementos_p:
    elemento = elemento.get_text(strip = True)
    descripciones.append(elemento)

print(descripciones)

# probemos con los enlaces

soup.find("a").get("href")


elementos_a = soup.find_all("a")
len(elementos_a)

enlaces = []
for elemento in elementos_a:
    elemento = elemento.get("href")
    enlaces.append(elemento)

print(enlaces)