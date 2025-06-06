from datetime import datetime

def pedir_datos():
    print("\n=== NUEVO CÁLCULO DE GASTOS ===")
    nombre = input("¿Cuál es tu nombre? ")
    ingreso = float(input("¿Cuánto ganas al mes (en dólares)? "))

    print("\nIngresa tus gastos mensuales:")
    comida = float(input("Comida: "))
    transporte = float(input("Transporte: "))
    entretenimiento = float(input("Entretenimiento: "))
    otros = float(input("Otros: "))

    return nombre, ingreso, comida, transporte, entretenimiento, otros


def calcular_saldo(ingreso, comida, transporte, entretenimiento, otros):
    total_gastos = comida + transporte + entretenimiento + otros
    saldo = ingreso - total_gastos
    return total_gastos, saldo


def mostrar_resumen(nombre, ingreso, total_gastos, saldo):
    print("\n🔍 RESUMEN FINANCIERO")
    print(f"Nombre: {nombre}")
    print(f"Ingresos: ${ingreso:.2f}")
    print(f"Gastos totales: ${total_gastos:.2f}")
    print(f"Saldo restante: ${saldo:.2f}")

    if saldo > 0:
        print("✅ ¡Estás ahorrando! 💪")
    elif saldo == 0:
        print("😐 Estás justo, sin ahorro ni pérdida.")
    else:
        print("⚠️ Estás gastando más de lo que ganas. ¡Cuidado!")


def guardar_en_archivo(nombre, ingreso, total_gastos, saldo):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("historial_gastos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"🕓 Fecha: {fecha}\n")
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Ingresos: ${ingreso:.2f}\n")
        archivo.write(f"Gastos totales: ${total_gastos:.2f}\n")
        archivo.write(f"Saldo restante: ${saldo:.2f}\n")
        archivo.write("-" * 40 + "\n")


# BUCLE PRINCIPAL
while True:
    try:
        nombre, ingreso, comida, transporte, entretenimiento, otros = pedir_datos()
        total_gastos, saldo = calcular_saldo(ingreso, comida, transporte, entretenimiento, otros)
        mostrar_resumen(nombre, ingreso, total_gastos, saldo)
        guardar_en_archivo(nombre, ingreso, total_gastos, saldo)

        repetir = input("\n¿Quieres hacer otro cálculo? (sí/no): ").strip().lower()
        if repetir != "sí":
            print("👋 ¡Hasta luego! Revisa tu archivo 'historial_gastos.txt'")
            break

    except ValueError:
        print("❌ Error: Ingresa solo números válidos.")
