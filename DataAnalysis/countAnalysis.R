# Load data
All <- read.table('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/OSD direction.dat',
                  header = FALSE)
colnames(All) <- c('Device', 'Direction', 'ID', 'Freq')

All

abv<-aov(Freq ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data=All)

summary(abv)

library(tidyverse)
library(ggpubr)
library(rstatix)
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
