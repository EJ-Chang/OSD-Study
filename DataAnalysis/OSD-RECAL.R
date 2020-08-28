# Data of OSD re-calibrated

library(tidyverse)
library(ggpubr)
library(rstatix)
library(dplyr)
require(nlme)
require(multcomp)
library(ggplot2)

dat <- read.table('/Users/YJC/Dropbox/UsabilityTesting/DataAnalysis/OSDrecal.dat', 
                  header = FALSE)


colnames(dat) <- c('ID', 'Device', 'Direction',
                   'iRow', 'iCol',
                   'reqRow', 'reqCol',
                   'Answer', 'Step',
                   'Time', 'TimeStamp', 'RT',
                   'nTrial', 'D_need', 'K_need',
                   'AcTrg'
                   )

dat <- dat[,c(-4,-5,-10,-11)]

dat <- dat[dat$AcTrg==1,]

# Mean SD====

tapply(dat$RT, list(dat$Device, dat$Direction), mean)
tapply(dat$RT, list(dat$Device, dat$Direction), sd)

# outlier ==== 
b<-boxplot(dat$RT)
lowerwhisker<-b$stats[1]
upperwhisker<-b$stats[5]
testdata<-dat[dat$RT>lowerwhisker & dat$RT<upperwhisker,]

# boxplot(testdata$RT)

# Visualization ====

bxp <- ggboxplot(
  testdata, x = "Direction", y = "RT",
  color = "Device", palette = "jco"
)
bxp

p <- ggplot(testdata, aes(x=Direction, y=RT, fill = Device)) + 
  scale_x_discrete(limits=c("Up","Down","Left","Right","OK")) +
  geom_boxplot() 
p


# RT ====
abv<-aov(RT ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = testdata)

summary(abv)


# Effect of treatment at each time point
abv<-aov(RT ~ Device + 
           Error(ID/(Device)),
         data = testdata)

summary(abv)

abv<-aov(RT ~ Direction + 
           Error(ID/(Direction)),
         data = testdata)

summary(abv)

# Pairwise comparisons between treatment groups
pwc_direction <- testdata %>%
  group_by(Device) %>%
  pairwise_t_test(
    RT ~ Direction,
    p.adjust.method = "bonferroni"
  )
pwc_direction

pwc_device <- testdata %>%
  group_by(Direction) %>%
  pairwise_t_test(
    RT ~ Device,
    p.adjust.method = "bonferroni"
  )
pwc_device
