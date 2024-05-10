logo = """
 _____ _____  _____   __       
|  _  |  _  |/ __  \ /  |      
 \ V /| |/' |`' / /' `| |__  __
 / _ \|  /| |  / /    | |\ \/ /
| |_| \ |_/ /./ /__ __| |_>  < 
\_____/\___/ \_____(_)___/_/\_\ """ 
                         
print(logo)

import os # permite interactuar con el sistema operativo
import shutil # permite manipular carpetas y archivos

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
        os.system('sudo hostapd /etc/hostapd/hostapd.conf')
        print("Hostapd iniciado.")



def añadir_usuario_radius():
    username = input ("Introduce el nombre de usuario: ")
    password = input ("Introduce la contraseña: ")

    radius_users_path = '/etc/freeradius/3.0/users'

    nueva_linea = f"{username} Cleartext-Password := \"{password}\"\n"

    try: 
        with open(radius_users_path, 'r+') as file:
            lineas_existentes = file.readlines()
            file.seek(0)
            file.write(nueva_linea)
            file.writelines(lineas_existentes)

        os.system('sudo systemctl restart freeradius')

        print(f"Usuario {username} añadido a RADIUS.")

    except Exception as e:
        print(f"Error al añadir el usuario a RADIUS: {e}")



def añadir_mac():
    mac_address = input("Introduce la dirección MAC: ")

    macs_path = '/home/alex/macs/accept_mac.txt'

    nueva_linea = f"{mac_address}\n"

    try: 
        with open(macs_path, 'r+') as file:
            lineas_existentes = file.readlines()
            file.seek(0)
            file.write(nueva_linea)
            file.writelines(lineas_existentes)

    except Exception as e:
        print(f"Error al añadir dirección MAC: {e}")



def añadir_usuraio_mschapv2():
    username = input("Introduce el nombre de usuario:")
    password = input("Introduce la contraseña:")

    mschapv2_users_path = '/home/alex/configuraciones/eap_user2'

    nueva_linea = (
        f"# Phase 1 users\n"
        f"\"{username}\" PEAP\n\n"
        f"# Phase 2\n"
        f"\"{username}\" MSCHAPV2 \"{password}\" [2]\n"
        f"\n"
    )

    try: 
        with open(mschapv2_users_path, 'r+') as file:
            lineas_existentes = file.readlines()
            file.seek(0)
            file.write(nueva_linea)
            file.writelines(lineas_existentes)

    except Exception as e:
        print(f"Error al añadir usuario: {e}")
    


def añadir_certificado_tls():
    username = input("Introduce el nombre de nuevo usuario:  ")
    password = input("introduce la contraseña para cifrar el .rar con las claves:")

    base_path = '/home/alex/Descargas/'
    ca_path = '/home/alex/server/'

    client_key_path = os.path.join(base_path,f"{username}_key.pem")
    client_csr_path = os.path.join(base_path,f"{username}.csr")
    client_crt_path = os.path.join(base_path,f"{username}.crt")

    ca_cert_path = os.path.join(ca_path,'ca_cert.pem') 
    ca_key_path = os.path.join(ca_path,'ca_key.pem')

    # Generar clave privada para el cliente.
    os.system(f"openssl genpkey -algorithm RSA -out {client_key_path} -pkeyopt rsa_keygen_bits:2048")
    
    # Generar CSR para el cliente.
    os.system(f"openssl req -new -key {client_key_path} -out {client_csr_path} "
              f"-subj \"/CN={username}/O=Cliente/C=ES\"")
    
    # Firmar la CSR del cliente con la CA existente.
    os.system(f"openssl x509 -req -in {client_csr_path} -CA {ca_cert_path} "
              f"-CAkey {ca_key_path} -CAcreateserial -out {client_crt_path} "
              f"-days 365 -sha256")
    
    csr_path = os.path.join(base_path, f"{username}.csr")
    key_path = os.path.join(base_path, f"{username}_key.pem")
    crt_path = os.path.join(base_path, f"{username}.crt")

    rar_path = os.path.join(base_path, f"{username}.rar")
    os.remove(csr_path)
    os.system(f"rar a -p{password} {rar_path} {key_path} {crt_path}")
    os.remove(key_path)
    os.remove(crt_path)

    print(f"Certificado para {username} generado.")



def main():
    print("¿Que desea hacer?")
    print("1. Escoger método de autentificación")
    print("2. Añadir usuario a RADIUS")
    print("3. Añadir dirección MAC")
    print("4. Añadir usuario a MSCHAPv2")
    print("5. Añadir certificado TLS")
    print()
    
    opcion = input("Elige una opcion  ")

    if opcion == '1':
        print("Configuraciones disponibles:")
        for i, key in enumerate(configuraciones.keys()):
            print(f"{i + 1}. {key}")

        # Pide al usuario ue elija una configuracion
        opcion = input ("Elige una configuración: ")

        # Maneja la eleccion del usuario
        if opcion.isdigit():
            # Combierte el numero a indice
            opcion = int(opcion) - 1 
            if opcion < 0 or opcion >= len(configuraciones): # Si escoge 0 o mas de los que hay da opcion no valida
                print("Opción no válida.")
                return
            opcion = list(configuraciones.keys())[opcion]
        elif opcion not in configuraciones:
            print("Opción no válida.")
            return
        
        # Aplica la configuracion
        aplicar_configuracion(opcion)

    elif opcion == '2':
        añadir_usuario_radius()
    elif opcion == '3':
        añadir_mac()
    elif opcion == '4':
        añadir_usuraio_mschapv2()
    elif opcion == '5':
        añadir_certificado_tls()
    else:
        print("Opción no válida.")

if __name__ == '__main__':
    main()