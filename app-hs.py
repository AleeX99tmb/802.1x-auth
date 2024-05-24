import subprocess

def ejecutar_tshark(nombre_archivo):
    # Ejecutar tshark para leer el archivo de captura
    comando = ["tshark", "-r", nombre_archivo]
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, _ = proceso.communicate()
    return salida.decode("utf-8")

def buscar_handshakes(salida_tshark):
    handshakes = {}
    lines = salida_tshark.split('\n')
    for line in lines:
        if "EAPOL" in line and "Key (Message" in line:
            campos = line.split()
            print(f"Mensaje encontrado: {line}")  # Imprimir el mensaje para depuración


if __name__ == "__main__":
    nombre_archivo = "allthedata-01.cap"
    salida_tshark = ejecutar_tshark(nombre_archivo)
    handshakes = buscar_handshakes(salida_tshark)
