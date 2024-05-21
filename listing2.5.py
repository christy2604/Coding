# Nama  : Albrita Parangka
# Nim   : 23208045

# prompt the user for input
second = eval (input("enter an integer for second: "))

# get minutes and remaining seconds
minutes = second // 60 
remainingSecond = second % 60
print (second, "second is", minutes, "minutes and", remainingSecond, "seconds")
