library(imager)

args = commandArgs(trailingOnly=TRUE)

if (!length(args)==2) {
  stop("Three arguments must be supplied ( file name where model is stored (RDataname), test file (.txt, matrix) and file name for AUC output).n", call.=FALSE)
} 

files <- list.files(args[1], pattern="*.jpg", full.names=TRUE)
df <- data.frame(img = character(), mean=double(), std=double(), stringsAsFactors=FALSE) 
str(df)
for (file in files){
  im <- load.image(file)
  #plot(im)
  m <- mean(im)
  s <- sd(im)
  den <- density(im)
  df[nrow(df) + 1,] = list(file,m,s)
  # df <- rbind(df, c(file, m))
}

write.csv(df, args[2], row.names=FALSE)
