# IP Query Tool

Herramienta desarrollada en Python para consultar información detallada sobre direcciones IP, dominios o redes utilizando la API de `ip.guide`.

## Características

- Consulta información de red.
- Obtiene datos de ubicación geográfica.
- Muestra información del sistema autónomo (ASN).
- Exporta resultados a un archivo local.
- Compatible con:
  - Direcciones IP
  - Dominios
  - Redes CIDR

---

# Requisitos

- Python 3.8+
- Librería `requests`

Instalación de dependencias:

```
pip install requests
```

---

# Uso

## Sintaxis

```
python IPconsulter.py [opciones]
```

---

# Opciones disponibles

| Opción | Descripción |
|---|---|
| `-i`, `--host` | Dirección IP, dominio o red objetivo |
| `-a`, `--all` | Muestra toda la información |
| `-n`, `--network` | Muestra únicamente información de red |
| `-l`, `--location` | Muestra únicamente información de ubicación |
| `-f`, `--file` | Exporta la salida a un archivo |

---

# Ejemplos

## Consultar toda la información de una IP

```
python IPconsulter.py -i 8.8.8.8 -a
```

---

## Consultar únicamente información de red

```
python IPconsulter.py -i 1.1.1.1 -n
```

---

## Consultar ubicación geográfica

```
python IPconsulter.py -i google.com -l
```

---

## Exportar resultados a un archivo

```
python IPconsulter.py -i 8.8.8.8 -a -f resultado.txt
```

---

# Información obtenida

## Información de red

- CIDR
- IP inicial y final
- ASN
- Organización
- País
- RIR

## Información de ubicación

- Ciudad
- País
- Zona horaria
- Coordenadas geográficas

---

# Ejemplo de salida

```text
Direccion IP: 8.8.8.8

RED:
  -CIDR: 8.8.8.0/24
  -IP inicial: 8.8.8.0
  -IP final: 8.8.8.255

Sistema autonomo:
  -ASN: 15169
  -Nombre: GOOGLE
  -Empresa: Google LLC
  -Pais: US
  -RIR: ARIN

Ubicacion:
  -Ciudad: Mountain View
  -Pais: United States
  -Zona de tiempo: America/Los_Angeles

[*] Consulta a 8.8.8.8 finalizada con exito.
```

---

# Estructura del proyecto

```text
.
├── IPconsulter.py
└── README.md
```

---

# API utilizada

Este proyecto utiliza la API pública de:

- https://ip.guide

---

# Implementaciones futuras

- Manejo de excepciones más detallado.
- Colores en terminal.
- Interfaz gráfica.
- Consultas masivas desde archivos.
