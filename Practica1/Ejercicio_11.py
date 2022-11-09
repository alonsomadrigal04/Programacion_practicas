# Entradas
peso = float(input("Calcularemos tu IMC, dime primero tu peso (kg): "))
altura = float(input("Dime ahora tu altura (m): "))

# IMC
imc = round(peso / (altura ** 2), 2)
print(imc)
# Condicionales
if imc >= 40:
    print("Tienes: Obesidad mórbida")
elif 40 > imc >= 30:
    print("Tienes: obesidad")
elif 30 > imc >= 25:
    print("Tienes: sobrepeso")
elif 24.99 > imc > 18.5:
    print("Tienes: peso normal")
else:
    print("Tienes: bajo peso")

