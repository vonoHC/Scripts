# Escáner de Puertos

```python
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def sock(ip,port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    resultado = cliente.connect_ex((ip,port))
    if not resultado:
        print(f"[+] Puerto {port}:{ip} abierto.")
    cliente.close()
    


def main():
    
    parser = argparse.ArgumentParser(description="Escaner de puertos multihilo.")

    parser.add_argument("-ip", "--ip", type=str, required=True, help="Direccion IP del objetivo.")
    parser.add_argument("-p", "--puertos", type=int, required=True, help="Numero de puertos a escanear.")

    args = parser.parse_args()

    ip = args.ip
    puertos = args.puertos

    print(f"[-] Iniciando escaneo en {ip} desde el puerto 1 al {puertos}...\n")

    with ThreadPoolExecutor(max_workers=100) as ejecutor:
        ejecutor.map(lambda p: sock(ip,p), range(1,puertos + 1))  
    print(f"\n[-] Escaneo a {ip} finalizado.")

if __name__ == "__main__":
    main()
```
