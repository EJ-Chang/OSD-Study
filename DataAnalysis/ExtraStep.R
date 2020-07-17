library(dplyr)
library(tidyverse)
library(ggpubr)
library(rstatix)


setwd('/Users/YJC/Dropbox/ExpRecord_OSD')
dat <- read.table('RevOSD.txt',
                  header = FALSE)

colnames(dat) <- c('ID', 'Device', 'Direction',
                   'iRow', 'iCol',
                   'reqRow', 'reqCol',
                   'Answer',
                   'stepToGoal',
                   'Time', 'RealTime', 'Step')

ndat <- dat %>%
  group_by(Device, Direction, ID) %>%
  count()

# 2 way repeated measured
abv<-aov(n ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = ndat)

summary(abv)

# 2 way between
abv<-aov(n ~ Device*Direction,
         data = ndat)

summary(abv)

TukeyHSD(abv, 'Device')
TukeyHSD(abv, 'Direction')

# ====
ndat %>%
  pairwise_t_test(
    n ~ Direction, paired = TRUE, 
    p.adjust.method = "bonferroni"
  )

library(postHoc)


MM <- glm(n ~ Direction+0, data=ndat)
GG <- posthoc(MM)


# ====
library(nlme)
library(multcomp)
lme_velocity = lme(n ~ Device*Direction, data=ndat, random = ~1|ID)
anova(lme_velocity)


summary(glht(lme_velocity, linfct=mcp(Device = "Tukey")), test = adjusted(type = "bonferroni"))
