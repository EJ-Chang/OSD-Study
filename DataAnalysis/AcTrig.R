All<- read.table('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/AccidentCount.txt', 
                 header = FALSE)

colnames(All) <- c('Device', 'Direction', 'ID', 'Freq')

# Data manipulation
library(dplyr)
library(tidyverse)
library(ggpubr)
library(rstatix)

abv<-aov(Freq ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data=All)

summary(abv)


All %>%
  pairwise_t_test(
    Freq ~ Direction, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )


All %>%
  pairwise_t_test(
    Freq ~ Device, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )
