import matplotlib.pyplot as plt
import pandas as pd
import json
import os

# Función de interés compuesto
def IC(capital, tasa, tiempo, n):
    """
    Calcula el interés compuesto y el valor futuro.
    capital: capital inicial
    tasa: tasa de interés anual en forma decimal (ej. 0.08 para 8%)
    tiempo: tiempo en años
    n: número de capitalizaciones por año
    """
    valor_futuro = capital * (1 + tasa / n) ** (n * tiempo)
    interes = valor_futuro - capital
    return interes, valor_futuro

# Función para leer datos desde archivo
def leer_datos_desde_archivo(archivo):
    """
    Lee datos desde un archivo JSON o CSV
    """
    if not os.path.exists(archivo):
        print(f"El archivo {archivo} no existe.")
        return None
    
    extension = archivo.lower().split('.')[-1]
    
    try:
        if extension == 'json':
            with open(archivo, 'r') as f:
                datos = json.load(f)
            return datos
        elif extension == 'csv':
            df = pd.read_csv(archivo)
            return df.to_dict('records')[0]  # Toma la primera fila
        else:
            print(f"Formato de archivo no soportado: {extension}")
            return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

# Función para guardar configuración
def guardar_configuracion(datos, archivo):
    """
    Guarda la configuración en un archivo JSON
    """
    try:
        with open(archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Configuración guardada en: {archivo}")
    except Exception as e:
        print(f"Error al guardar la configuración: {e}")

# Función para generar reporte completo
def generar_reporte_completo(datos, resultados, archivo):
    """
    Genera un reporte completo en formato JSON
    """
    reporte = {
        "parametros_entrada": datos,
        "resultados": resultados,
        "resumen": {
            "capital_inicial": datos['capital'],
            "valor_futuro": resultados['valor_futuro'],
            "interes_generado": resultados['interes'],
            "tasa_anual": datos['tasa'] * 100,
            "periodo": datos['tiempo'],
            "capitalizaciones_anuales": datos['n']
        }
    }
    
    try:
        with open(archivo, 'w') as f:
            json.dump(reporte, f, indent=4)
        print(f"Reporte completo guardado en: {archivo}")
    except Exception as e:
        print(f"Error al generar el reporte: {e}")

# Función principal
def main():
    print("Calculadora de Interés Compuesto")
    print("=" * 40)
    
    # Preguntar si desea cargar datos desde archivo
    usar_archivo = input("¿Desea cargar datos desde un archivo? (s/n): ").lower()
    
    if usar_archivo == 's':
        archivo_entrada = input("Ingrese el nombre del archivo (JSON o CSV): ")
        datos = leer_datos_desde_archivo(archivo_entrada)
        
        if datos:
            P = datos.get('capital', datos.get('P', 0))
            r = datos.get('tasa', datos.get('r', 0)) / 100
            t = datos.get('tiempo', datos.get('t', 0))
            n = datos.get('n', datos.get('capitalizaciones', 1))
            print("✓ Datos cargados desde archivo")
        else:
            print("Usando entrada manual...")
            P = float(input("Ingrese el capital inicial: "))
            r = float(input("Ingrese la tasa de interés anual (%): ")) / 100
            t = float(input("Ingrese el tiempo (en años): "))
            n = int(input("Ingrese el número de veces que se capitaliza el interés por año: "))
    else:
        # Entrada manual de datos
        P = float(input("Ingrese el capital inicial: "))
        r = float(input("Ingrese la tasa de interés anual (%): ")) / 100
        t = float(input("Ingrese el tiempo (en años): "))
        n = int(input("Ingrese el número de veces que se capitaliza el interés por año: "))
    
    # Calcular interés compuesto
    interes, valor_futuro = IC(P, r, t, n)
    
    # Mostrar resultados
    print(f"\n{' RESULTADOS ':=^40}")
    print(f"Capital inicial: ${P:,.2f}")
    print(f"Tasa de interés anual: {r*100:.2f}%")
    print(f"Tiempo: {t} años")
    print(f"Capitalizaciones por año: {n}")
    print(f"Interés generado: ${interes:,.2f}")
    print(f"Valor futuro: ${valor_futuro:,.2f}")
    
    # Guardar configuración actual
    guardar_config = input("\n¿Desea guardar esta configuración? (s/n): ").lower()
    if guardar_config == 's':
        config = {
            "capital": P,
            "tasa": r * 100,  # Guardar como porcentaje
            "tiempo": t,
            "n": n
        }
        archivo_config = input("Nombre del archivo de configuración (ej: config.json): ")
        guardar_configuracion(config, archivo_config)
    
    # Generar datos para la gráfica
    años = [i/n for i in range(int(n*t)+1)]
    valores = [P * (1 + r/n) ** (n * i) for i in años]
    
    # Crear DataFrame con la evolución
    df = pd.DataFrame({
        'Año': [f"{año:.2f}" for año in años],
        'Valor_Acumulado': valores,
        'Interes_Acumulado': [valor - P for valor in valores]
    })
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(años, valores, marker='o', linewidth=2, markersize=4)
    plt.title('Crecimiento del Capital con Interés Compuesto', fontsize=14, fontweight='bold')
    plt.xlabel('Años')
    plt.ylabel('Valor acumulado ($)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Preguntar si guardar la gráfica
    guardar_grafica = input("\n¿Desea guardar la gráfica? (s/n): ").lower()
    if guardar_grafica == 's':
        nombre_grafica = input("Nombre del archivo de la gráfica (ej: grafica.png): ")
        plt.savefig(nombre_grafica, dpi=300, bbox_inches='tight')
        print(f"Gráfica guardada como: {nombre_grafica}")
    
    plt.show()
    
    # Guardar datos en diferentes formatos
    print("\n" + "="*40)
    print("GUARDAR DATOS")
    print("="*40)
    
    # Excel
    archivo_excel = 'interes_compuesto.xlsx'
    df.to_excel(archivo_excel, index=False)
    print(f"✓ Datos guardados en Excel: {archivo_excel}")
    
    # CSV
    archivo_csv = 'interes_compuesto.csv'
    df.to_csv(archivo_csv, index=False)
    print(f"✓ Datos guardados en CSV: {archivo_csv}")
    
    # JSON con reporte completo
    datos_entrada = {
        "capital": P,
        "tasa": r,
        "tiempo": t,
        "n": n
    }
    
    resultados_calc = {
        "interes": interes,
        "valor_futuro": valor_futuro
    }
    
    archivo_reporte = 'reporte_interes_compuesto.json'
    generar_reporte_completo(datos_entrada, resultados_calc, archivo_reporte)
    
    print(f"\n¡Proceso completado! Se han generado 3 archivos:")
    print(f"1. {archivo_excel} - Datos detallados en Excel")
    print(f"2. {archivo_csv} - Datos detallados en CSV")
    print(f"3. {archivo_reporte} - Reporte completo en JSON")

if __name__ == "__main__":
    main()
