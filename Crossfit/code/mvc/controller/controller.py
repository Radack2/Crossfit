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
        o = '8'
        while 0 != '8':
            self.view.main_menu()
            self.view.option('8')
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
                self.user_menu()
            elif o == '8':
                self.view.end()
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
                self.create_cliente()
            elif o == '2':
                self.read_cliente()
            elif o == '3':
                self.read_all_clientes()
            elif o == '4':
                self.read_cliente_nombre()
            elif o == '5':
                self.read_cliente_tel()
            elif o == '6':
                self.update_cliente()
            elif o == '7':
                self.delete_cliente()
            elif o == '8':
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
        return [nombre, apellidoP, apellidoM, edad, tel, email, fechaPago]

    def create_client(self):
        nombre, apellidoP, apellidoM, edad, tel, email, fechaPago = self.ask_cliente()
        out = self.model.create_cliente(nombre, apellidoP, apellidoM, edad, tel, email, fechaPago)
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

    def read_cliente_tel(self):
        self.view.ask('Teléfono: ')
        tel = input()
        clients = self.model.read_cliente_tel(tel)
        if type(clients) == list:
            self.view.show_cliente_header(' Cliente con el teléfono: '+tel+' ')
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
        fields, vals = self.update_lists(['cl_nombre', 'cl_apellido_p', 'cl_apellido_m', 'cl_edad', 'cl_telefono', 'cl_correo', 'cl_fecha_pago'], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok(id_client, 'actualizadó')
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

    
    
