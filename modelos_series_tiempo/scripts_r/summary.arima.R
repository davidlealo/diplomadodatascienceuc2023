summary.arima <- function(fit, fixed = NULL){
if(is.null(fixed)){fixed = rep(NA, length(fit$coef))}	
z.value = fit$coef[is.na(fixed)]/sqrt(diag(fit$var.coef))
p.value = 2*(1-pnorm(abs(z.value)))
Tabla <- round(cbind(fit$coef[is.na(fixed)],sqrt(diag(fit$var.coef)), z.value, p.value),4)
colnames(Tabla) = c("Estimate", "Std. Error", "z value", "Pr(>|z|)")
Tabla
}