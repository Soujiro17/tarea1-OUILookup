# Imports
try:
    import getopt
    import sys
    from getmac import get_mac_address
except ImportError:
    raise ImportError(
        'Error al importar una librería. Revise el archivo "requirements.txt" el cual contiene todos los complementos necesarios para una correcta ejecución del programa.')

# Cuerpo principal


def main():
    try:
        # para tener opciones largas, es necesario colocar las opciones cortas respectivas,
        # aunque no se utilicen. En este caso: -r y -m
        options, args = getopt.getopt(
            sys.argv[1:], "ip,mac", ['ip=', 'mac=', 'help'])
    except:
        print("Error: Parametros incorrectos.")
        uso()

    IP = None
    MAC = None

    for opt, arg in options:
        if opt in ('--help'):
            uso()
        if opt in ('--ip'):
            IP = arg
        elif opt in ('--mac'):
            MAC = arg

    # IP o MAC deben estar ingresadas.
    if IP == None and MAC == None:
        print("Error: Solo debe ingresar un parámetro (IP o MAC).")
        uso()

    # Ahora se pasa al programa
    MAC, Vendor = getVendor(IP, MAC)
    if(MAC == None):
        print(
            f'\n{Vendor}')
    else:
        print(
            f'\nMAC address  : {MAC}\nVendor       : {Vendor}')


def uso():
    print("Uso: " + sys.argv[0] +
          " --ip <ip>  --mac <mac> [--help] ")
    print("\nParametros:")
    print("     --ip: IP del dispositivo.")
    print("     --mac: MAC Address del dispositivo.")
    print("     --help: muestra esta pantalla y termina. Opcional")
    exit(1)


def getVendor(IP, MAC):
    if(IP != None and MAC == None):
        eth_mac = get_mac_address(ip=IP)
        if(eth_mac != None):
            eth_mac = eth_mac.upper()
            return eth_mac, solicitudDB(eth_mac)
        else:
            return eth_mac, "Error: ip is outside the host network"
    else:
        return MAC, solicitudDB(MAC)


def solicitudDB(MAC):
    MAC = MAC[:8]
    try:
        db = open("vendorsDB.txt", "r", encoding="utf8")
        db = db.readlines()
        for line in db:
            line = line.split("	")
            if(MAC == line[0]):
                return line[1]
            if(MAC == line[0].split("/")[0] and len(line) > 8):
                return line[1]
    except IOError:
        print("Archivo de DB no encontrado.")
    return "Not found"


# Esto se utiliza para poder importar este codigo en otro script para utilizar sus funciones.
if __name__ == '__main__':
    main()
