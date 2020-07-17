# ACC analysis
# read data
setwd('/Users/YJC/Dropbox/ExpRecord_ACC/')
dat <- read.table('ACC_Merge.txt',
                  header = FALSE)
# dat <- dat[c(1,2,8,10)]
# colnames(dat) <- c('ID','Device', 'Direction', 'Answer')
dat <- dat[c(-6,-7)]
colnames(dat) <- c('ID','Device',
                   'nTrial', 'nLine',
                   'resHW', 'Direction',
                   'que','Answer', 'RT', 'TimeStamp')
# Error path ====
library(dplyr)

dat2 <- dat[dat$Answer==0,]

ndat <- dat2 %>%
  group_by(Device, Direction, ID) %>%
  count()


abv2<-aov(n ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = ndat)


summary(abv2)


abv<-aov(RT ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = dat)

summary(abv)


mean_RT <- ddply(dat, c("ID",'Device','Direction'), 
                 summarise, mean = mean(RT))

abv<-aov(mean ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = mean_RT)

summary(abv)

mean_RT %>%
  pairwise_t_test(
    mean ~ Device, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )  

# Wheel has longer RT


mean_ACC <- ddply(dat, c("ID",'Device','Direction'), 
                 summarise, mean = mean(Answer))

abv<-aov(mean ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = mean_ACC)

summary(abv)

mean_ACC %>%
  pairwise_t_test(
    mean ~ Device, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )  
# dPad has higher ACC


# post Hoc now
# no sig. interaction
# comparisons for treatment variable
library(tidyverse)
library(ggpubr)
library(rstatix)

dat2 %>%
  pairwise_t_test(
    RT ~ Device, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )
# comparisons for time variable
selfesteem2 %>%
  pairwise_t_test(
    score ~ time, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )




# Need posthoc
#Using MVA10.0 data
require(nlme)
require(multcomp)




# ACC ====

dat <-dat[order(dat$Device, dat$Direction,dat$Answer),]

tapply(dat$Answer, list(dat$Device, dat$Direction), mean)
tapply(dat$Answer, list(dat$Device, dat$Direction), sd)



# Get RT mean by condition
tapply(dat$Answer, list(dat$Device, dat$Direction, dat$ID), mean)
tapply(dat$Answer, list(dat$Device, dat$Direction, dat$ID), sd)

# Data manipulation
library(dplyr)

ndat <- dat %>%
  group_by(Device, Direction, ID) %>%
  summarize(mean_acc = mean(Answer, na.rm = TRUE))

# Method 1
ACCanova<-aov(ndat$mean_acc~ndat$Direction*ndat$Device)

anova(ACCanova)


# Method 2
abv<-aov(mean_acc ~ Device*Direction + Error(ID/(Device*Direction)),
         data=ndat)

summary(abv)

# Errors analysis
errkey <- dat[dat$Answer==0,]
table(errkey$Device,errkey$Direction)


chisq.test(c(5,7,2,4), p = c(0.25,0.25,0.25,0.25))
chisq.test(c(77,104,37,75), p = c(0.25,0.25,0.25,0.25))
