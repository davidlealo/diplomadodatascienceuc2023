# Taller de web scraping con Python
# Diplomado en Ciencia de Datos UC
# Sesión a cargo de Riva Quiroga (https://rivaquiroga.cl)

# Ejercicio 2

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Pasos iniciales
sitio = "http://programminghistorian.org/es/lecciones/"
respuesta = requests.get(sitio)
contenido = respuesta.text
soup = BeautifulSoup(contenido, "html.parser")

# Extraer los datos que nos interesan

# probar qué pasa si trato de extraer las etiquetas que identificamos

elementos_h2 = soup.find_all("h2", class_ = "title")
len(elementos_h2)
elementos_h2[0].get_text()
elementos_h2[58].get_text()

todos_los_enlaces = soup.find_all("a")
len(todos_los_enlaces)

for enlace in todos_los_enlaces:
    print(enlace.get("href"))

# Lo anterior nos devolvía más información de la que queríamos. Por lo tanto vamos a hacer un "recorte": vamos a extraer los datos de el div con la clase "lesson-description" y ahí dentro buscar lo que nos interesa

lista_lecciones = soup.find_all("div", class_ = "lesson-description")
len(lista_lecciones)

lista_lecciones[41]

# titulo
lista_lecciones[41].h2.get_text()

# autores
lista_lecciones[41].h3.get_text(strip = True)

# enlace
lista_lecciones[41].a.get("href")

# descripcion
lista_lecciones[41].p.get_text(strip = True)

# date
lista_lecciones[41].find("span", class_ = "date").get_text()

# topics

lista_lecciones[41].find("span", class_ = "topics").get_text()
lista_lecciones[2].find("span", class_ = "topics").get_text().split()


# Ahora que ya exploramos la página, hagamos la extracción:

titulos = []
topicos = []
enlaces = []

for leccion in lista_lecciones:
    # extremos el título y lo guardamos en la lista títulos
    titulo = leccion.h2.get_text(strip = True)
    titulos.append(titulo)

    # extraemos los tópicos y los guardamos en la lista tópicos
    topico = leccion.find("span", class_ = "topics").get_text().split()
    topicos.append(topico)

    # extrer y guardar los enlaces
    enlace = leccion.a.get("href")
    enlaces.append(f"http://programminghistorian.org{enlace}")


# creamos un diccionario

tutoriales_ph = {"titulo": titulos, "topicos": topicos, "enlace": enlaces}

df_tutoriales_ph = pd.DataFrame(tutoriales_ph)

df_tutoriales_ph.head()
df_tutoriales_ph.info()

df_tutoriales_ph.to_csv("datos-extraidos/tutoriales_ph.csv", index = False)