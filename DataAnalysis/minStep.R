# Go to working directory
setwd('/Users/YJC/Dropbox/ExpRecord_OSD/')
dat <- read.table('OSD_Merge.txt',
                  header = FALSE)

colnames(dat) <- c('ID','Device', 'Direction', 'Answer', 'Step', 'Time')

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
