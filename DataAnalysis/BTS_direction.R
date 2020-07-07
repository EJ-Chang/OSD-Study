# BTS analysis

setwd('/Users/YJC/Dropbox/ExpRecord_BTS/')
dat <- read.table('/Users/YJC/Dropbox/ExpRecord_BTS/BTS_Merge.txt',
                  header = FALSE)
colnames(dat) <- c('ID', 'reqDevice','Device',
                   'QueType',
                   'reqRow', 'reqCol',
                   'Direction',
                   'Answer',
                   'Time', 'RealTime')

# RT ====
tapply(dat$Time, list(dat$Device, dat$Direction), mean)
tapply(dat$Time, list(dat$Device, dat$Direction), sd)


# Data manipulation
library(dplyr)

ndat <- dat %>%
  group_by(Device, Direction, ID) %>%
  summarize(mean_RT = mean(Answer, na.rm = TRUE))


# Method 2
abv<-aov(mean_RT ~ Device*Direction + Error(ID/(Device*Direction)),
         data=ndat)

summary(abv)

# BTS distribution ====

require(chisq.posthoc.test)



res_dPad <- dat[dat$Device =='dPad',]

count_dPad <- table(res_dPad$QueType, res_dPad$Direction)


chisq.test(count_dPad)
chisq.posthoc.test(count_dPad)


res_Wheel <- dat[dat$Device != 'dPad',]

count_Wheel <- table(res_Wheel$QueType, res_Wheel$Direction)

chisq.test(count_Wheel)
chisq.posthoc.test(count_Wheel)


OK <- as.table(rbind(count_dPad[,1], count_Wheel[,1]))
dimnames(OK) <- list(Device = c('dPad','Wheel'),
                    QueType = c('Radio', 'Switch', 'Switch_clue'))
chisq.test(OK)
chisq.posthoc.test(OK)



R <- as.table(rbind(count_dPad[,2], count_Wheel[,2]))
dimnames(R) <- list(Device = c('dPad','Wheel'),
                     QueType = c('Radio', 'Switch', 'Switch_clue'))
chisq.test(R)
chisq.posthoc.test(R)
