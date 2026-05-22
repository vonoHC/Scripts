# Python

Repositorio de herramientas y scripts desarrollados en Python enfocados en redes, automatización y ciberseguridad.  
El objetivo del proyecto es reunir utilidades prácticas, educativas y escalables que puedan ampliarse con nuevos proyectos en el futuro.

---

# Contenido Actual

| Herramienta | Descripción |
|---|---|
| Escaner de puertos multihilo | Escáner de puertos TCP multihilo |
| Recolector de encabezados HTTP | Recolector y visualizador de headers HTTP |


---

# Proyectos

---

## Escaner de puertos multihilo

Escáner de puertos TCP desarrollado en Python utilizando multihilo para acelerar el proceso de análisis.

### Características

- Escaneo TCP
- Resolución automática de dominios
- Detección de servicios conocidos
- Soporte multihilo mediante `ThreadPoolExecutor`
- Configuración de timeout
- Interfaz CLI con `argparse`

---

## Recolector de encabezados HTTP

Herramienta para obtener y visualizar encabezados HTTP de sitios web.

### Características

- Obtención de headers HTTP
- Consulta individual de valores
- Exportación a archivos `.txt`
- Interfaz interactiva en terminal

### Tecnologías

- Python
- Requests
- Contextlib

### Tecnologías

- Python
- Socket
- Concurrent Futures
- Argparse

---

# Instalación

Clona el repositorio:

```
git clone https://github.com/usuario/python-cybersecurity-scripts.git
cd python-cybersecurity-scripts
```

Instala las dependencias:

```
pip install -r requirements.txt
```

---

# Estructura del Proyecto

```
Python/
│
├── Escaner de puertos multihilo/
│   ├── main.py
│   └── README.md
│
├── Recolector de encabezados HTTP/
│   ├── scanner.py
│   └── README.md
|
├── requirements.txt
└── README.md
```

---

# Objetivos del Repositorio

- Centralizar herramientas desarrolladas en Python
- Practicar conceptos de redes y ciberseguridad
- Mejorar habilidades de programación y automatización
- Crear proyectos escalables y reutilizables
- Mantener una colección organizada de utilidades técnicas

---

# Futuras Herramientas

Algunos proyectos que podrían añadirse más adelante:

- Banner Grabber
- DNS Resolver
- Packet Sniffer
- Subdomain Scanner
- Web Directory Scanner
- Hash Cracker
- Network Monitoring Tools

---

# Requisitos

- Python 3.x

