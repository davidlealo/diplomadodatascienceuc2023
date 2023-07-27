library(tidyverse)

library(readxl)
viviendasRM <- read_excel("viviendasRM.xlsx")
View(viviendasRM)

df = viviendasRM

# 1. Cambie el nombre de la variable Quien_Vende por Vendedor
df <- df %>%
  rename(Vendedor = Quien_Vende)

# 2. Ordene la base de datos según la cantidad de baños y 
# luego entregue la información de las primeras diez viviendas.
# Con glimpse(df) vi el nombre de todas las variables en la consola
df_ordenado_banos <- df %>%
  arrange(N_Banos)

primeras_diez_viviendas <- head(df_ordenado_banos, 10)

print(primeras_diez_viviendas)

# 3. Agrupe la base según la cantidad de estacionamientos 
# e indique la cantidad de viviendas para cada grupo
df_agrupado <- df %>%
  group_by(N_Estacionamientos) %>%
  summarize(Cantidad_Viviendas = n(), .groups = "drop")

print(df_agrupado)

# 4. Calcule la media de los valores en UF y en CLP usando dplyr

media_valores <- df %>%
  summarize(
    Media_Valor_UF = mean(Valor_UF, na.rm = TRUE),
    Media_Valor_CLP = mean(Valor_CLP, na.rm = TRUE)
  )

print(media_valores)

