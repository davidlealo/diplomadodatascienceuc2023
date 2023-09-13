library(datasets) 
# ajuste del modelo 
fm1 <- aov(breaks ~ wool + tension,            
           data = warpbreaks) 
# información del modelo 
summary(fm1) 
# comparacion de media de a pares 
TukeyHSD(fm1, "tension", ordered = TRUE) 
plot(TukeyHSD(fm1, "tension"))

install.packages("yarr")
library(yarr) 
library(ggplot2)
diamonds.lm <- lm(formula = price ~ depth + carat + color,                  
                  data = diamonds) 
summary(diamonds.lm)

# obtenemos los coeficientes 
diamonds.lm$coefficients 
# obtenemos los valores que ajustó el modelo 
diamonds.lm$fitted.values 
# obtenemos los residuos del modelo 
diamonds.lm$residuals 
# obtenemos el r2 
summary(diamonds.lm)$r.squared

install.packages("ggformula")
library(ggformula)
res <- diamonds.lm$residuals
ggplot(NULL, aes(sample = res)) + stat_qq() + stat_qqline()

step(lm(price ~ 1,data = diamonds),
     direction = c("forward"))

hist(diamonds$price)

summary(diamonds.lm)
model = lm(price ~ 1,data = diamonds)
summary(model)


