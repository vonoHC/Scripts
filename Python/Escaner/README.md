# Escaner de Puertos

```python
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def sock(ip,port):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    resultado = cliente.connect_ex((ip,port))
    if not resultado:
        print(f"[+] Puerto {port} en {ip} abierto.")
    cliente.close()
    
ip = input("Ingrese la IP a escanear: ")
ports = int(input("\nIngrese el puerto limite que desea escanear: "))
print()
    
with ThreadPoolExecutor(max_workers=100) as ejecutor:
    ejecutor.map(lambda p: sock(ip,p), range(1,ports + 1))  
print()
```
