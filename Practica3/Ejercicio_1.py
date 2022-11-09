palabra = input("Dame una palabra: ")
if palabra[-2:] == "ar" or palabra[-2:] == "er" or palabra[-2:] == "ir":
    print(palabra[:-2]+"ing")
else:
    print(palabra+"tion")
