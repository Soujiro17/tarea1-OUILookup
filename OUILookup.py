# Imports
try:
    from getmac import get_mac_address
    import argparse
    import warnings
except ImportError:
    raise ImportError(
        'Error al importar una librería. Revise el archivo "requirements.txt" el cual contiene todos los complementos para una correcta ejecución del programa.')


# ARGP
parser = argparse.ArgumentParser()

# Configuración parámetros
parser.add_argument("--ip", help="specify the IP of the host to query.")
parser.add_argument("--mac", help="specify the MAC address to query.")

# Cerrar
args = parser.parse_args()

# Funciones


def solicitudDB(mac):
    mac = mac[:8]
    try:
        db = open("vendorsDB.txt", "r", encoding="utf8")
        db = db.readlines()
        for line in db:
            line = line.split("	")
            if(mac == line[0]):
                return line[1]
    except IOError:
        print("Archivo de DB no encontrado.")
    return "Not found"


# Condiciones de None
if(args.ip != None):
    eth_mac = get_mac_address(ip=args.ip).upper()
    if(eth_mac != None):
        print(
            f'\nMAC address  : {eth_mac}\nVendor       : {solicitudDB(eth_mac)}')
    else:
        print("Error: ip is outside the host network")
if(args.mac != None):
    pass
    #win_mac = get_mac_address(interface="Ethernet 1")
    #ip_mac = get_mac_address(ip="192.168.0.1")
    #ip6_mac = get_mac_address(ip6="::1")
    #host_mac = get_mac_address(hostname="localhost")
    #updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)
    # print(f'{eth_mac}\n{win_mac}\n{ip_mac}\n{ip6_mac}\n{host_mac}\n{updated_mac}\n')
#print("Para ver la lista de parámetros ejecute el nombre del programa seguido del parámetro -h.")
