import matplotlib.pyplot as plt
import pandas as pd
import json
import os

# Función de interés compuesto
def IC(capital, tasa, tiempo, n):
    valor_futuro = capital * (1 + tasa / n) ** (n * tiempo)
    interes = valor_futuro - capital
    return interes, valor_futuro

# Función para entrada manual
def entrada_manual():
    print("\n📝 ENTRADA MANUAL")
    print("-" * 20)
    P = float(input("Ingrese el capital inicial: "))
    r = float(input("Ingrese la tasa de interés anual (%): ")) / 100
    t = float(input("Ingrese el tiempo (en años): "))
    n = int(input("Ingrese el número de capitalizaciones por año: "))
    return P, r, t, n

# Función para cargar datos desde archivo
def cargar_desde_archivo():
    print("\n📂 CARGAR DESDE ARCHIVO")
    print("-" * 20)
    nombre_archivo = input("Nombre del archivo JSON: ")
    
    if not nombre_archivo.endswith('.json'):
        nombre_archivo += '.json'
    
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)
            
            P = datos['capital']
            r = datos['tasa'] / 100
            t = datos['tiempo'] 
            n = datos['n']
            print("✓ Datos cargados correctamente")
            return P, r, t, n
            
        except Exception as e:
            print(f"✗ Error en el archivo: {e}")
            return None
    else:
        print(f"✗ El archivo '{nombre_archivo}' no existe")
        return None

# Función para guardar datos
def guardar_datos(P, r, t, n):
    print("\n💾 GUARDAR DATOS")
    print("-" * 20)
    nombre_json = input("Nombre del archivo JSON: ")
    
    if not nombre_json.endswith('.json'):
        nombre_json += '.json'
    
    datos_guardar = {
        "capital": P,
        "tasa": r * 100,
        "tiempo": t,
        "n": n
    }
    
    try:
        with open(nombre_json, 'w') as f:
            json.dump(datos_guardar, f, indent=4)
        print(f"✓ Configuración guardada en: {nombre_json}")
        return True
    except Exception as e:
        print(f"✗ Error al guardar: {e}")
        return False

# Función principal
def main():
    while True:
        print("\n" + "=" * 50)
        print("CALCULADORA DE INTERÉS COMPUESTO")
        print("=" * 50)
        print("1. Ingresar datos manualmente")
        print("2. Cargar datos desde archivo")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '1':
            # Opción 1: Entrada manual
            P, r, t, n = entrada_manual()
            
            # Calcular resultados
            interes, valor_futuro = IC(P, r, t, n)
            
            # Mostrar resultados
            print(f"\n{' RESULTADOS ':=^40}")
            print(f"Capital inicial: ${P:,.2f}")
            print(f"Tasa de interés anual: {r*100:.2f}%")
            print(f"Tiempo: {t} años")
            print(f"Capitalizaciones por año: {n}")
            print(f"Interés generado: ${interes:,.2f}")
            print(f"Valor futuro: ${valor_futuro:,.2f}")
            
            # Preguntar si guardar
            guardar = input("\n¿Quieres guardar estos datos? (s/n): ")
            if guardar.lower() == 's':
                guardar_datos(P, r, t, n)
            
            # Generar gráfica
            años = [i/n for i in range(int(n*t)+1)]
            valores = [P * (1 + r/n) ** (n * i) for i in años]
            
            plt.figure(figsize=(10, 6))
            plt.plot(años, valores, marker='o', linewidth=2)
            plt.title('Crecimiento del Capital con Interés Compuesto')
            plt.xlabel('Años')
            plt.ylabel('Valor acumulado ($)')
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()
            
            # Guardar en Excel
            df = pd.DataFrame({'Tiempo (años)': años, 'Valor acumulado ($)': valores})
            archivo_excel = 'interes_compuesto.xlsx'
            df.to_excel(archivo_excel, index=False)
            print(f"✓ Datos guardados en Excel: {archivo_excel}")
            
        elif opcion == '2':
            # Opción 2: Cargar desde archivo
            datos = cargar_desde_archivo()
            
            if datos:
                P, r, t, n = datos
                
                # Calcular resultados
                interes, valor_futuro = IC(P, r, t, n)
                
                # Mostrar resultados
                print(f"\n{' RESULTADOS ':=^40}")
                print(f"Capital inicial: ${P:,.2f}")
                print(f"Tasa de interés anual: {r*100:.2f}%")
                print(f"Tiempo: {t} años")
                print(f"Capitalizaciones por año: {n}")
                print(f"Interés generado: ${interes:,.2f}")
                print(f"Valor futuro: ${valor_futuro:,.2f}")
                
                # Generar gráfica
                años = [i/n for i in range(int(n*t)+1)]
                valores = [P * (1 + r/n) ** (n * i) for i in años]
                
                plt.figure(figsize=(10, 6))
                plt.plot(años, valores, marker='o', linewidth=2)
                plt.title('Crecimiento del Capital con Interés Compuesto')
                plt.xlabel('Años')
                plt.ylabel('Valor acumulado ($)')
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.show()
                
                # Guardar en Excel
                df = pd.DataFrame({'Tiempo (años)': años, 'Valor acumulado ($)': valores})
                archivo_excel = 'interes_compuesto.xlsx'
                df.to_excel(archivo_excel, index=False)
                print(f"✓ Datos guardados en Excel: {archivo_excel}")
            
        elif opcion == '3':
            print("¡Hasta luego!")
            break
            
        else:
            print("❌ Opción no válida. Por favor seleccione 1, 2 o 3.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
