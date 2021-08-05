# belajar-python-12-return-value

# function return value
def kuadrat(param1):
    total = param1 ** 2
    # print("kuadrat dari", param1, "adalah", total)
    return total

kuadrat(3)

def tambah(param1, param2):
    total = param1 + param2
    # print(param1, "+", param2, "=", total)
    return total

tambah(3,4)

def kali(param1, param2):
    total = param1 * param2
    # print(param1, "x", param2, "=", total)
    return total

kali(3,4)

varTotKuadrat = kuadrat(3)
varTotTambah = tambah(3,4)
varTotKali = kali(3,4)
varTotTambahKali = varTotTambah + varTotKali

print(varTotKuadrat)
print(varTotTambah)
print(varTotKali)
print(varTotTambahKali)