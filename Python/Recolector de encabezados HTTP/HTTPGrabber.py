import requests,contextlib, subprocess

def cls():
    subprocess.run("cls",shell=True)


class Wrapper:
    def __init__(self,url):
        self.url = url
        self.request = self.rq()
        self.headers = self.__getHeaders()

    def rq(self):
        request = requests.get(self.url)
        return request
    
    def __getHeaders(self):
        heads = self.request.headers
        headers_list = []
        for i,j in heads.items():
            headers_list.append((i,j))
        return headers_list

    
    def printHeaders(self):
        print()
        print(f" -----------------------------------------")
        print(f"| Numero  |          Encabezado           |")
        print(f" -----------------------------------------")
        for i in self.headers:
            print(f"| #{self.headers.index(i):<7}|    {i[0]:<27}|")
            print(f" -----------------------------------------")
        print()

    def getHeaderValue(self,header):
        h = self.headers[header]
        print()
        print(f"[{h[0]}]:\n")
        print(f"'{h[1]}'\n")
    
    def exportFile(self,file):
        with open(file,"w") as file:
            with contextlib.redirect_stdout(file):
                self.printHeaders()
    
        

def main():
    cls()
    print("  ==============================================")
    print("||          Recolector de Headers HTTP          ||")
    print("  ==============================================")
    
    while True:
        try:
            url = input("\n[*] Ingrese la URL a consultar: ")
            solicitud = Wrapper(url)
            break
        except:
            print("\n[!] URL invalida; Formato admitido: http(s)://example.com | http(s)://xxx.xxx.xxx.xxx")
    cls()
    print("  ------------------------------ ")
    print("|          Bienvenido!           |")
    print("  ------------------------------ ")
    print("\n[*] Escriba '?' para ver los comandos disponibles.")
    print()
    while True:
        print("guest@wrapper:~$ ",end="")
        comando = input()
        match comando.lower().replace(" ",""):
            case "?":
                print("\n'?' - Muestra los comandos disponibles.\n'show heads' - Muestra los headers de respuesta de la web indicada.\n'show headval' - Muestra el valor del header indicado.\n'export heads' - Guarda los headers de respuesta en un archivo local.\n'cls' | 'clear' - Limpia la terminal.\n'ls | dir' - Muestra el contenido del directorio actual en el sistema.")
            case "showheads":
                solicitud.printHeaders()
            case "showheadval":
                head = int(input("\n[*] Indique el numero de header a consultar: "))
                try:
                    solicitud.getHeaderValue(head)
                except:
                    print("\n[!] Header no valido. Ingrese una de las opciones mostradas en la tabla de 'show heads'.")
            case "exportheads":
                file = input("\n[*] Indique el nombre del archivo: ")
                try:
                    solicitud.exportFile(file)
                    print(f"[+] {file} creado con exito.\n")
                except:
                    print("[!] Hubo un error al crear el archivo.\n")
            case "cls" | "clear":
                cls()
            case "ls" | "dir":
                try:
                    print()
                    subprocess.run("dir",shell=True)
                    print()
                except:
                    print("No se pudo mostrar el contenido del directorio actual en el sistema.")

            case _:
                print("\n[!] Opcion invalida. Use los comandos listados en '?'.\n")
            

if __name__ == "__main__":
    main()
