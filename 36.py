sum = 0

for x in range(1, 1000000):
  getBin = lambda x: x >= 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
  if int(str(x)[::-1]) == x and getBin(x) == getBin(x)[::-1]: sum += x

print sum
