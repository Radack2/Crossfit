from model.model import Model
from view.view import View
from datetime import date


class Controller:
    """
    ************************************
    *  A controller for a crossfit DB  *
    ************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()


    """
    *********************************
    *       General Controller      *
    *********************************
    """
    def main_menu(self):
        o = '0'
        while o != '7':
            self.view.main_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.cliente_menu()
            elif o == '2':
                self.coach_menu()
            elif o == '3':
                self.material_menu()
            elif o == '4':
                self.ejercicio_menu()
            elif o == '5':
                self.wod_menu()
            elif o == '6':
                self.clase_menu()
            elif o == '7':
                self.view.end()
                exit()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals


    """
    *********************************
    *    Controllers for cliente    *
    *********************************
    """
    def cliente_menu(self):
        o = '0'
        while o != '8':
            self.view.cliente_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_client()
            elif o == '2':
                self.read_cliente()
            elif o == '3':
                self.read_all_clientes()
            elif o == '4':
                self.read_cliente_nombre()
            elif o == '5':
                self.update_cliente()
            elif o == '6':
                self.delete_cliente()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_cliente(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        apellidoP = input()
        self.view.ask('Apellido Materno: ')
        apellidoM = input()
        self.view.ask('Edad: ')
        edad = input()
        self.view.ask('Teléfono: ')
        tel = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Fecha de Pago: ')
        fechaPago = input()
        self.view.ask('Hora de clase: ')
        hora_clase = input()
        return [nombre, apellidoP, apellidoM, edad, tel, email, fechaPago, hora_clase]

    def create_client(self):
        nombre, apellidoP, apellidoM, edad, tel, email, fechaPago, hora_clase = self.ask_cliente()
        out = self.model.create_cliente(nombre, apellidoP, apellidoM, edad, tel, email, fechaPago, hora_clase)
        if out == True:
            self.view.ok(nombre+' '+apellidoP+' '+apellidoM, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL CLIENTE. REVISA')
        return

    def read_cliente(self):
        self.view.ask('ID Cliente: ')
        id_cliente = input()
        client = self.model.read_cliente(id_cliente)
        if type(client) == tuple:
            self.view.show_cliente_header(' Datos del cliente '+id_cliente+' ')
            self.view.show_a_cliente(id_cliente)
            self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER EL CLIENTE. REVISA')
        return
    
    def read_all_clientes(self):
        clients = self.model.read_all_clientes()
        if type(clients) == list:
            self.view.show_cliente_header(' Todos los clientes ')
            for client in clients:
                self.view.show_a_cliente(client)
                self.view.show_cliente_midder()
                self.view.show_cliente_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA')
        return
    
    def read_cliente_nombre(self):
        self.view.ask('Nombre: ')
        name = input()
        clients = self.model.read_cliente_nombre(name)
        if type(clients) == list:
            self.view.show_cliente_header(' Clientes con el nombre: '+name+' ')
            for client in clients:
                self.view.show_a_cliente(client)
                self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA')
        return

    def update_cliente(self):
        self.view.ask('ID de cliente a modificar: ')
        id_client = input()
        client = self.model.update_cliente(id_client)
        if type(client) == tuple:
            self.view.show_cliente_header(' Datos del Cliente: '+id_client+' ')
            self.view.show_a_cliente(client)
            self.view.show_cliente_midder()
            self.view.show_cliente_footer()
        else:
            if client == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CLIENTE. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_cliente()
        fields, vals = self.update_lists(['`nombre`, `apellido_p`, `apellido_m`,`edad`,`telefono`,`correo`,`fecha_pago`,`hora_clase`'], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok(id_client, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CLIENTE. REVISA')
        return

    def delete_cliente(self):
        self.view.ask('ID de cliente a borrar: ')
        id_client = input()
        count = self.model.delete_cliente(id_client)
        if count != 0:
            self.view.ok(id_client, 'se borró')
        else:
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CLIENTE. REVISA')
        return

    """
    *********************************
    *     Controllers for coach     *
    *********************************
    """
    def coach_menu(self):
        o = '0'
        while o != '8':
            self.view.coach_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_coach()
            elif o == '2':
                self.read_coach()
            elif o == '3':
                self.read_all_coach()
            elif o == '4':
                self.read_coach_nombre()
            elif o == '5':
                self.update_coach()
            elif o == '6':
                self.delete_coach()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_coach(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido Paterno: ')
        apellidoP = input()
        self.view.ask('Apellido Materno: ')
        apellidoM = input()
        self.view.ask('Teléfono: ')
        tel = input()
        self.view.ask('Email: ')
        email = input()
        return [nombre, apellidoP, apellidoM, tel, email]

    def create_coach(self):
        nombre, apellidoP, apellidoM, tel, email = self.ask_coach()
        out = self.model.create_coach( nombre, apellidoP, apellidoM, tel, email)
        if out == True:
            self.view.ok(nombre+' '+apellidoP+' '+apellidoM, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL COACH. REVISA')
        return

    def read_coach(self):
        self.view.ask('ID Coach: ')
        id_coach = input()
        coach = self.model.read_coach(id_coach)
        print(coach)
        if type(coach) == tuple:
            self.view.show_coach_header(' Datos del coach '+id_coach+' ')
            self.view.show_a_coach(coach)
            self.view.show_coach_midder()
            self.view.show_coach_footer()
        else:
            if coach == None:
                self.view.error('EL COACH NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER EL COACH. REVISA')
        return
    
    def read_all_coach(self):
        coachs = self.model.read_all_coach()
        if type(coachs) == list:
            self.view.show_coach_header(' Todos los coachs ')
            for coach in coachs:
                self.view.show_a_coach(coach)
                self.view.show_coach_midder()
                self.view.show_coach_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS COACHS. REVISA')
        return
    
    def read_coach_nombre(self):
        self.view.ask('Nombre: ')
        name = input()
        coachs = self.model.read_coach_nombre(name)
        if type(coachs) == list:
            self.view.show_coach_header(' Coach con el nombre: '+name+' ')
            for coach in coachs:
                self.view.show_a_coach(coach)
                self.view.show_coach_midder()
                self.view.show_coach_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL COACH. REVISA')
        return

    def update_coach(self):
        self.view.ask('ID de coach a modificar: ')
        id_coach = input()
        coach = self.model.update_coach(id_coach)
        if type(coach) == tuple:
            self.view.show_coach_header(' Datos del coach: '+id_coach+' ')
            self.view.show_a_coach(coach)
            self.view.show_coach_midder()
            self.view.show_coach_footer()
        else:
            if coach == None:
                self.view.error('EL COACHS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL COACHS. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_coach()
        fields, vals = self.update_lists(['nombre', 'apellido_p', 'apellido_m', 'telefono', 'correo'], whole_vals)
        vals.append(id_coach)
        vals = tuple(vals)
        out = self.model.update_coach(fields, vals)
        if out == True:
            self.view.ok(id_coach, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL COACHS. REVISA')
        return

    def delete_coach(self):
        self.view.ask('ID de coach a borrar: ')
        id_coach = input()
        count = self.model.delete_coach(id_coach)
        if count != 0:
            self.view.ok(id_coach, 'se borró')
        else:
            if count == 0:
                self.view.error('EL COACHS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL COACHS. REVISA')
        return

    """
    ************************************
    *     Controllers for Material     *
    ************************************
    """

    def material_menu(self):
        o = '0'
        while o != '6':
            self.view.material_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_material()
            elif o == '2':
                self.read_a_material()
            elif o == '3':
                self.read_all_materiales()
            elif o == '4':
                self.update_material()
            elif o == '5':
                self.delete_material()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_material(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Cantidad: ')
        cantidad = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        return [nombre, cantidad, descripcion]

    def create_material(self):
        nombre, cantidad, descripcion = self.ask_material()
        out = self.model.create_material(nombre, cantidad, descripcion)
        if out == True:
            self.view.ok(nombre,'se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL MATERIAL. REVISA')
        return

    def read_a_material(self):
        self.view.ask('Nombre material: ')
        nombre = input()
        material = self.model.read_a_material(nombre)
        if type(material) == tuple:
            self.view.show_material_header(' Datos del Material: '+nombre+' ')
            self.view.show_a_material(material)
            self.view.show_material_midder()
            self.view.show_material_footer()
        else:
            if material == None:
                self.view.error('EL MATERIAL NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER EL MATERIAL. REVISA')
        return
    
    def read_all_materiales(self):
        materiales = self.model.read_all_materiales()
        if type(materiales) == list:
            self.view.show_material_header(' Todos los materiales ')
            for material in materiales:
                self.view.show_a_material(material)
                self.view.show_material_midder()
                self.view.show_material_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS MATERIALES. REVISA')
        return
    
    def update_material(self):
        self.view.ask('Nombre de material a modificar: ')
        nombre = input()
        material = self.model.read_a_material(nombre)
        if type(material) == tuple:
            self.view.show_material_header(' Datos del material: '+nombre+' ')
            self.view.show_a_material(material)
            self.view.show_material_midder()
            self.view.show_material_footer()
        else:
            if material == None:
                self.view.error('EL MATERIAL NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL MATERIAL. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_material()
        fields, vals = self.update_lists(['nombre', 'cantidad', 'descripcion'], whole_vals)
        vals.append(nombre)
        vals = tuple(vals)
        out = self.model.update_material(fields, vals)
        if out == True:
            self.view.ok(nombre, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL MATERIAL. REVISA')
        return

    def delete_material(self):
        self.view.ask('Nombre del material a borrar: ')
        nombre = input()
        count = self.model.delete_material(nombre)
        if count != 0:
            self.view.ok(nombre, 'se borró')
        else:
            if count == 0:
                self.view.error('EL MATERIAL NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL MATERIAL. REVISA')
        return

 

    """
    ************************************
    *     Controllers for Ejercicios     *
    ************************************
    """
    def ejercicio_menu(self):
        o = '0'
        while o != '6':
            self.view.ejercicio_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_ejercicio()
            elif o == '2':
                self.read_a_ejercicio()
            elif o == '3':
                self.read_all_ejercicios()
            elif o == '4':
                self.update_ejercicio()
            elif o == '5':
                self.delete_ejercicio()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_ejercicio(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Material: ')
        material = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        return [nombre, material, descripcion]

    def create_ejercicio(self):
        nombre, material, descripcion = self.ask_ejercicio()
        out = self.model.create_ejercicio(nombre, material, descripcion)
        if out == True:
            self.view.ok(nombre+' '+material, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL EJERCICIO. REVISA')
        return

    def read_a_ejercicio(self):
        self.view.ask('Nombre Ejercicio: ')
        nombre = input()
        ejercicio = self.model.read_a_ejercicio(nombre)
        if type(ejercicio) == tuple:
            self.view.show_ejercicio_header(' Datos del ejercicio: '+nombre+' ')
            self.view.show_a_ejercicio(ejercicio)
            self.view.show_ejercicio_midder()
            self.view.show_ejercicio_footer()
        else:
            if ejercicio == None:
                self.view.error('EL EJERCICIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER EL EJERCICIO. REVISA')
        return
    
    def read_all_ejercicios(self):
        ejercicios = self.model.read_all_ejercicios()
        if type(ejercicios) == list:
            self.view.show_ejercicio_header(' Todos los ejercicios ')
            for ejercicio in ejercicios:
                self.view.show_a_ejercicio(ejercicio)
                self.view.show_ejercicio_midder()
                self.view.show_ejercicio_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS EJERCICIOS. REVISA')
        return
    
    def update_ejercicio(self):
        self.view.ask('Nombre del ejercicio a modificar: ')
        nombre = input()
        ejercicio = self.model.read_a_ejercicio(nombre)
        if type(ejercicio) == tuple:
            self.view.show_ejercicio_header(' Datos del ejercicio: '+nombre+' ')
            self.view.show_a_ejercicio(ejercicio)
            self.view.show_ejercicio_midder()
            self.view.show_ejercicio_footer()
        else:
            if ejercicio == None:
                self.view.error('EL EJERCICIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL EJERCICIO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_ejercicio()
        fields, vals = self.update_lists(['nombre', 'material', 'descripcion'], whole_vals)
        vals.append(nombre)
        vals = tuple(vals)
        out = self.model.update_ejercicio(fields, vals)
        if out == True:
            self.view.ok(nombre, 'actualizadó')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL EJERCICIO. REVISA')
        return

    def delete_ejercicio(self):
        self.view.ask('Nombre del ejercicio a borrar: ')
        nombre = input()
        count = self.model.delete_ejercicio(nombre)
        if count != 0:
            self.view.ok(nombre, 'se borró')
        else:
            if count == 0:
                self.view.error('EL EJERCICIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL EJERCICIO. REVISA')
        return

 
    """
    ************************************
    *        Controllers for WOD       *
    ************************************
    """
    def wod_menu(self):
        o = '0'
        while o != '9':
            self.view.wod_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_wod()
            elif o == '2':
                self.read_a_wod()
            elif o == '3':
                self.read_all_wods()
            elif 0 == '4':
                self.agregar_ejercicios_wod()
            elif o == '5':
                self.update_wod()
            elif o == '6':
                self.update_ejercicio_wod()
            elif o == '7':
                self.delete_ejercicio_wod()
            elif o == '8':
                self.delete_wod()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_wod(self):
        self.view.ask('Fecha wod: ')
        fecha = input()
        self.view.ask('Tiempo (minutos): ')
        tiempo = input()
        self.view.ask('Tipo: ')
        tipo = input()
        return [fecha, tiempo, tipo]
    
    def ask_ejercicio(self):
        self.view.ask('Nombre Ejercicio: ')
        nombre = input()
        self.view.ask('Repeticiones: ')
        reps = input()
        return [nombre,reps]

    def create_wod(self):
        fecha, tiempo, tipo = self.ask_wod()
        out = self.model.create_wod(fecha, tiempo, tipo)
        if out == True:
            print('Cuantos ejercicios desea agregar al wod?')
            n = input()
            for i in range(int(n)):
                nombre,reps = self.ask_ejercicio()
                out1 = self.model.agregar_ejercicio_wod(nombre,fecha,reps)
                if out1 == True:
                    self.view.ok(nombre, ' se agregó')
                else:
                     self.view.error('NO SE PUDO AGREGAR EL EJERCICIO. REVISA')
            self.view.ok('WOD '+fecha, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL WOD. REVISA')
        return

    def read_a_wod(self):
        self.view.ask('Fecha wod: ')
        fecha = input()
        wod = self.model.read_a_wod(fecha)
        ejercicios = self.model.read_all_ejercicios_wod(fecha)
        if type(wod) == tuple:
            self.view.show_wod_header(' Datos del wod: '+fecha+' ')
            self.view.show_a_wod(wod)
            if type(ejercicios) == list:
                self.view.show_ejercicio_midder()
                self.view.show_ejercicio_header('Ejercicios del WOD ')
                for ejercicio in ejercicios:
                    self.view.show_ejercicio_wod(ejercicio)
                    self.view.show_ejercicio_midder()
                self.view.show_ejercicio_footer()
            else:
                self.view.error('EL WOD NO TIENE EJERCICIOS')
        else:
            if wod == None:
                self.view.error('EL WOD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER EL WOD. REVISA')
        return
    
    def read_all_wods(self):
        wods = self.model.read_all_wods()
        if type(wods) == list:
            self.view.show_wod_header(' Todos los wods ')
            for wod in wods:
                self.view.show_a_wod(wod)
                ejercicios = self.model.read_all_ejercicios_wod(wod[0])
                if type(ejercicios) == list:
                    for ejercicio in ejercicios:
                        self.view.show_ejercicio_wod(ejercicio)
                    self.view.show_wod_midder()
                    self.view.show_wod_footer()
                else:
                    self.view.error('EL WOD NO TIENE EJERCICIOS')
        else:
            self.view.error('PROBLEMA AL LEER LOS WODS. REVISA')
        return
    
    def update_wod(self):
        self.view.ask('Fecha WOD a modificar: ')
        id_wod = input()
        wod = self.model.update_wod(id_wod)
        if type(wod) == tuple:
            self.view.show_wod_header(' Datos del wod: '+id_wod+' ')
            self.view.show_a_wod(wod)
            self.view.show_wod_midder()
            self.view.show_wod_footer()
        else:
            if wod == None:
                self.view.error('EL WOD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL WOD. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_wod()
        fields, vals = self.update_lists(['fecha', 'tiempo', 'tipo'], whole_vals)
        vals.append(id_wod)
        vals = tuple(vals)
        out = self.model.update_wod(fields, vals)
        if out == True:
            self.view.ok(id_wod, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL WOD. REVISA')
        return

    def delete_wod(self):
        self.view.ask('Fecha WOD a borrar: ')
        id_wod = input()
        count = self.model.delete_wod(id_wod)
        if count != 0:
            self.view.ok(id_wod, 'se borró')
        else:
            if count == 0:
                self.view.error('EL WOD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL WOD. REVISA')
        return

    def agregar_ejercicios_wod(self):
        self.view.ask('Fecha WOD a agregar ejercicios: ')
        fecha = input()
        nombre,reps = self.ask_ejercicio()
        out = self.model.agregar_ejercicio_wod(nombre,fecha,reps)
        if out == True:
            self.view.ok(nombre+' agregado al WOD'+fecha, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR EL WOD. REVISA')

    def update_ejercicio_wod(self):
        self.view.ask('Fecha WOD a modificar: ')
        fecha = input()
        wod = self.model.read_a_wod(fecha)
        if type(wod) == tuple:
            self.view.show_wod_header(' Datos del wod: '+fecha+' ')
            self.view.show_a_wod(wod)
            ejercicios = self.model.read_all_ejercicios_wod(wod[0])
            if type(ejercicios) == list:
                for ejercicio in ejercicios:
                    self.view.show_ejercicio_wod(ejercicio)
            self.view.show_wod_midder()
            self.view.show_wod_footer()
        else:
            if wod == None:
                self.view.error('EL WOD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL WOD. REVISA')
            return
        self.view.ask('Nombre del ejercio a modificar: ')
        nombre = input()
        self.view.msg('Ingresa el numero nuevo de repeticiones: ')
        whole_vals = input()
        fields, vals = self.update_lists(['repeticiones'], whole_vals)
        vals.append(fecha)
        vals.append(nombre)
        vals = tuple(vals)
        out = self.model.update_ejercicio_wod(fields, vals)
        if out == True:
            self.view.ok(nombre, 'actualizado')
        else:
            print(out)
            self.view.error('NO SE PUDO ACTUALIZAR EL WOD. REVISA')
        return

    def delete_ejercicio_wod(self):
        self.view.ask('Fecha WOD: ')
        fecha = input()
        wod = self.model.read_a_wod(fecha)
        if type(wod) == tuple:
            self.view.show_wod_header(' Datos del wod: '+fecha+' ')
            self.view.show_a_wod(wod)
            ejercicios = self.model.read_all_ejercicios_wod(wod[0])
            if type(ejercicios) == list:
                for ejercicio in ejercicios:
                    self.view.show_ejercicio_wod(ejercicio)
            self.view.show_wod_midder()
            self.view.show_wod_footer()
        else:
            if wod == None:
                self.view.error('EL WOD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL WOD. REVISA')
            return
        self.view.ask('Nombre del ejercio a eliminar: ')
        nombre = input()
        out = self.model.delete_ejercicio_wod(fecha,nombre)
        if out == True:
            self.view.ok(nombre, 'actualizado')
        else:
            print(out)
            self.view.error('NO SE PUDO ACTUALIZAR EL WOD. REVISA')
        return

    """
    ************************************
    *        Controllers for Clase       *
    ************************************
    """
    def clase_menu(self):
        o = '0'
        while o != '6':
            self.view.clase_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_clase()
            elif o == '2':
                self.read_a_clase()
            elif o == '3':
                self.read_all_clases()
            elif o == '4':
                self.read_clase_coach()
            elif o == '5':
                self.update_clase()
            elif o == '6':
                self.delete_clase()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_clase(self):
        self.view.ask('Hora Inicio: ')
        horaInicio = input()
        self.view.ask('Hora Fin: ')
        horaFin = input()
        self.view.ask('Fecha WOD: ')
        wod = input()
        self.view.ask('ID Coach: ')
        coach = input()
        return [horaInicio, horaFin, wod, coach]

    def create_clase(self):
        horaInicio, horaFin, wod, coach = self.ask_clase()
        out = self.model.create_clase(horaInicio, horaFin, wod, coach)
        if out == True:
            self.view.ok('Clase '+horaInicio, ' se agregó')
        else:
            self.view.error('NO SE PUDO AGREGAR LA CLASE. REVISA')
        return

    def read_a_clase(self):
        self.view.ask('Hora de la clase: ')
        hora = input()
        clase = self.model.read_a_clase(hora)
        if type(clase) == tuple:
            self.view.show_clase_header(' Datos de la clase: '+hora+' ')
            self.view.show_a_clase(clase)
            self.view.show_clase_midder()
            self.view.show_clase_footer()
        else:
            if clase == None:
                self.view.error('LA CLASE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LLER LA CLASE. REVISA')
        return
    
    def read_all_clases(self):
        clases = self.model.read_all_clases()
        if type(clases) == list:
            self.view.show_clase_header(' Todas las clases ')
            for clase in clases:
                self.view.show_a_clase(clase)
                self.view.show_clase_midder()
                self.view.show_clase_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CLASES. REVISA')
        return

    def read_clase_coach(self):
        self.view.ask('Nombre Coach: ')
        nombre = input()
        self.view.ask('Apellido Coach: ')
        apellido = input()
        clases = self.model.read_clase_coach(nombre, apellido)
        if type(clases) == list:
            self.view.show_clase_header(' CLases del coach: '+nombre+' ')
            for clase in clases:
                self.view.show_clase_header(' CLase de las: '+str(clase[0])+' ')
                self.view.show_a_clase(clase)
                self.view.show_clase_midder()
            self.view.show_clase_footer()
        else:
            if clase == None:
                self.view.error('LA CLASE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CLASE. REVISA')
        return
    
    def update_clase(self):
        self.view.ask('Hora de clase a  modificar: ')
        hora = input()
        clase = self.model.read_a_clase(hora)
        if type(clase) == tuple:
            self.view.show_clase_header(' Datos de la clase: '+hora+' ')
            self.view.show_a_clase(clase)
            self.view.show_clase_midder()
            self.view.show_clase_footer()
        else:
            if clase == None:
                self.view.error('LA CLASE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA CLASE. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual): ')
        whole_vals = self.ask_clase()
        fields, vals = self.update_lists(['hora_inicio', 'hora_fin', 'fecha_wod','id_coach'], whole_vals)
        vals.append(hora)
        vals = tuple(vals)
        out = self.model.update_wod(fields, vals)
        if out == True:
            self.view.ok(hora, 'Clase actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA CLASE. REVISA')
        return

    def delete_wod(self):
        self.view.ask('Hora de la clase: ')
        hora = input()
        count = self.model.delete_clase(hora)
        if count != 0:
            self.view.ok(hora, 'se borró')
        else:
            if count == 0:
                self.view.error('LA CLASE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA CLASE. REVISA')
        return
