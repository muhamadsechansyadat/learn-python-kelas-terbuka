# belajar-python-11-function-arguments

# function argument
def staff(nama):
    print("Staff IT bernama :", nama)

staff('Sechan')

# function keyword argument
def staffNOC(nama, shift):
    print("Staff NOC bernama : ", nama)
    print("Staff NOC bershift : ", shift)

staffNOC(nama='Sechan', shift='Malam')

# function default argument
def security(nama, shift='Malam', attitude='Tidak'):
    print("Staff Security bernama : ", nama)
    print("Staff Security bershift : ", shift)
    print("Staff Security berattitude : ", attitude)

security("Sechan")