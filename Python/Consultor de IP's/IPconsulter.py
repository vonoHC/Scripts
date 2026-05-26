import requests, argparse, contextlib

class IP:
    def __init__(self,ip=""):
        self.ip = ip
        self.consulta = self.solicitud()
        self.contenido = self.__content()
        
    def solicitud(self):
        consulta = requests.get(f"https://ip.guide/{self.ip}")
        return consulta
    
    def __content(self):
        return self.consulta.json()
    
    def getNetInfo(self):
        print(f"\nDireccion IP: {self.contenido["ip"]}\n")
        print(f"RED:")
        print(f"  -CIDR: {self.contenido["network"]["cidr"]}")
        print(f"  -IP inicial: {self.contenido["network"]["hosts"]["start"]}")
        print(f"  -IP final: {self.contenido["network"]["hosts"]["end"]}\n")
        print(f"  Sistema autonomo:")
        print(f"    -ASN: {self.contenido["network"]["autonomous_system"]["asn"]}")
        print(f"    -Nombre: {self.contenido["network"]["autonomous_system"]["name"]}")
        print(f"    -Empresa: {self.contenido["network"]["autonomous_system"]["organization"]}")
        print(f"    -Pais: {self.contenido["network"]["autonomous_system"]["country"]}")
        print(f"    -RIR: {self.contenido["network"]["autonomous_system"]["rir"]}\n")
        
    def getLocationInfo(self):
        print(f"\nDireccion IP: {self.contenido["ip"]}\n")
        print(f"\nUbicacion:")
        print(f"  -Ciudad: {self.contenido["location"]["city"]}")
        print(f"  -Pais: {self.contenido["location"]["country"]}")
        print(f"  -Zona de tiempo: {self.contenido["location"]["timezone"]}")
        print(f"  Coordenadas:")
        print(f"    -Latitud: {self.contenido["location"]["latitude"]}")
        print(f"    -Longitud: {self.contenido["location"]["longitude"]}\n")

    def getAllInfo(self):
        print(f"\nDireccion IP: {self.contenido["ip"]}\n")
        print(f"RED:")
        print(f"  -CIDR: {self.contenido["network"]["cidr"]}")
        print(f"  -IP inicial: {self.contenido["network"]["hosts"]["start"]}")
        print(f"  -IP final: {self.contenido["network"]["hosts"]["end"]}\n")
        print(f"  Sistema autonomo:")
        print(f"    -ASN: {self.contenido["network"]["autonomous_system"]["asn"]}")
        print(f"    -Nombre: {self.contenido["network"]["autonomous_system"]["name"]}")
        print(f"    -Empresa: {self.contenido["network"]["autonomous_system"]["organization"]}")
        print(f"    -Pais: {self.contenido["network"]["autonomous_system"]["country"]}")
        print(f"    -RIR: {self.contenido["network"]["autonomous_system"]["rir"]}\n")
        print(f"Ubicacion:")
        print(f"  -Ciudad: {self.contenido["location"]["city"]}")
        print(f"  -Pais: {self.contenido["location"]["country"]}")
        print(f"  -Zona de tiempo: {self.contenido["location"]["timezone"]}")
        print(f"  Coordenadas:")
        print(f"    -Latitud: {self.contenido["location"]["latitude"]}")
        print(f"    -Longitud: {self.contenido["location"]["longitude"]}\n")
        
    def getIP(self):
        return self.contenido["ip"]
    
    def exportInfo(self,file):
        with open(file,"w") as file:
            with contextlib.redirect_stdout(file):
                self.getAllInfo()

def main():
    parser = argparse.ArgumentParser(description="Consultor de IP's")
    
    info = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("-i","--host",type=str,required=False,help="Direccion IP, Nombre de dominio o Red objetivo. Si no se indica algun host se consultara la IP propia.")
    info.add_argument("-a","--all",help="Muestra toda la informacion obtenida sobre el objetivo.",action="store_true")
    info.add_argument("-n","--network",help="Muestra exclusivamente la informacion relacionada con la red del objetivo.",action="store_true")
    info.add_argument("-l","--location",help="Muestra exclusivamente la informacion relacionada con la locacion del objetivo.",action="store_true",)
    parser.add_argument("-f","--file",type=str,required=False,help="Indica el archivo local para exportar la salida.")
    
    
    args = parser.parse_args()
    
    host = args.host
    onlyNetwork = args.network
    onlyLocation = args.location
    allInfo = args.all
    exportFile = args.file
    
    try:
        if host:
            consulta = IP(host)
        else:
            consulta = IP()
    
    
        if allInfo:
            funcion = consulta.getAllInfo()
        elif onlyNetwork:
            funcion = consulta.getNetInfo()
        elif onlyLocation:
            funcion = consulta.getLocationInfo()
            
        if exportFile:
            funcion
            consulta.exportInfo(exportFile)
        else:
            funcion
        
        print(f"\n[*] Consulta a {host or consulta.getIP()} finalizada con exito.\n")
        
    except:
        print("\n[!] Objetivo invalido. Ingrese una red, una direccion IP o nombre de dominio.\n")
        
if __name__ == "__main__":
    main()
    
    
    
