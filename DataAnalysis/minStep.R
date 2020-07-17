# Go to working directory
setwd('/Users/YJC/Dropbox/ExpRecord_OSD/')
dat <- read.table('OSD_Merge.txt',
                  header = FALSE)

colnames(dat) <- c('ID', 'Device', 'Direction',
                   'iRow', 'iCol',
                   'reqRow', 'reqCol',
                   'Answer',
                   'stepToGoal',
                   'Time', 'RealTime')


# mini step
reqRow <- c(1, 3, 2, 1, 4, 2, 3, 3, 2, 1, 
            3, 3, 3, 3, 1, 1, 3, 2, 3, 4, 
            1, 1, 2, 3, 4, 1, 4, 2, 4, 2, 
            2, 4, 2, 1, 4, 3, 2, 1, 4, 2, 
            3, 2, 4, 4, 3, 4, 1, 4, 1, 3, 
            1, 3, 3, 3, 3, 4, 2, 2, 4, 3, 
            2, 3, 4, 1, 1, 1, 4, 1, 3, 4, 
            3, 2, 4, 4, 1, 1, 2, 1, 3, 2, 
            4, 4, 2, 3, 2, 2, 3, 4, 4, 3, 
            4, 2, 1, 1, 1, 3, 2, 4, 4, 1)

reqCol <- rep(c(0, 1, 2, 3), times = 10)

reqSti <- cbind(reqRow[1:40], reqCol)

StiQue <- c(10, 31, 22, 13, 40, 21, 32, 33, 20, 11, 32, 33, 30, 31, 12, 13, 30, 21,
            32, 43, 10, 11, 22, 33, 40, 11, 42, 23, 40, 21, 22, 43, 20, 11, 42, 33, 20,
            11, 42, 23)

table(StiQue)


# residual steps
# res<-dat[dat$Direction!='OK',]
res<-dat[dat$Time>0.1,]

res_dpad <- res[res$Device=='dPad',]
count_dpad<- table(res_dpad$Direction)
as.array(count_dpad)
count_dpad[1] <- count_dpad[1] - 1552 # subtract Down 
count_dpad[3] <- count_dpad[3] - 640 # subtract OK
count_dpad

res_Wheel <- res[res$Device!='dPad',]
count_Wheel <- table(res_Wheel$Direction)
as.array(count_Wheel)
count_Wheel[1] <- count_Wheel[1] - 1552 # subtract Down 
count_Wheel[3] <- count_Wheel[3] - 640 # subtract OK
count_Wheel

count_Wheel[3] <- 0
count_Wheel[4] <- count_Wheel[4] - 29


chisq.test(rbind(count_dpad[-3], count_Wheel[-3]))

# Chi square test and post hoc
M <- as.table(rbind(count_dpad[-3], count_Wheel[-3]))
dimnames(M) <- list(Device = c("dPad", "Wheel"),
                    Direction = c("Down","Left","Right","Up"))
chisq.test(M)
chisq.posthoc.test(M)
# ----


