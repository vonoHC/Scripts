# Escáner de Puertos Multihilo en Python

Escáner de puertos hecho en Python usando `socket`, `argparse` y `ThreadPoolExecutor`.  
El objetivo del proyecto es tener una herramienta rápida, flexible y fácil de usar desde la terminal.

---

## ¿Qué puede hacer?

- Escaneo multihilo para acelerar el proceso.
- Resolución automática de dominios (`example.com → IP`).
- Soporte para:
  - Puertos específicos.
  - Rangos de puertos.
  - Escaneo hasta un puerto máximo.
- Permite elegir si el objetivo será:
  - una IP
  - o un dominio.
- Posibilidad de definir la cantidad de hilos.
- Todo configurable directamente desde la terminal gracias a `argparse`.

---

# Tecnologías utilizadas

- Python 3
- Socket
- Argparse
- Concurrent.futures

---

# Cómo funciona

El script crea múltiples hilos usando el modulo `ThreadPoolExecutor` de `concurrent.futures` para intentar conexiones TCP a distintos puertos al mismo tiempo. Cada puerto abierto se muestra automáticamente en pantalla durante el escaneo.

---

# Uso

## Escanear usando una IP

```bash
python3 escaner.py -ip 192.168.0.10 -mp 1000
```

## Escanear usando un dominio

```bash
python3 escaner.py -d example.com -mp 1000
```

---

# Argumentos disponibles

| Argumento | Descripción |
|---|---|
| `-ip` / `--ip` | IP objetivo |
| `-d` / `--domain` | Dominio objetivo |
| `-t` / `--hilos` | Cantidad de hilos |
| `-mp` / `--maxport` | Escanea desde el puerto 1 hasta el indicado |
| `-p` / `--port` | Puertos específicos separados por coma |
| `-pr` / `--portrange` | Rango de puertos |

---

# Ejemplos

## Puertos específicos

```bash
python3 escaner.py -ip 192.168.0.10 -p 21,22,80,443
```

## Rango de puertos

```bash
python3 escaner.py -d example.com -pr 20-100
```

## Escaneo completo hasta un puerto máximo

```bash
python3 escaner.py -ip 192.168.0.10 -mp 65535
```

## Cambiando la cantidad de hilos

```bash
python3 escaner.py -ip 192.168.0.10 -mp 1000 -t 500
```
### Escaneo UDP
```bash
python3 escaner.py -ip 192.168.0.10 -mp 1000 -u
```

---

# Ejemplo de salida

```text
[-] Iniciando escaneo TCP a example.com hasta el puerto 1000.

[+] Puerto 80 abierto.
[+] Puerto 443 abierto.

[-] Escaneo a example.com finalizado con 2 puertos abiertos.
```

---

# Estructura

```text
.
├── escaner.py
└── README.md
```

# Próximas implementaciones
* **Recolección de Banners**: para obtener información sobre el servicio y la versión activa en el puerto escaneado.
* **Exportación en formato JSON**: para almacenar los resultados del escaneo en un formato flexible.
* **Implementación completa del escaneo UDP**: aunque actualmente este modo hace su función (enviar datos y esperar una respuesta para deducir el estado de un puerto), por la naturaleza del protocolo UDP es necesario enviar los datos en un formato específico para el servicio activo en cada puerto con el fin de conocer con precisión su estado.
