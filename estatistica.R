areas <- c(100, 150, 200, 250, 300)  # cria um vetor com áreas

cat("Áreas cadastradas:\n")  # escreve um título
print(areas)  # mostra o vetor

media <- mean(areas)  # calcula a média
desvio <- sd(areas)  # calcula o desvio padrão

cat("\nMédia das áreas:", media, "\n")  # mostra a média
cat("Desvio padrão das áreas:", desvio, "\n")  # mostra o desvio