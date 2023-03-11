import random

def passwordGenerator(array,size):
    out = ""
    for i in range(size):
        akku = array[random.randint(0,len(array))]
        out = out+akku
    return out

def smallLetters(array):
    for i in range(97,123):
        array.append(chr(i))
    return array

def capitalLetters(array):
    for i in range(65,91):
        array.append(chr(i))
    return array

def numbers(array):
    for i in range(0,10):
        array.append(str(i))
    return array

def specialSymbols(array):
    for i in range(32,48):
        array.append(chr(i))
    for i in range(58,65):
        array.append(chr(i))
    return array

print("************************\nPASSWORD GENERATION TOOL\n************************")
while True:
    size = int(input("Enter the size of password: "))
    print('''Set the complexity of password
    1.Capital letters and small letters only
    2.Capital letters,small letters and numbers
    3.Capital letters,small letters,numbers and special symbols''')
    complexity = int(input("\nChoose the desired option: "))
    array = []
    match complexity:
        case 1:
            smallLetters(array)
            capitalLetters(array)
            print("\nThe generated password is: ",passwordGenerator(array,size))
            breaker=input("Do you want to generate another password[Y/N]: ")
            if breaker=="Y":
                pass
            else:
                break

        case 2:
            smallLetters(array)
            capitalLetters(array)
            numbers(array)
            print("\nThe generated password is: ",passwordGenerator(array,size))
            breaker=input("Do you want to generate another password[Y/N]: ")
            if breaker=="Y":
                pass
            else:
                break

        case 3:
            smallLetters(array)
            capitalLetters(array)
            numbers(array)
            specialSymbols(array)
            print("\nThe generated password is: ",passwordGenerator(array,size))
            breaker=input("Do you want to generate another password[Y/N]: ")
            if breaker=="Y":
                pass
            else:
                break
        

        



