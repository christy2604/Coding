# Nama  : Albrita Parangka
# Nim   : 23208045

import time

currentTime = time.time()

# obtain the total second since midnight, jan 1, 1970
totalsecond = int(currentTime)

#get the current second
currentsecond = totalsecond % 60

# obtain the total minutes
totalminutes = totalsecond // 60

# compute the current minute in the hour
currentminute = totalminutes % 60

# obtain the total hours
totalhours = totalminutes // 60

