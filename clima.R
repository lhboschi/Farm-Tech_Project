args <- commandArgs(trailingOnly = TRUE)

cidade <- "Campinas"

if (length(args) > 0) {
  cidade <- args[1]
}

user_lib <- Sys.getenv("R_LIBS_USER")

if (user_lib == "") {
  user_lib <- "C:/Users/lhbos/Documents/R/win-library/4.5"
}

dir.create(user_lib, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(user_lib, .libPaths()))

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  install.packages("jsonlite", repos = "https://cloud.r-project.org", lib = user_lib)
}

library(jsonlite, lib.loc = user_lib)

cat("===== CONSULTA METEOROLÓGICA =====\n")
cat("Cidade pesquisada:", cidade, "\n\n")

url_geo <- paste0(
  "https://geocoding-api.open-meteo.com/v1/search?name=",
  URLencode(cidade),
  "&count=1&language=pt&format=json"
)

geo <- fromJSON(url_geo)

if (is.null(geo$results)) {
  cat("Cidade não encontrada.\n")
} else {
  lat <- geo$results$latitude[1]
  lon <- geo$results$longitude[1]
  nome <- geo$results$name[1]
  pais <- geo$results$country[1]

  url_clima <- paste0(
    "https://api.open-meteo.com/v1/forecast?latitude=", lat,
    "&longitude=", lon,
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m",
    "&timezone=auto"
  )

  clima <- fromJSON(url_clima)

  cat("Local:", nome, "-", pais, "\n")
  cat("Temperatura:", clima$current$temperature_2m, "°C\n")
  cat("Umidade:", clima$current$relative_humidity_2m, "%\n")
  cat("Vento:", clima$current$wind_speed_10m, "km/h\n")
  cat("Horário:", clima$current$time, "\n")
}