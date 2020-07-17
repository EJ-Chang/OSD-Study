# OSD analysis
# read data
setwd('/Users/YJC/Dropbox/ExpRecord_OSD/')
dat <- read.table('OSD_Merge.txt',
                  header = FALSE)
dat <- dat[c(1, 2, 3, 8, 9, 10)]
colnames(dat) <- c('ID','Device', 'Direction', 'Answer', 'Step', 'Time')
dat <-dat[order(dat$Device,dat$Answer),]



# Get RT mean by condition
tapply(dat$Answer, list(dat$Device, dat$Direction, dat$ID), mean)
tapply(dat$Answer, list(dat$Device, dat$Direction, dat$ID), sd)

# Data manipulation
library(dplyr)

ndat <-dat %>%
  group_by(Device, Direction, ID) %>%
  summarize(mean_acc = mean(Answer, na.rm = TRUE))

# Method 1
ACCanova<-aov(ndat$mean_acc~ndat$Direction*ndat$Device)

anova(ACCanova)



# Method 2
abv<-aov(mean_acc ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data=ndat)

library(tidyverse)
library(ggpubr)
library(rstatix)
a %>%
  pairwise_t_test(
    Freq ~ Direction, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )



subsetdata <- dat[dat$Direction!='OK',]
# Method 2
abv<-aov(Time ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = subsetdata)

summary(abv)

subsetdata %>% 
  pairwise_t_test(
    Time ~ Device,
    p.adjust.method = 'bonferroni'
  )

subsetdata %>% 
  pairwise_t_test(
    Time ~ Direction,
    p.adjust.method = 'bonferroni'
  )

