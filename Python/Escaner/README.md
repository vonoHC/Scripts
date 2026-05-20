# Escáner de Puertos Multihilo en Python

Escáner de puertos hecho en Python usando `socket`, `argparse` y `ThreadPoolExecutor`.  
El objetivo del proyecto es tener una herramienta rápida, flexible y fácil de usar desde la terminal.

---

## ¿Qué puede hacer?

- Escaneo multihilo para acelerar el proceso.
- Resolución automática de dominios (`google.com → IP`).
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
- `socket`
- `argparse`
- `concurrent.futures`

---

# Cómo funciona

El script crea múltiples hilos usando `ThreadPoolExecutor` para intentar conexiones TCP a distintos puertos al mismo tiempo. Cada puerto abierto se muestra automáticamente en pantalla durante el escaneo.

---

# Uso

## Escanear usando una IP

```bash
python3 escaner.py -ip 192.168.0.10 -mp 1000
```

## Escanear usando un dominio

```bash
python3 escaner.py -d google.com -mp 1000
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
python3 escaner.py -ip 192.168.1.1 -p 21,22,80,443
```

## Rango de puertos

```bash
python3 escaner.py -d example.com -pr 20-100
```

## Escaneo completo hasta un puerto máximo

```bash
python3 escaner.py -ip 10.10.10.10 -mp 65535
```

## Cambiando la cantidad de hilos

```bash
python3 escaner.py -ip 192.168.0.5 -mp 1000 -t 500
```

---

# Ejemplo de salida

```text
[-] Iniciando escaneo a google.com hasta el puerto 1000.

[+] Puerto 80 abierto.
[+] Puerto 443 abierto.

[-] Escaneo a google.com finalizado.
```

---

# Estructura

```text
.
├── scanner.py
└── README.md
```
