import requests
import json

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

total_vulnerabilidades = requests.get(URL)
datos = total_vulnerabilidades.json()

def obtener_vulnerabilidades():
    try:
        if "vulnerabilities" in datos:
            for indice, cve in enumerate(datos["vulnerabilities"], 1): #agrega indice e imprime desde el 1 en adelante las vulnerabilidades encontradas
                print(f"{indice}. {cve['cve']['id']}")
        else:
            print("No se encontraron vulnerabilidades.")

    except requests.exceptions.RequestException as e:
        print("Error")

def obtener_vulnerabilidades_fixeadas():
    print("Prueba punto 2.")

def obtener_vulnerabilidades_no_fixeadas():
    print("Prueba punto 3.")

def obtener_informacion_severidad(): #MALO
    try:
        severidades = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
        for vulner in datos.get("result", {}).get("CVE_Items", []):
            for metric in vulner.get("cve", {}).get("metrics", {}).get("cvssMetricV2", []):
                severidad = metric.get("baseSeverity")
                if severidad in severidades:
                    severidades[severidad] += 1

        print("Recuento de severidades:")
        for categoria, cantidad in severidades.items():
            print(f"{categoria}: {cantidad}")

    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar la respuesta JSON: {e}")

obtener_informacion_severidad()
    
def mostrar_menu():
    """Muestra el menú de opciones."""
    print("Por favor, elija una de las siguientes opciones:")
    print("1) Listado total de las vulnerabilidades.")
    print("2) Recibir las vulnerabilidades fixeadas.")
    print("3) Listado de vulnerabilidades exceptuando las fixeadas (punto 2).")
    print("4) Información sumarizada de vulnerabilidades por severidad.")
    print("5) Salir - Chao con adios.")

def main():
    """Función principal para ejecutar el programa."""
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            obtener_vulnerabilidades()
        elif opcion == "2":
            obtener_vulnerabilidades_fixeadas()
        elif opcion == "3":
            obtener_vulnerabilidades_no_fixeadas()
        elif opcion == "4":
            obtener_informacion_severidad()
        elif opcion == "5":
            print("Chao con adios")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()