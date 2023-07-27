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

# 5. Genere una nueva variable que clasifique 
# la cantidad de habitaciones según tabla
# 2 o menos  = pocas_hab
# 3 a 5 (incluidos) = varias_hab
# 6 o más = muchas_hab

pocas_hab <- df %>% 
  mutate(pocas_hab = case_when(N_Habitaciones < 2 ~ "Pocas Habitaciones",
                               TRUE ~ FALSE)) %>% 
  arrange(pocas_hab)

print(pocas_hab)

varias_hab <- df %>%
  mutate(varias_hab = case_when(
    N_Habitaciones >= 3 & N_Habitaciones <= 5 ~ "Varias Habitaciones",
    TRUE ~ FALSE
  )) %>%
  arrange(varias_hab)

print(varias_hab)