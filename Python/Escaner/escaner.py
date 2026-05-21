import socket as sc,argparse
from concurrent.futures import ThreadPoolExecutor,as_completed

def socket_tcp(ip,port,timeout,bannergrapper=""):
    cliente = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    cliente.settimeout(timeout)
    servicio = "Desconocido"
    try:
        servicio = sc.getservbyport(port,"tcp")
    except:
        pass
    try:
        resultado = cliente.connect_ex((ip,port))
        if resultado == 0:
            print(f"[+] {port:<5}/{servicio:<15} [ABIERTO]")
            return port
    except:
        pass
    finally:
        cliente.close()
    return

def socket_udp(ip,port,timeout):
    cliente = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)
    cliente.settimeout(timeout)
    servicio = "Desconocido"
    try:
        servicio = sc.getservbyport(port,"udp")
    except:
        pass
    try:
        cliente.sendto(b"hola",(ip,port))
        cliente.recvfrom(1024)
        print(f"[+] {port:<5}/{servicio:<15} [ABIERTO]")
        return port
    except:
        pass
    finally:
        cliente.close()
    return

def main():
  
    parser = argparse.ArgumentParser(description="Escaner de Puertos Multihilo.")
    puerto = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument("-t","--hilos",type=int,required=False,help="Numero de hilos.       Ej: -t 200;     Por Defecto: '100'",default=100)
    parser.add_argument("-tm","--timeout",type=float,required=False,help="Tiempo Limite.        Ej: -to 0.5;      Por Defecto: '0.3'",default=0.3)
    parser.add_argument("-u","--udp",required=False,help="Escaneo UDP.      Ej: -u ...",action="store_true")
    parser.add_argument("-b","--bannergrapper",required=False,help="Recolector de Banner.       Al activar esta opcion los resultados del escaneo seran mostrados al concluir el mismo.",action="store_true")
    
    parser.add_argument("-i","--host",type=str,required=True,help="IP/Dominio del Host Objetivo.        Ej. -ip 192.168.0.10 | -i example.com")

    puerto.add_argument("-r","--portrange",type=int,required=False,help="Rango de puerto a escanear.        Ej: -r 65535 (se escanearan los puertos desde 1 hasta 65535)",default=None)
    puerto.add_argument("-p","--port",type=str,required=False,help="Puertos Especificos a Escanear separados por coma.      Ej: -p 21,22,80",default=None)
  

    args = parser.parse_args()
    hilos = args.hilos
    timeout = args.timeout
    udp = args.udp
    host = args.host
    port = args.port
    portrange = args.portrange
    bannergrapper = args.bannergrapper

    try:
        host = sc.gethostbyname(host)
    except:
        print(f"\n[!] No se pudo resolver {host}\n")
        return
  
    if udp:
        funcion = socket_udp; tlp = "UDP"
    else:
        funcion = socket_tcp; tlp = "TCP"

    print()
    if port:
        print(f"[-] Iniciando escaneo {tlp} a {host} en los puertos {port}.")
    elif portrange:
        print(f"[-] Iniciando escaneo {tlp} a {host} hasta el puerto {portrange}.")
    print()

    resultado = []
        
    with ThreadPoolExecutor(max_workers=hilos) as ejecutor:

        if port:
            port = [int(p) for p in port.split(",")]
            futures = [ejecutor.submit(funcion,host,p,timeout) for p in port]

        elif portrange:
            futures = [ejecutor.submit(funcion,host,p,timeout) for p in range(1,portrange + 1)]

        for future in as_completed(futures):
            try:
                puerto = future.result()
                if puerto != None:
                    resultado.append(puerto)
            except:
                pass
    
    resultado.sort()

    print(f"\n[-] Escaneo a {host} finalizado con {len(resultado)} puertos abiertos.\n")

if __name__ == "__main__":  
    main()
