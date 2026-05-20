import socket as sc,argparse
from concurrent.futures import ThreadPoolExecutor

def socket(ip,port):
    ip = str(sc.gethostbyname(ip))
    cliente = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    cliente.settimeout(1)
    resultado = cliente.connect_ex((ip,port))
    cliente.close()
    if resultado == 0:
        print(f"[+] Puerto {port} abierto.")
      return

def main():
  
    parser = argparse.ArgumentParser(description="Escaner de Puertos Multihilo.")
    host = parser.add_mutually_exclusive_group(required=True)
    puerto = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("-t","--hilos",type=int,required=False,help="Numero de hilos. Ej. -t 100",default=1000)

    host.add_argument("-ip","--ip",type=str,help="Direccion IP del Host Objetivo. Ej. -ip 192.168.0.10")
    host.add_argument("-d","--domain",type=str,help="Nombre de Dominio del Host Objetivo. Ej. -d host.com")

    puerto.add_argument("-mp","--maxport",type=int,required=False,help="Puerto Maximo a Escanear. Ej. -mp 65535",default=None)
    puerto.add_argument("-p","--port",type=str,required=False,help="Puertos Especificos a Escanear. Separados por coma, Ej. -p 21,22,80",default=None)
    puerto.add_argument("-pr","--portrange",type=str,required=False,help="Rago de Puertos Especificos a Escanear. Indicado por guion, Ej. -pr 22-80",default=None)

    args = parser.parse_args()
    ip = args.ip
    domain = args.domain
    maxPort = args.maxport
    port = args.port
    portRange = args.portrange
    hilos = args.hilos
  
    if port:
        print(f"[-] Iniciando escaneo a {ip or domain} en los puertos {port}")
    elif maxPort:
        print(f"[-] Iniciando escaneo a {ip or domain} hasta el puerto {maxPort}.")
    elif portRange:
        print(f"[-] Iniciando escaneo a {ip or domain} en el rango {portRange}.")
    print()
        
    with ThreadPoolExecutor(max_workers=hilos) as ejecutor:
        if maxPort:
            ejecutor.map(lambda p: socket(ip or domain,p), range(1,maxPort + 1))
        elif port:
             port = [int(p) for p in port.split(",")]
             ejecutor.map(lambda p: socket(ip or domain,p), port)
        elif portRange:
            portRange = [int(p) for p in portRange.split("-")]
            ejecutor.map(lambda p: socket(ip or domain,p), range(portRange[0],portRange[1] + 1))
    
    print(f"\n[-] Escaneo a {ip or domain} finalizado.\n")

main()
    

