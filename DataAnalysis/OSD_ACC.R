# OSD analysis
# read data
setwd('/Users/YJC/Dropbox/ExpRecord_OSD/')
dat <- read.table('OSD_Merge.txt',
                  header = FALSE)
dat <- dat[c(1, 2, 3, 8, 9, 10)]
colnames(dat) <- c('ID','Device', 'Direction', 'Answer', 'Step', 'Time')
dat <-dat[order(dat$Device,dat$Answer),]


correctDat <- dat[dat$Direction=='OK',]
correctDat <- correctDat[correctDat$Step>=1,]
tapply(correctDat$Time/correctDat$Step, list(correctDat$Device), mean)
tapply(correctDat$Time/correctDat$Step, list(correctDat$Device), sd)


# Test

# Data manipulation
library(dplyr)

ndat <- correctDat %>%
  group_by(Device, ID) %>%
  summarize(mean_acc = mean(correctDat$Time/correctDat$Step, na.rm = TRUE))

# Method 1
ACCanova<-aov(ndat$mean_acc~ndat$Device)

anova(ACCanova)


# Method 2
abv<-aov(mean_acc ~ Device + Error(ID/(Device)),
         data=ndat)

summary(abv)
