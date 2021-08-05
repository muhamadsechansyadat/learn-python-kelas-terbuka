# belajar-python-7-for-else-range-break

varNum = 20

for i in range(0,40):
    # print(i)

    if i is varNum:
        print("angka ditemukan", varNum)
        break
else:
    print("angka", varNum, "tidak ditemukan")

print(50*"=", "space diluar loop", 50*"=")