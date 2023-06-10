import requests
from bs4 import BeautifulSoup
import pandas as pd

# Pasos WS sitios estáticos
# Paso 1: de request usaré get para tomar la url del sitio a trabajar 
sitio = "https://rivaquiroga.github.io/taller-web-scraping-python-2023/ejercicio-1.html" #Guardar el sitio en una variable para hacer todo más fácil. No es un paso obligatorio
respuesta = requests.get(sitio) #guardamos en una variable 'respuesta' el código fuente extraído con get

print(respuesta)

# Paso 2: Crear una variable contenido para guardar la respuesta como texto solo el texto
contenido = respuesta.text

print(contenido)

# Paso 3: rear una "SOPA" usando el html parser. Paraque BeautifulSoup pueda comprender las etiquetas, atributos y valores html como corresponde 

soup = BeautifulSoup(contenido, 'html.parser')

print(soup)

# Buscar elementos en el texto

soup.find('h1') # Esto es para buscar etiquetas h1. En este caso nos devuelve el contenido y la etiqueta
print(soup.find('h1'))
print('Fin busqueda con etiqueta')
print('__________________________________')
print(' ')


# En caso de querer no imprimir la etiqueta: 
soup.find('h1').get_text()
print(soup.find('h1').get_text())

# Lo anterior funcionó porque hay una sola etiqueta h1, pero etiquetas h2 tenemos tres elementos. Por lo tanto, debemos usar find_all en vez de find
soup.find_all('h2')
soup.find_all('h2').get_text() # esto no funciona porque esto sirve en un elemento y no en un grupo. Por eso debemos iterar los elementos
soup.find_all('h2')[0].get_text()

# extraer todos los nombres de las librerías

elementos_h2 = soup.find_all('h2')

librerias = []
for elemento in elementos_h2:
    elemento = elemento.get_text()
    librerias.append(elemento)

print(librerias)

#  extraigamos las descripciones

elementos_p = soup.find_all('p', class_ = 'librerias')
len(elementos_p)
print(elementos_p)


descripciones = []
for elemento in elementos_p:
    elemento = elemento.get_text(strip = True)
    descripciones.append(elemento)

print(descripciones)

# probemos con los enlaces

soup.find('a').get('href')


elementos_a = soup.find_all('a')
len(elementos_a)

enlaces = []
for elemento in elementos_a:
    elemento = elemento.get('href')
    enlaces.append(elemento)

print(enlaces)