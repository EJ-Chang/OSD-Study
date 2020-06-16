# RT analysis
# read data
setwd('/Users/YJC/Dropbox/ExpRecord_RT/')
dat <- read.table('/Users/YJC/Dropbox/ExpRecord_RT/RT_Merge.txt',
           header = FALSE)

dat <- dat[c(1,5,6,7,8)]
colnames(dat) <- c('ID','Device', 'Direction', 'Answer', 'RT')
dat <-dat[order(dat$Device, dat$Direction,dat$Answer),]
# Get RT mean by condition
tapply(dat$RT, list(dat$Device, dat$Direction), mean)
tapply(dat$RT, list(dat$Device, dat$Direction), sd)
RTanova<-aov(dat$RT~dat$Direction*dat$Device)

anova(RTanova)

library(tidyverse)
library(ggpubr)
library(rstatix)
res.aov <- anova_test(
  data = dat, dv = RT, wid = ID,
  within = c(Device, Direction)
)
get_anova_table(res.aov)



# test

dat %>% sample_n_by(Device, size = 1)

dat %>%
  group_by(Device, Direction) %>%
  get_summary_stats(RT, type = "mean_sd")


dat %>%
  group_by(Device, Direction) %>%
  identify_outliers(RT)


dat %>%
  group_by(Device, Direction) %>%
  shapiro_test(RT)


res.aov <- anova_test(
  data = dat, dv = RT, wid = ID,
  within = c(Device, Direction)
)




dat2 <- within(dat, {
  ID   <- factor(ID)
  Device <- factor(Device)
  Direction <- factor(Direction)
})

dat2 <- dat2[order(dat2$ID), ]
head(dat2)

dat.mean <- aggregate(dat$RT,
                         by = list(dat$ID, dat$Device,
                                   dat$Direction),
                         FUN = 'mean')

colnames(dat.mean) <- c("ID","Device","Direction","RT")

dat.mean <- dat.mean[order(dat.mean$ID), ]


reaction.aov <- with(dat.mean,
                   aov(RT ~ Device * Direction +
                         Error(ID))
)
summary(reaction.aov)
res.aov2 <- aov(RT ~ Device + Direction, data = dat.mean)
summary(res.aov2)

abv<-aov(RT ~ Device*Direction + Error(ID/(Device*Direction)),
         data=dat.mean)

summary(abv)
# I don't have enough degree of freedom
