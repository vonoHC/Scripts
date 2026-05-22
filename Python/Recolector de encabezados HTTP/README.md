# Recolector de encabezados HTTP

Herramienta desarrollada en Python para recolectar y visualizar encabezados HTTP de cualquier sitio web.  
Permite consultar headers, ver sus valores individuales y exportarlos a un archivo local desde una interfaz interactiva en terminal.

---

## Características

- Obtención de headers HTTP mediante `requests`
- Visualización organizada en formato tabla
- Consulta individual del valor de cada header
- Exportación de headers a archivos `.txt`
- Interfaz interactiva desde consola
- Limpieza de terminal integrada
- Compatible con URLs y direcciones IP

---

## Vista previa

```
  ==============================================
||          Recolector de Headers HTTP          ||
  ==============================================

[*] Ingrese la URL a consultar: https://example.com
```

```
guest@wrapper:~$ show heads

 -----------------------------------------
| Numero  |          Encabezado           |
 -----------------------------------------
| #0      |    Date                       |
 -----------------------------------------
| #1      |    Content-Type               |
 -----------------------------------------
| #2      |    Server                     |
 -----------------------------------------
```

---

## Requisitos

- Python 3.x
- Librería `requests`

---

## Instalación

Clona el repositorio:

```
git clone https://github.com/usuario/header-wrapper.git
cd header-wrapper
```

Instala las dependencias:

```
pip install requests
```

---

## Uso

Ejecuta el programa:

```
python HTTPGrabber.py
```

Luego ingresa una URL válida:

```
https://example.com
```

o

```
http://192.168.1.1
```

---

## Comandos Disponibles

| Comando | Descripción |
|---|---|
| `?` | Muestra los comandos disponibles |
| `show heads` | Lista todos los headers encontrados |
| `show headval` | Muestra el valor de un header específico |
| `export heads` | Exporta los headers a un archivo |
| `cls` / `clear` | Limpia la terminal |
| `ls` / `dir` | Muestra el contenido del directorio actual |

---

## Exportación de Headers

El programa permite guardar los encabezados HTTP en un archivo local:

```
guest@wrapper:~$ export heads
```

Ejemplo:

```
headers.txt
```

---

## Tecnologías Utilizadas

- Python
- Requests
- Contextlib
- Subprocess

---

## Estructura del Proyecto

```
header-wrapper/
│
├── main.py
└── README.md
```
---
