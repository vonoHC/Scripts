# Escáner de Puertos
```python
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def sock(ip,port):

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(1)
    resultado = cliente.connect_ex((ip,port))
    if resultado == 0:
        banner = "No Banner."
        try:
            banner = cliente.recv(1024)
            if banner:
                banner = f"     {banner.decode('utf-8',errors='ignore').replace("\r", "").replace("\n", " ")}"
        except socket.timeout:
           pass
        cliente.close()
        return (port,banner)
    cliente.close()
    return
    
def main():
    
    parser = argparse.ArgumentParser(description="Escaner de puertos multihilo.")

    parser.add_argument("-ip", "--ip", type=str, required=True, help="Direccion IP del objetivo.")
    parser.add_argument("-p", "--puertos", type=int, required=True, help="Numero de puertos a escanear.")
    parser.add_argument("-t", "--hilos", type=int, required=True, help="Numero de hilos.")

    args = parser.parse_args()

    ip = args.ip
    puertos = args.puertos
    hilos = args.hilos

    print(f"\n[-] Iniciando escaneo en {ip} desde el puerto 1 al {puertos}...\n")

    with ThreadPoolExecutor(max_workers=hilos or 100) as ejecutor:
        resultado = ejecutor.map(lambda p: sock(ip,p), range(1,puertos + 1))  

    resultado = list(resultado)
    resultado = [port for port in resultado if port != None]
    resultado.sort(key=lambda x: x[0])
    

    for port,banner in resultado:
        print(f"[+] Puerto {port:<5} abierto | {banner}")

    
    print(f"\n[-] Escaneo a {ip} finalizado con {len(resultado)} puertos abiertos.\n")
    ```

    

    

if __name__ == "__main__":
    main()


