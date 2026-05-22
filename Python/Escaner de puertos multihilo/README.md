# ⚡ Escáner de Puertos Multihilo en Python

Herramienta de escaneo de puertos desarrollada en Python, diseñada para realizar análisis rápidos sobre hosts remotos usando múltiples hilos, con soporte para TCP y UDP, resolución automática de dominios y detección del nombre del servicio asociado a cada puerto.

---

# ✨ Características principales

- 🚀 Escaneo multihilo para mayor velocidad.
- 🌐 Soporte para protocolos TCP y UDP.
- 🎯 Escaneo de puertos específicos.
- 📡 Escaneo por rango de puertos.
- 🔎 Resolución automática de dominios a IP.
- 🧠 Detección automática del servicio asociado al puerto.
- ⏱️ Timeout configurable.
- 🖥️ Compatible con IPs y dominios.
- 📋 Resultados ordenados y fáciles de leer.

---

# 📌 Requisitos

- Python 3.x

El proyecto utiliza únicamente módulos estándar de Python:

- `socket`
- `argparse`
- `concurrent.futures`

No requiere instalación de dependencias externas.

---

# 🚀 Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

Ejecutar el script:

```bash
python3 escaner.py
```

---

# 🛠️ Uso

## Escanear puertos específicos

```bash
python3 escaner.py -i 192.168.1.10 -p 21,22,80
```

## Escanear un rango de puertos

```bash
python3 escaner.py -i 192.168.1.10 -r 1024
```

## Escaneo UDP

```bash
python3 escaner.py -i 192.168.1.10 -p 53,123,161 -u
```

## Aumentar número de hilos

```bash
python3 escaner.py -i 192.168.1.10 -r 65535 -t 200
```

## Cambiar timeout

```bash
python3 escaner.py -i 192.168.1.10 -r 1000 -tm 0.5
```

---

# ⚙️ Argumentos

| Argumento | Descripción |
|---|---|
| `-i`, `--host` | IP o dominio objetivo |
| `-p`, `--port` | Puertos específicos separados por coma |
| `-r`, `--portrange` | Escanea desde el puerto 1 hasta el puerto indicado |
| `-u`, `--udp` | Activa el escaneo UDP |
| `-t`, `--hilos` | Número de hilos a utilizar |
| `-tm`, `--timeout` | Tiempo límite de espera |
| `-b`, `--bannergrapper` | Opción reservada para banner grabbing |

---

# 📤 Ejemplo de salida

```bash
[-] Iniciando escaneo TCP a 192.168.1.10 en los puertos 21,22,80.

[+] 21   /ftp             [ABIERTO]
[+] 22   /ssh             [ABIERTO]
[+] 80   /http            [ABIERTO]

[-] Escaneo a 192.168.1.10 finalizado con 3 puertos abiertos.
```

---

# 🔍 Funcionamiento

El escáner realiza los siguientes pasos:

1. Resuelve automáticamente el dominio a una dirección IP.
2. Selecciona el modo TCP o UDP.
3. Genera múltiples hilos usando `ThreadPoolExecutor`.
4. Envía conexiones simultáneas a los puertos objetivo.
5. Detecta puertos abiertos y muestra el servicio asociado.

---

# 📘 Notas

- TCP utiliza `connect_ex()` para verificar conexiones abiertas.
- UDP envía un paquete y espera respuesta.
- Algunos puertos UDP pueden no responder aunque estén abiertos.
- Los resultados se muestran ordenados al finalizar el escaneo.
- La opción `--bannergrapper` aún no está implementada.

---

# 🧠 Tecnologías utilizadas

- Python 3
- Socket Programming
- Multithreading
- ThreadPoolExecutor

