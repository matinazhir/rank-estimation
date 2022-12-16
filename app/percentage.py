from factor import columns, df, lessons, zarib, factor


temp = []
for i in range(len(columns)):
    percentage = int(input("{}:\t".format(i+1)))
    z = (percentage - lessons[columns[i]][0])/lessons[columns[i]][1]
    t = (1000*z) + 5000
    temp.append(t*lessons[columns[i]][2])
print("Taraz:\t", round((sum(temp)/sum(zarib))/factor))
