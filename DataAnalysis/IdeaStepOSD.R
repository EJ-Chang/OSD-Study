library(tidyverse)
library(ggpubr)
library(rstatix)
library(dplyr)
require(nlme)
require(multcomp)


# Ideal solution in OSD
ideadat <- read.table('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/DelibrateTrigger.txt',
                      header = FALSE)

colnames(ideadat) <- c('ID', 'Device', 'Direction',
                   'iRow', 'iCol',
                   'reqRow', 'reqCol',
                   'Answer',
                   'stepToGoal',
                   'Time', 'RealTime', 'Delibrately')
ideadat <- ideadat[ideadat$Delibrately==1,]

# Describe data

tapply(ideadat$Time, list(ideadat$Device, ideadat$Direction), mean)

# Visualization ====

bxp <- ggboxplot(
  ideadat, x = "Direction", y = "Time",
  color = "Device", palette = "jco"
)
bxp

# RT ====
abv<-aov(Time ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = ideadat)

summary(abv)

# Effect of treatment at each time point
# Pairwise comparisons between treatment groups
pwc <- ideadat %>%
  group_by(Device) %>%
  pairwise_t_test(
    Time ~ Direction,
    p.adjust.method = "bonferroni"
  )
pwc

pwc <- ideadat %>%
  group_by(Direction) %>%
  pairwise_t_test(
    Time ~ Device,
    p.adjust.method = "bonferroni"
  )
pwc


ideadat %>% 
  pairwise_t_test(
    Time ~ Device,
    p.adjust.method = 'bonferroni'
  )

ideadat %>% 
  pairwise_t_test(
    Time ~ Direction,
    p.adjust.method = 'bonferroni'
  )

# Delibrate Tigger ====

delibrate <- read.table('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/Delibrate.txt',
                        header = FALSE)


colnames(delibrate) <- c('Device', 'Direction',
                       'ID', 'Freq')
# Describe data
tapply(delibrate$Freq, list(delibrate$Device, delibrate$Direction), mean)

# Anova
abv<-aov(Freq ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = delibrate)

summary(abv)
