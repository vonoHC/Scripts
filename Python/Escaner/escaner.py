import socket as sc,argparse
from concurrent.futures import ThreadPoolExecutor

def socket_tcp(ip,port):
    ip = str(sc.gethostbyname(ip))
    cliente = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    cliente.settimeout(1)
    resultado = cliente.connect_ex((ip,port))
    cliente.close()
    if resultado == 0:
        print(f"[+] Puerto {port} abierto.")
        return port
    return

def socket_udp(ip,port):
    ip = str(sc.gethostbyname(ip))
    cliente = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)
    cliente.settimeout(1)
    cliente.sendto(b"hola",(ip,port))
    try:
        resultado = cliente.recvfrom(1024)
        cliente.close()
        print(f"[+] Puerto {port} respondio.")
        return port
    except:
        pass
    return

def main():
  
    parser = argparse.ArgumentParser(description="Escaner de Puertos Multihilo.")
    host = parser.add_mutually_exclusive_group(required=True)
    puerto = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("-t","--hilos",type=int,required=False,help="Numero de hilos. Ej. -t 100\nPor Defecto: '1000'",default=1000)
    parser.add_argument("-to","--timeout",type=int,required=False,help="Numero de hilos. Ej. -to 1\nPor Defecto: '1'",default=0.5)
    parser.add_argument("-u","--udp",required=False,help="Escaneo UDP. Ej. -u ...",action="store_true")

    host.add_argument("-ip","--ip",type=str,help="Direccion IP del Host Objetivo. Ej. -ip 192.168.0.10")
    host.add_argument("-d","--domain",type=str,help="Nombre de Dominio del Host Objetivo. Ej. -d example.com")

    puerto.add_argument("-mp","--maxport",type=int,required=False,help="Puerto Maximo a Escanear. Ej. -mp 65535",default=None)
    puerto.add_argument("-p","--port",type=str,required=False,help="Puertos Especificos a Escanear. Separados por coma, Ej. -p 21,22,80",default=None)
    puerto.add_argument("-pr","--portrange",type=str,required=False,help="Rago de Puertos Especificos a Escanear. Indicado por guion, Ej. -pr 22-80",default=None)

    args = parser.parse_args()
    hilos = args.hilos
    timeout = args.timeout
    udp = args.udp
    ip = args.ip
    domain = args.domain
    maxPort = args.maxport
    port = args.port
    portRange = args.portrange
    
  
    if udp:
        funcion = socket_udp; tlp = "UDP"
    else:
        funcion = socket_tcp; tlp = "TCP"

    print()
    if port:
        print(f"[-] Iniciando escaneo {tlp} a {ip or domain} en los puertos {port}.")
    elif maxPort:
        print(f"[-] Iniciando escaneo {tlp} a {ip or domain} hasta el puerto {maxPort}.")
    elif portRange:
        print(f"[-] Iniciando escaneo {tlp} a {ip or domain} en el rango {portRange}.")
    print()
        
    with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
        if maxPort:
            resultado = ejecutor.map(lambda p: funcion(ip or domain,p), range(1,maxPort + 1))
        elif port:
             port = [int(p) for p in port.split(",")]
             resultado = ejecutor.map(lambda p: funcion(ip or domain,p), port)
        elif portRange:
            portRange = [int(p) for p in portRange.split("-")]
            resultado = ejecutor.map(lambda p: funcion(ip or domain,p), range(portRange[0],portRange[1] + 1))
    
    resultado = list(resultado); resultado = [p for p in resultado if p != None]; resultado.sort()

    print(f"\n[-] Escaneo a {ip or domain} finalizado con {len(resultado)} puertos abiertos.\n")

if __name__ == "__main__":  
    main()
