import os
import shutil
import time

# Diccionario con las diferentes configuraciones
configuraciones = {
    'WEP': 'wep.conf',
    'MAC': 'mac.conf',
    'WPA2': 'wpa2.conf',
    'WPA3': 'wpa3.conf',
    'MSCHAPV2': 'mschapv2.conf',
    'EAP RADIUS PEAP': 'eapradius.conf',
    'EAP RADIUS TTLS': 'eapradius.conf',
    'EAP TLS certificate': 'eaptls.conf'
}

# Ruta archivo de configuracion de hostapd
hostapd_conf_path = '/etc/hostapd/hostapd.conf'

# Ruta a los archivos de configuracion
config_path = '/home/alex/configuraciones/'

def aplicar_configuracion(opcion):
    # Copia el archivo de configuracion seleccionado de configuraciones a hostapd.conf 
    config_file = configuraciones[opcion]
    config_full_path = os.path.join(config_path, config_file)
    shutil.copy(config_full_path, hostapd_conf_path)
    print(f"Configuración {opcion} aplicada.")

    # Inicia hostapd
    os.system('sudo killall hostapd')
    os.system('sudo hostapd /etc/hostapd/hostapd.conf &')
    print("Hostapd iniciado.")

def iniciar_wireshark():
    os.system('sudo wireshark &')
    print("Wireshark iniciado.")

def main():
    iniciar_wireshark()
    for configuracion in configuraciones.keys():
        aplicar_configuracion(configuracion)
        time.sleep(20)
        os.system('sudo killall hostapd')
        print("Hostapd detenido.")
    print("Todas las configuraciones han sido aplicadas.")

if __name__ == '__main__':
    main()
