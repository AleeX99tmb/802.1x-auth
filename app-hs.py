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
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["airmon-ng", "start", "wlx00e04c093e49"])
   
    proceso_airodump = subprocess.Popen(["sudo", "airodump-ng", "-c", "11", "-w", "allthedata", "--bssid", "E8:9C:25:B0:C4:40", "wlx00e04c093e49"])
    time.sleep(120)
    proceso_airodump.terminate()
    proceso_airodump.wait()

    nombre_archivo = "allthedata-01.cap"
    salida_tshark = ejecutar_tshark(nombre_archivo)
    handshakes = buscar_handshakes(salida_tshark)
