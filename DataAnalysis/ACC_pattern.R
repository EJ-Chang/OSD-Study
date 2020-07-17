errorIndex <- dat3[dat3$Answer==0,]$a
preIndex<-errorIndex-1

patternIndex <- c(errorIndex, preIndex)
patternIndex <- sort(patternIndex)


padat <- dat3[patternIndex,]

padat[padat$Device != 'dPad',]




abv<-aov(RT ~ Device*Direction + 
           Error(ID/(Device*Direction)),
         data = padat)

summary(abv)


table(padat$Device, padat$Direction)

errdat <- dat3[errorIndex,]
predat <- dat3[preIndex,]


preDirection <-predat$Direction
dat4 <- cbind(errdat, preDirection)


dat5<-dat4[dat4$Direction == dat4$preDirection,]


ndat <- dat5[c(2,6)] %>%
  group_by(Device, Direction) %>%
  count()

res.aov2 <- aov(freq ~ Device + Direction, data = ndat)
summary(res.aov2)
