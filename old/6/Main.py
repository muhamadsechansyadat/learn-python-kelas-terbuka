# bab function

def function1():
    print("ini function 1")

def function2():
    print("ini function 2")
    function1()

def perkalian10(varInputAngka):
    varAngka = 10
    varTotal = varAngka * varInputAngka
    print("Jika", varAngka, "x", varInputAngka, "sama dengan", varTotal)

perkalian10(2)
# def testFunction(response, response2):
#     print(response, response2)
#
# varRes = "ini adalah function"
# varRes2 = "ini adalah param function 2"
# testFunction(varRes, varRes2)
