#Variable
clientes = []

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        
        def __init__(self,nombre,contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto,direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []
            
        def agregar_mascota(self,mascota):
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1
        
        def __init__(self,nombre,especie,raza,edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre 
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico= []
            
            SistemaVeterinaria.Mascota.id_counter += 1
            
        def agregar_cita(self,cita):
            self.historia_clinico.append(cita)

    class Citas:
        id_counter = 1
        
        def __init__(self,fecha,hora,servicio,veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            
            SistemaVeterinaria.Citas.id_counter += 1

#Funciones del sistemas
def registrar_cliente():
    print("========REGISTRO DE CLIENTE===========")
    nombre = input("Ingrese nombre del cliente: ")
    contacto = input("Ingrese contacto del cliente: ")
    direccion = input("Ingrese la direccion del cliente: ")
    cliente = SistemaVeterinaria.Cliente(nombre,contacto,direccion)
    
    print("=============REGISTRO DE MASCOTA==========")
    nombre_mascota= input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    raza = input("Raza de la mascota: ")
    edad = input("Ingrese edad de la mascota: ")
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie,raza,edad)
    
    cliente.agregar_mascota(mascota)
    
    clientes.append(cliente)
    print("Cliente y mascota agregado con exito")
    

def programar_cita():
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del cliente: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return
    
    
    
    print("Cita agendada")

def consultar_historia():
    pass

#Menu Principal
def menu_principal():
    while True:
        print("==============Menu Principal==============")
        print("1. Registar cliente y mascota")
        print("2. Programar Cita")
        print("3. Consultar historial de servicios")
        print("4. Salir")
        opc = input("Selecicion una opcion: ")
        
        if opc == "1":
            registrar_cliente()
        elif opc == "2":
            programar_cita()
        elif opc == "3":
            pass
        elif opc == "4":
            break
        else:
            print("Opcion no valida. Intente de nuevo")

menu_principal()