# Belajar Python [Dasar] - 05 - Tipe Data - YouTube

# int
varInt = 10
print("====== INT ======")
print("data : ", varInt)
print("type : ", type(varInt), "\n")

# float
varFloat = 10.533
print("====== FLOAT ======")
print("data : ", varFloat)
print("type : ", type(varFloat), "\n")

# string
varString = "Ini String"
print("====== STRING ======")
print("data : ", varString)
print("type : ", type(varString), "\n")

# bool
varBool = True
print("====== Bool ======")
print("data : ", varBool)
print("type : ", type(varBool), "\n")

# complex
varComplex = complex(5,6)
print("====== Complex ======")
print("data : ", varComplex)
print("type : ", type(varComplex), "\n")


from ctypes import *
# c_bool
varCDouble = c_double(10.88888)
print("====== C Double ======")
print("data : ", varCDouble)
print("type : ", type(varCDouble), "\n")
