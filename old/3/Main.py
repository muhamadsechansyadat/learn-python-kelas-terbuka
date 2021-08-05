# list itterable
jajan = ['baso', 'cimol', 'cilok', 'cilor']

for beli in jajan:
    print(beli)

# string itterable
varString = 'sechan'

for nama in varString:
    print(nama)

print(100*"=")
# for in for

varBuah = ['semangka', 'melon', 'jeruk', 'anggur']
varSayur = ['timun', 'tomat', 'cabai', 'selada']

varDataBelanjaan = [jajan, varBuah, varSayur]

for dataBelanja in varDataBelanjaan:
    for semuaBelanjaan in dataBelanja:
        print(semuaBelanjaan)