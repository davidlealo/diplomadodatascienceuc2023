def desertores(df_anterior, df_posterior):
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
    return desertores