def solicitudDB(mac):
    mac = mac[:8]
    try:
        db = open("vendorsDB.txt", "r", encoding="utf8")
        db = db.readlines()
        for line in db:
            line = line.split(" ")
    except IOError:
        print("Archivo de DB no encontrado.")
    finally:
        db.close()

    '''resp = requests.get(
        "http://standards.ieee.org/develop/regauth/oui/oui.txt")
    resp = resp.text
    with open("vendorsDB.txt", "w", encoding="utf8") as f:
        for line in resp:
            f.write(line)
            count += 1'''
