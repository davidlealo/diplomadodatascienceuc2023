salida.arima = function(Y, fit, fixed = NULL){
print(summary(fit))
cat("","\n","")
r2 = cbind(1-var(Y-fit$fitted, na.rm = T)/var(Y, na.rm = T))
colnames(r2) = "Adjusted R-squared"
rownames(r2) = ""
cat("","\n","")
print(r2)
cat("","\n","")
print(summary.arima(fit, fixed = fixed))

M = cbind(ks.test(scale(fit$res+runif(length(fit$res),-1e-15,+1e-15)), "pnorm")$p.value,
lmtest::bptest(fit$res ~ time(fit$res))$p.value)
colnames(M) = c("Kolmogorov-Smirnov test", "Breusch-Pagan test")
rownames(M) = "p-value"
cat("\n","Residuals:","\n","")
print(M)


}


