
"""
for z in df.values:
    print("------------------", z)
    print("-------)")
    l = []
    k = 0
    for each in dfnew:
        print(each)
        print(z[3], type(z[3]))
        if str(z[3]) in each:
            pass
        else:
            k =1
    if k == 1:
            l = [z[3], "", "", "", z[1], " "]
    j += 1
    #print(l,j)
    dfnew.append(l)
        # print(datetime.datetime.fromtimestamp(z))
dfff = pd.DataFrame(dfnew)
print(dfff)
print(len(dfnew))
print("----------------------")
"""
# dfff.to_csv('file1.csv')
"""
path = "EOL-dump"
i = 0
for each in os.listdir(path):
    i += 1
    l = []
    newpath = str(f"EOL-dump\\{each}")
    df1 = pd.read_csv(newpath)
    for z in df1['tis']:
        # print(z)
        l.append(datetime.datetime.fromtimestamp(z))
    print(i, each)
    print(l[0],"\t\t", l[-1], end="\n\n")
    # print(each)
print(i)
"""
