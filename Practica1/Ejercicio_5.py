# Datos
print("Dime los siguientes valores y te daré la temperatura de sensación: ")
velocidad = float(input("Dame la velocidad del viento: "))
temperatura_aire = float(input("Dame la temperatura del aire en Celsius: "))

# Operación
temperatura_de_sensacion = 13.12 + (0.6215 * temperatura_aire) - (11.37 * (velocidad ** 0.16)) + \
                           (0.3965 * temperatura_aire) * (velocidad ** 0.16)
# print
print("La temperatura de sensación es: ", round(temperatura_de_sensacion, 2))