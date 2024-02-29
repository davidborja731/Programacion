class telefonomovil:
    fabricante=""
    tamaño_pantalla=float
    numero_nucleos=int
    aplicaciones=[]
    estado=True or False #Bool es un true or false
    def __init__(self,fabricante,tamaño_pantalla,numero_nucleos) -> bool:
        self.fabricante=fabricante
        self.tamaño_pantalla=tamaño_pantalla
        self.numero_nucleos=numero_nucleos
        self.status=False  
    def power_on(self):
        if self.estado == False:
            self.estado=True
    def power_off(self):
        if self.estado == True:
            self.estado=False
    def install_app(self,aplicaciones):
        if aplicaciones not in self.aplicaciones:
            self.aplicaciones.append(aplicaciones)
    def uninstall_app(self,aplicaciones):
        if aplicaciones in self.aplicaciones:
            self.aplicaciones.remove(aplicaciones)
        else:
            print("No se puede desinstalar")
    def mostrar(self):
        print(f"{self.fabricante},{str(self.tamaño_pantalla)},{str(self.numero_nucleos)},{str(self.aplicaciones)},{str(self.estado)}")

movil=telefonomovil("Xiaomi",6.7,8)
movil.install_app("Google")
movil.install_app("Telegram")
movil.install_app("Whatshapp")
movil.uninstall_app("firefox")
movil.uninstall_app("Telegram")
movil.mostrar()


        