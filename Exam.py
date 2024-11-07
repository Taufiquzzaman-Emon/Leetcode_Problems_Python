def avg(self,*arg):
    arg = list(arg)
    avg = (sum(arg)/len(arg))
    return float(avg)

print(avg(1,2,3))
