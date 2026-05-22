import requests, subprocess, socket

def cls():
    subprocess.run("cls",shell=True)
    
class Wrapper:
    
    def __init__(self,url):
        self.url = url
        self.rq = self.r()
        self.heads = self.__getHeaders()
        
    def r(self):
        rq = requests.get(self.url) 
        return rq
    
    def __getHeaders(self):
        headers = self.rq.headers
        i = 1
        heads = {}
        for h in headers.keys():
            heads.update({i:h})
            i += 1
        return heads
    
    def printHeaders(self):
        print()
        print(" ---        ---------------------------")
        print("| # |      |           Value            |")
        print(" ---        ---------------------------")
        print(str(self.heads).replace("{", " ").replace("}", "").replace(",","\n").replace(" '"," ").replace("'","").replace(":","-->").replace(" ","").replace("-->","    -->   "))
        print()
        
    def printHeaderValue(self,headerNumber):
        print()
        headerValue = self.rq.headers[self.heads[headerNumber]]
        print(f"Header '{self.heads[headerNumber]}':\n\n{headerValue}") 
        print()
        




cls()
print("  ==============================")
print("|   Recolector de HTTP Headers    |")
print("  ==============================\n")

while True:
    url = input("[-] Ingrese el URL objetivo: ")
    try:
        rq = Wrapper(url)
        break
    except:
        print("[!] URL no valida.")

cls()
print("  ==============================")
print("|   Recolector de HTTP Headers   |")
print("  ==============================\n")
print("[!] Bienvenido! \n\n[!] Escriba ? para ver la ayuda.")
    
while True:
    try:
        print("wrapper@wrapper:~$ ",end="")
        comando = input()
        match  comando.lower().replace(" ",""):
            case "?":
                print("\n? - Ver Comandos dispnibles.\nshow heads - Ver los Heads de respuesta de la pagina objetivo.\nshow hvals - Ver el valor del Head especificado.\ncls | clear - Limpia la pantalla.\n")
            case "showheads":
                rq.printHeaders()
            case "showheadsval":
                h = int(input("[-] Ingrese el numero de Header a consultar: "))
                rq.printHeaderValue(h)
            case "clear" | "cls":
                cls()
            case _ :
                raise ValueError("[!] Comando desconocido.")
    except ValueError:
        print("[!] Ingrese un comando valido.")
                
                
    
