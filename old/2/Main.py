# chapter if elif else
print(50*"=", " Chapter 1 ", 50*"=")
nilaiA = 80
nilaiB = 75

# nested if
if nilaiA == 80: #equal eksplisit
    print("Nilai A Anda : ", nilaiA)
    if nilaiB == 75:
        print("Nilai B Anda : ", nilaiB)
# nested if

nilai = 60
if nilai == 60: #equal
    print("Nilai anda : ", nilai)
if nilai != 60: #not equal
    print("Nilai anda bukan : 60")

nilaiMatkul = 30
print(50*"=") #for comment
if 80 <= nilaiMatkul <= 100:
    print("Nilai Matkul anda : A")
elif 70 <= nilaiMatkul < 80:
    print("Nilai Matkul anda : B")
elif 60 <= nilaiMatkul < 70:
    print("Nilai Matkul anda : C")
elif 50 <= nilaiMatkul < 60:
    print("Nilai Matkul anda : D, Silahkan lakukan perbaikan")
else:
    print("Anda tidak lulus matkul ini !!!")

print(50*"=", " Chapter 2 ", 50*"=")

buah = ["apel","anggur","jeruk","tomat","pepaya","semangka"]
beli = "kesemek"

if beli in buah:
    print("Ya saya jual buah", beli)

if not beli in buah:
    print("Saya tidak menjual buah", beli)

char = "z"
if char in beli:
    print("Ya ada karakter", char, "di beli")
else :
    print("Tidak ada karakter", char, "di beli")
