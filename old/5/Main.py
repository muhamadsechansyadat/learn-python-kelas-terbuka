# belajar-python-8-continue-dan-pass
varNum = 11

for i in range(1,11):
    print("nilai saat ini",i)

    if i is varNum:
        print("nilai var Num adalah", varNum)
        continue
        print("angka", varNum, "ditemukan")
else:
    print("end loop")

print(50*"=", "space diluar loop", 50*"=")
