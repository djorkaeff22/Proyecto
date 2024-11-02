edad = int(input("ingrese su edad: "))
if edad <= 10:
    precio=3000
elif edad <= 15:
    precio=5000
elif edad < 18:
    precio=7500
elif edad >= 50:
    print("muy grande para videojuegos?pongase a bretear mejor")
else:
    precio=10000
print("el precio de la entrada es :",precio,"colones")