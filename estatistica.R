arquivo <- "dados_farmtech.csv"

if (!file.exists(arquivo)) {
  cat("Arquivo dados_farmtech.csv não encontrado.\n")
} else {

  dados <- read.csv(arquivo, stringsAsFactors = FALSE)

  if (nrow(dados) == 0) {
    cat("Não há registros cadastrados.\n")
  } else {

    areas <- dados$area

    cat("===== ESTATÍSTICA BÁSICA =====\n")
    cat("Quantidade de registros:", length(areas), "\n\n")

    cat("Áreas cadastradas:\n")
    print(areas)

    media <- mean(areas)
    minimo <- min(areas)
    maximo <- max(areas)

    cat("\nMédia das áreas:", media, "\n")

    if (length(areas) < 2) {
      cat("Desvio padrão das áreas: não disponível com apenas 1 registro.\n")
    } else {
      desvio <- sd(areas)
      cat("Desvio padrão das áreas:", desvio, "\n")
    }

    cat("Menor área:", minimo, "\n")
    cat("Maior área:", maximo, "\n")
  }
}