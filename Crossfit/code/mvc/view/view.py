class View:
    """
    **********************************
    *     A view for a Crossfit DB   *
    **********************************
    """

    def start(self):
        print('=================================')
        print('= ¡Bienvenido a la BD CROSSFIT! =')
        print('=================================')

    def end(self):
        print('=================================')
        print('=        ¡Hasta la vista!       =')
        print('=================================')

    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. Clientes')
        print('2. Coachs')
        print('3. Material')
        print('4. Ejercicio')
        print('5. WOD')
        print('6. Clase')
        print('7. Usuario')
        print('8. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de Nuevo')
    
    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def  ok(self, id, op):
        print('+'*(len(str(id)) + len(op) +24))
        print('+ ¡'+str(id)+' '+op+' correctamente! +')
        print('+'*(len(str(id)) + len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err) +4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))


    """
    *******************************
    *       View for Cliente      *
    *******************************
    """
    def cliente_menu(self):
        print('*************************')
        print('* -- Submenu Cliente -- *')
        print('*************************')
        print('1. Agregar Cliente')
        print('2. Mostrar Cliente')
        print('3. Mostrar todos los Clientes')
        print('4. Mostrar Clientes por nombre')
        print('5. Mostrar Clientes por número telefónico')
        print('6. Actualizar Cliente')
        print('7. Borrar Cliente')
        print('8. Regresar')

    def show_a_cliente(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3]+' | ',record[4],' años')
        print('Datos | Email: ', record[5]+' Telefono: '+record[6])
        print('Fecha de pago: ', record[7])

    def show_cliente_header(self, header):
        print(header.center(78, '*'))
        print('-'*78)

    def show_cliente_midder(self):
        print('-'*78)

    def show_cliente_footer(self):
        print('*'*78)


    """
    *****************************
    *       View for Coach      *
    *****************************
    """
    def coach_menu(self):
        print('*************************')
        print('* -- Submenu Coach -- *')
        print('*************************')
        print('1. Agregar Coach')
        print('2. Mostrar Coach')
        print('3. Mostrar todos los Coachs')
        print('4. Mostrar Coachs por nombre')
        print('5. Mostrar Coachs por día de trabajo')
        print('6. Actualizar Coachs')
        print('7. Borrar Coachs')
        print('8. Regresar')

    def show_a_coach(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[3]+' '+record[4]+' '+record[5])
        print('Hora de inicio: ', record[1], ' | Hora Finaliza ', record[2])
        print('Datos | Email: ', record[6]+' Telefono: '+record[7])

    def show_coach_header(self, header):
        print(header.center(78, '*'))
        print('-'*78)

    def show_coach_midder(self):
        print('-'*78)

    def show_coach_footer(self):
        print('*'*78)

    
    """
    *******************************
    *     View for Material       *
    *******************************
    """
    def material_menu(self):
        print('***************************')
        print('* -- Submenu Material -- *')
        print('***************************')
        print('1. Agregar Material')
        print('2. Leer Material')
        print('3. Leer todos los Materiales')
        print('4. Actualizar Material')
        print('5. Borrar Material')
        print('6. Regresar')

    def show_a_material(self, record):
        print('Nombre: ', record[0])
        print('Cantidad: ', record[1])
        print('Descripcion: ', record[2])

    def show_material_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_material_midder(self):
        print('-'*48)

    def show_material_footer(self):
        print('*'*48)


    """
    *******************************
    *     View for Ejercicio      *
    *******************************
    """
    def ejercicio_menu(self):
        print('***************************')
        print('* -- Submenu Ejercicio -- *')
        print('***************************')
        print('1. Agregar Ejercicio')
        print('2. Leer Ejercicio')
        print('3. Leer todos los Ejercicios')
        print('4. Actualizar Ejercicio')
        print('5. Borrar Ejercicio')
        print('6. Regresar')

    def show_a_ejercicio(self, record):
        print('Nombre: ', record[0])
        print('Material: ', record[1])
        print('Descripcion: ', record[2])

    def show_ejercicio_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_ejercicio_midder(self):
        print('-'*48)

    def show_ejercicio_footer(self):
        print('*'*48)


    """
    *******************************
    *         View for WOD        *
    *******************************
    """
    def wod_menu(self):
        print('***************************')
        print('* -- Submenu WOD -- *')
        print('***************************')
        print('1. Agregar WOD')
        print('2. Leer WOD')
        print('3. Leer todos los WOD')
        print('4. Actualizar WOD')
        print('5. Borrar WOD')
        print('6. Regresar')

    def show_a_wod(self, record):
        print('ID WOD: ', record[0])
        print('Ejercicio: ', record[1])
        print('Tiempo: ', record[2])
        print('Repeticiones: ', record[3])

    def show_wod_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_wod_midder(self):
        print('-'*48)

    def show_wod_footer(self):
        print('*'*48)



    """
    *******************************
    *         View for Clase        *
    *******************************
    """
    def clase_menu(self):
        print('***************************')
        print('* -- Submenu Clase -- *')
        print('***************************')
        print('1. Agregar Clase')
        print('2. Leer Clase')
        print('3. Leer todos los Clase')
        print('4. Leer Clase por Coach')
        print('5. Leer Clase por día')
        print('6. Leer Clase por Horario')
        print('7. Actualizar Clase')
        print('8. Borrar Clase')
        print('9. Regresar')

    def show_a_clase(self, record):
        print('ID Clase: ', record[0])
        print('Horario: ', record[1]+' - '+record[2])
        print('ID WOD: ', record[3])
        print('ID Coach: ', record[4])
        print('ID Cliente: ', record[5])

    def show_clase_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_clase_midder(self):
        print('-'*48)

    def show_clase_footer(self):
        print('*'*48)


    """
    *******************************
    *        View for User        *
    *******************************
    """
    def user_menu(self):
        print('***************************')
        print('* -- Submenu Usuario -- *')
        print('***************************')
        print('1. Agregar Usuario')
        print('2. Leer Usuario')
        print('3. Leer todos los Usuario')
        print('4. Actualizar Usuario')
        print('5. Borrar Usuario')
        print('6. Regresar')

    def show_a_user(self, record):
        print('Nombre: ', record[0]+' | password: '+record[1])

    def show_user_header(self, header):
        print(header.center(48, '*'))
        print('-'*48)

    def show_user_midder(self):
        print('-'*48)

    def show_user_footer(self):
        print('*'*48)


