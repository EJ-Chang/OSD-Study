# ACC analysis
# read data
setwd('/Users/YJC/Dropbox/ExpRecord_ACC/')
dat <- read.table('ACC_Merge.txt',
                  header = FALSE)
dat <- dat[c(1,2,8,10)]
colnames(dat) <- c('ID','Device', 'Direction', 'Answer')
dat <-dat[order(dat$Device, dat$Direction,dat$Answer),]

tapply(dat$Answer, list(dat$Device, dat$Direction), mean)
tapply(dat$Answer, list(dat$Device, dat$Direction), sd)



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
abv<-aov(mean_acc ~ Device*Direction + Error(ID/(Device*Direction)),
         data=ndat)

summary(abv)

