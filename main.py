from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar

print(" Chatbot iniciado. Escribe 'salir' para terminar.")

while True:
    user_input = sanitizar(input("Tú: "))

    if user_input == "salir":
        print("Adiós ")
        break

    #  CLIMA (más flexible)
    elif any(p in user_input for p in ["clima", "tiempo", "weather"]):
        print(obtener_clima("La Paz"))

    #  ACCIONES (más flexible)
    elif any(p in user_input for p in ["accion", "acciones", "stock", "precio", "bolsa"]):
        print(obtener_precio_accion("AAPL"))

    #  saludo
    elif any(p in user_input for p in ["hola", "hey", "buenas"]):
        print("Hola  dime clima o acciones")

    else:
        print("No entendí. Prueba: clima o acciones")
