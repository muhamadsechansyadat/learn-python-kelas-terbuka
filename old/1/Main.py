# chapter lists
dataLists = [1, 2, 4, 8, 16, 32, 64]

# akses list
dataList1 = dataLists[0]
dataList2 = dataLists[-3]

# cut list 
dataList3 = dataLists[:-2]
dataList4 = dataLists[-3:]

dataLists2 = [128, 256, 512, 1024, 2048, 4096]

# tambah lists
newDataLists = dataLists + dataLists2

# merubah content lists 
dataLists[5] = 3

# copy lists
copyLists = dataLists[:]
copyLists[5] = 666

# merubah content list dengan slicing
dataLists[2:4] = [111, 222]

# lists dalam list
dataLists3 = [dataLists, dataLists2]

# akses lists dalam list
x = dataLists3[1][5]

# method untuk list dalam list
dataLists.append(12345)

# function untuk list
lenLists = len(dataLists)

print(dataLists)
print(lenLists)
print(dataList4)