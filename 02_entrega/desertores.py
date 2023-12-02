
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def identificar_desertores_sistema_regular(df_anterior, df_posterior):
    # Filtrar los estudiantes que no son prebásica o de educación para adultos
    desertores = df_anterior[(~df_anterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes regulares sin prebasica y adultos año anterior",desertores.shape)


    # Filtrar los estudiantes que no asisten a 4to medio el año a analizar
    desertores = desertores[~((desertores['COD_GRADO'] == 4) & (df_anterior['COD_ENSE2'].isin([5, 7])))]
    # print("Desertores sin 4to medio año anterior", desertores.shape)

    # Filtrar a los estudiantes df_posterior que no están en 'COD_ENSE2' 1, 3, 4, 6 y 8
    df_posterior = df_posterior[(~df_posterior['COD_ENSE2'].isin([1, 3, 4, 6, 8]))]
    # print("Estudiantes sistema regular año posterior",df_posterior.shape)

    # Verificar si los estudiantes están presentes en el archivo actual
    desertores = desertores[~desertores['MRUN'].isin(df_posterior['MRUN'].unique())]
    # print("Desertores año a analizar", desertores.shape)
    
    # Estudiantes que se mantienen en el sistema regular
    estudiantes_regulares = df_posterior[df_posterior['MRUN'].isin(df_anterior['MRUN'].unique())]
    # print("Estudiantes regulares año a analizar", estudiantes_regulares.shape)


    # Devolver el resultado como DataFrame de Pandas
    # return desertores

    # Sexo DataFrame
    df_genero = pd.DataFrame()
    print('Sexo', df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    df_genero['Sexo'] = ['Sin información', 'Hombre', 'Mujer']
    df_genero['Cantidad A. Regulares'] = [((estudiantes_regulares['GEN_ALU'] == 0).sum()), 
                          ((estudiantes_regulares['GEN_ALU'] == 1).sum()), 
                          ((estudiantes_regulares['GEN_ALU'] == 2).sum())]
    df_genero['Porcentaje A. Regulares'] = [((estudiantes_regulares['GEN_ALU'] == 0).sum()) / len(estudiantes_regulares) * 100,
                            ((estudiantes_regulares['GEN_ALU'] == 1).sum()) / len(estudiantes_regulares) * 100,
                            ((estudiantes_regulares['GEN_ALU'] == 2).sum()) / len(estudiantes_regulares) * 100]
    df_genero['Cantidad A. Desertores'] = [((desertores['GEN_ALU'] == 0).sum()), 
                          ((desertores['GEN_ALU'] == 1).sum()), 
                          ((desertores['GEN_ALU'] == 2).sum())]
    df_genero['Porcentaje A. Desertores'] = [((desertores['GEN_ALU'] == 0).sum()) / len(desertores) * 100,
                            ((desertores['GEN_ALU'] == 1).sum()) / len(desertores) * 100,
                            ((desertores['GEN_ALU'] == 2).sum()) / len(desertores) * 100]
    
    display(df_genero)

    # Gráfico de torta sexo
    data_pie = estudiantes_regulares["GEN_ALU"].value_counts()
    print("Gráfico de torta: Sexo alumnos regulares",df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())

    # Definir etiquetas
    labels = ['Hombre' if index == 1 else 'Mujer' if index == 2 else 'Sin información' for index in data_pie.index]

    plt.pie(data_pie, labels = labels, autopct = lambda x: f"{x:0.2f}%")
    plt.show()

    data_pie = desertores["GEN_ALU"].value_counts()
    print("Gráfico de torta: Sexo alumnos desertores",df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())

    # Definir etiquetas
    labels = ['Hombre' if index == 1 else 'Mujer' if index == 2 else 'Sin información' for index in data_pie.index]

    plt.pie(data_pie, labels = labels, autopct = lambda x: f"{x:0.2f}%")
    plt.show()

    # Rural DataFrame
    df_rural = pd.DataFrame()
    print('Rural', df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    df_rural['RURAL_RBD'] = ['Urbano', 'Rural']
    df_rural['Cantidad A. Regulares'] = [((estudiantes_regulares['RURAL_RBD'] == 0).sum()), 
                          ((estudiantes_regulares['RURAL_RBD'] == 1).sum())] 
    df_rural['Porcentaje A. Regulares'] = [((estudiantes_regulares['RURAL_RBD'] == 0).sum()) / len(estudiantes_regulares) * 100,
                            ((estudiantes_regulares['RURAL_RBD'] == 1).sum()) / len(estudiantes_regulares) * 100]
    df_rural['Cantidad A. Desertores'] = [((desertores['RURAL_RBD'] == 0).sum()), 
                          ((desertores['RURAL_RBD'] == 1).sum())]
    df_rural['Porcentaje A. Desertores'] = [((desertores['RURAL_RBD'] == 0).sum()) / len(desertores) * 100,
                            ((desertores['RURAL_RBD'] == 1).sum()) / len(desertores) * 100]
    
    display(df_rural)

    # Gráfico de torta Rural
    data_pie = estudiantes_regulares["RURAL_RBD"].value_counts()
    print("Gráfico de torta: Ruralidad alumnos regulares",df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())

    # Definir etiquetas
    labels = ['Rural' if index == 1 else 'Urbano' for index in data_pie.index]

    plt.pie(data_pie, labels = labels, autopct = lambda x: f"{x:0.2f}%")
    plt.show()

    data_pie = desertores["RURAL_RBD"].value_counts()
    print("Gráfico de torta: Ruralidad alumnos desertores",df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())

    # Definir etiquetas
    labels = ['Rural' if index == 1 else 'Urbano' for index in data_pie.index]

    plt.pie(data_pie, labels = labels, autopct = lambda x: f"{x:0.2f}%")
    plt.show()

    # Dependencia DataFrame
    df_tipo_dependencia = pd.DataFrame()
    print('Dependencia', df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    df_tipo_dependencia['COD_DEPE'] = ['Municipal', 'Particular Subvencionado', 'Particular Pagado']
    df_tipo_dependencia['Cantidad A. Regulares'] = [((estudiantes_regulares['COD_DEPE'] == 1).sum()),
                            ((estudiantes_regulares['COD_DEPE'] == 2).sum()),
                            ((estudiantes_regulares['COD_DEPE'] == 3).sum())]
    df_tipo_dependencia['Porcentaje A. Regulares'] = [((estudiantes_regulares['COD_DEPE'] == 1).sum()) / len(estudiantes_regulares) * 100,
                            ((estudiantes_regulares['COD_DEPE'] == 2).sum()) / len(estudiantes_regulares) * 100,
                            ((estudiantes_regulares['COD_DEPE'] == 3).sum()) / len(estudiantes_regulares) * 100]
    df_tipo_dependencia['Cantidad A. Desertores'] = [((desertores['COD_DEPE'] == 1).sum()),
                            ((desertores['COD_DEPE'] == 2).sum()),
                            ((desertores['COD_DEPE'] == 3).sum())]
    df_tipo_dependencia['Porcentaje A. Desertores'] = [((desertores['COD_DEPE'] == 1).sum()) / len(desertores) * 100,
                            ((desertores['COD_DEPE'] == 2).sum()) / len(desertores) * 100,
                            ((desertores['COD_DEPE'] == 3).sum()) / len(desertores) * 100]
    
    display(df_tipo_dependencia)

    # Diccionario de categorías
    categorias = {
    1: 'Municipal',
    2: 'DAEM',
    3: 'Part. Sub.',
    4: 'P. P.',
    5: 'Adm. delegada',
    6: 'SLEP'
}

    # Colores
    colores = ['#A7C8F2', '#C9DFF2', '#594A1C', '#F2D377', '#BF895A', '#FFBB73']

    # Gráfico de alumnos regulares
    obs_categoria = estudiantes_regulares["COD_DEPE"].value_counts()
    print("Alumnos regulares:", df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    plt.bar(x = [categorias[i] for i in obs_categoria.index], height=obs_categoria, color=colores)
    plt.xlabel("Tipo de dependencia")
    plt.ylabel("Cantidad de estudiantes")
    plt.show()

    # Gráfico de alumnos desertores
    obs_categoria = desertores["COD_DEPE"].value_counts()
    print("Alumnos desertores:", df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    plt.bar(x = [categorias[i] for i in obs_categoria.index], height=obs_categoria, color=colores)
    plt.xlabel("Tipo de dependencia")
    plt.ylabel("Cantidad de estudiantes")
    plt.show()

    # Nuevo DataFrame Tipo de enseñanza agrupados
    df_ense = pd.DataFrame()
    print('Tipo de enseñanza agrupados', df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    df_ense['COD_ENSE2'] = ['Básica', 'Media CH', 'Media TP y Art']

    # Cálculo de las cantidades y porcentajes de alumnos regulares para cada tipo de enseñanza
    for ensenanza, nombre in zip([2, 5, 7], ['Básica', 'Media CH', 'Media TP y Art']):
        df_ense.loc[df_ense['COD_ENSE2'] == nombre, 'Cantidad A. Regulares'] = (estudiantes_regulares['COD_ENSE2'] == ensenanza).sum()
        df_ense.loc[df_ense['COD_ENSE2'] == nombre, 'Porcentaje A. Regulares'] = (estudiantes_regulares['COD_ENSE2'] == ensenanza).sum() / len(estudiantes_regulares) * 100

    # Cálculo de las cantidades y porcentajes de alumnos desertores para cada tipo de enseñanza
    for ensenanza, nombre in zip([2, 5, 7], ['Básica', 'Media CH', 'Media TP y Art']):
        df_ense.loc[df_ense['COD_ENSE2'] == nombre, 'Cantidad A. Desertores'] = (desertores['COD_ENSE2'] == ensenanza).sum()
        df_ense.loc[df_ense['COD_ENSE2'] == nombre, 'Porcentaje A. Desertores'] = (desertores['COD_ENSE2'] == ensenanza).sum() / len(desertores) * 100

    display(df_ense)

    # Diccionario de categorías enseñanza
    categorias_ense = {
        2: 'Básica',
        5: 'Media CH',
        7: 'Media TP y Artística'
    }

    # Colores
    colores = ['#A7C8F2', '#C9DFF2', '#594A1C']

    # Gráfico de alumnos regulares
    print("Alumnos regulares:", df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    plt.bar(x = df_ense['COD_ENSE2'], height=df_ense['Cantidad A. Regulares'], color=colores, tick_label=df_ense['COD_ENSE2'].replace(categorias_ense))
    plt.xlabel("Tipo de enseñanza")
    plt.ylabel("Cantidad de estudiantes")
    plt.show()

    # Gráfico de alumnos desertores
    print("Alumnos desertores:", df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())
    plt.bar(x = df_ense['COD_ENSE2'], height=df_ense['Cantidad A. Desertores'], color=colores, tick_label=df_ense['COD_ENSE2'].replace(categorias_ense))
    plt.xlabel("Tipo de enseñanza")
    plt.ylabel("Cantidad de estudiantes")
    plt.show()

    print('Estudiantes Educación Básica', df_anterior['AGNO'].unique(),"-", df_posterior['AGNO'].unique())

    # Filtrar estudiantes de educación básica en ambos DataFrames
    regulares_basica = estudiantes_regulares[(estudiantes_regulares['COD_ENSE2'] == 2) & (estudiantes_regulares['COD_GRADO'].between(1, 8))]
    desertores_basica = desertores[(desertores['COD_ENSE2'] == 2) & (desertores['COD_GRADO'].between(1, 8))]

    # Crear un diccionario para mapear los códigos de grado a sus nombres correspondientes
    grados = {
        1: '1º',
        2: '2º',
        3: '3º',
        4: '4º',
        5: '5º',
        6: '6º',
        7: '7º',
        8: '8º'
    }

    # Inicializar un DataFrame vacío
    df_basica = pd.DataFrame()

    # Recorrer cada grado
    for i in range(1, 9):
        # Filtrar estudiantes y desertores de cada grado
        estudiantes_basica_grado = regulares_basica[regulares_basica['COD_GRADO'] == i]
        desertores_basica_grado = desertores_basica[desertores_basica['COD_GRADO'] == i]

        # Crear un DataFrame temporal para este grado
        df_temp = pd.DataFrame()
        df_temp['COD_ENSE2'] = ['Básica ' + grados[i]]
        df_temp['Cantidad A. Regulares'] = [len(estudiantes_basica_grado)] 
        df_temp['Porcentaje A. Regulares'] = [len(estudiantes_basica_grado) / len(estudiantes_regulares) * 100 if len(estudiantes_regulares) > 0 else 0]
        df_temp['Cantidad A. Desertores'] = [len(desertores_basica_grado)]
        df_temp['Porcentaje A. Desertores'] = [len(desertores_basica_grado) / len(desertores) * 100 if len(desertores) > 0 else 0]

        # Agregar el DataFrame temporal al DataFrame final
        df_basica = pd.concat([df_basica, df_temp], ignore_index=True)

    display(df_basica)

    # Colores
    colores = ['#A7C8F2', '#C9DFF2', '#594A1C', '#F2D377', '#BF895A', '#FFBB73', '#F28500', '#F20056']

    # Gráfico de estudiantes regulares
    plt.figure(figsize=(10, 6))
    plt.bar(x = df_basica['COD_ENSE2'], height=df_basica['Cantidad A. Regulares'], color=colores)
    plt.xlabel("Grado")
    plt.ylabel("Cantidad de estudiantes regulares")
    plt.title("Estudiantes regulares en educación básica")
    plt.show()

    # Gráfico de desertores
    plt.figure(figsize=(10, 6))
    plt.bar(x = df_basica['COD_ENSE2'], height=df_basica['Cantidad A. Desertores'], color=colores)
    plt.xlabel("Grado")
    plt.ylabel("Cantidad de desertores")
    plt.title("Desertores en educación básica")
    plt.show()

    # Filtrar estudiantes de educación media en ambos DataFrames
    regulares_media = estudiantes_regulares[(estudiantes_regulares['COD_ENSE2'].isin([5, 7])) & (estudiantes_regulares['COD_GRADO'].between(1, 4))]
    desertores_media = desertores[(desertores['COD_ENSE2'].isin([5,7])) & (desertores['COD_GRADO'].between(1, 4))]


    # Crear un diccionario para mapear los códigos de grado a sus nombres correspondientes
    grados = {
        1: '1º',
        2: '2º',
        3: '3º',
        4: '4º'
    }

    # Inicializar un DataFrame vacío
    df_media = pd.DataFrame()

     # Recorrer cada grado
    for i in range(1, 5):
        # Filtrar estudiantes y desertores de cada grado
        estudiantes_media_grado = regulares_media[regulares_media['COD_GRADO'] == i]
        desertores_mediaa_grado = desertores_media[desertores_media['COD_GRADO'] == i]

        # Crear un DataFrame temporal para este grado
        df_temp = pd.DataFrame()
        df_temp['COD_ENSE2'] = ['Medio ' + grados[i]]
        df_temp['Cantidad A. Regulares'] = [len(estudiantes_media_grado)] 
        df_temp['Porcentaje A. Regulares'] = [len(estudiantes_media_grado) / len(estudiantes_regulares) * 100 if len(estudiantes_regulares) > 0 else 0]
        df_temp['Cantidad A. Desertores'] = [len(desertores_mediaa_grado)]
        df_temp['Porcentaje A. Desertores'] = [len(desertores_mediaa_grado) / len(desertores) * 100 if len(desertores) > 0 else 0]

        # Agregar el DataFrame temporal al DataFrame final
        df_media = pd.concat([df_media, df_temp], ignore_index=True)

    display(df_media)


    # Crear una lista con los grados
    grados = df_media['COD_ENSE2']

    # Crear una lista con las cantidades de alumnos regulares y desertores
    regulares = df_media['Cantidad A. Regulares']
    desertores = df_media['Cantidad A. Desertores']

    # Definir la ubicación de las etiquetas del eje x
    x = np.arange(len(grados))

    # Crear los gráficos de barras
    plt.figure(figsize=(10,6))
    bar1 = plt.bar(x - 0.2, regulares, 0.4, color='#594A1C', label='Regulares')
    bar2 = plt.bar(x + 0.2, desertores, 0.4, color='#a7c8f2', label='Desertores')

    # Colocar las etiquetas del eje x
    plt.xticks(x, grados)

    # Colocar la leyenda
    plt.legend()

    # Colocar las etiquetas en las barras
    for bar in bar1:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval,
                int(yval), va='bottom')

    for bar in bar2:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval,
                int(yval), va='bottom')

    # Colocar los títulos y etiquetas de los ejes
    plt.title('Cantidad de Estudiantes Regulares y Desertores por Nivel de Educación Media')
    plt.xlabel('Nivel de Educación Media')
    plt.ylabel('Cantidad de Estudiantes')

    # Mostrar el gráfico
    plt.show()
