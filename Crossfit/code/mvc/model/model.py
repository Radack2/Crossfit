from mysql  import connector

class Model:
    """"
    ***********************************************************
    A data model with Mysql for buying a ticket for a crossfit. 
    ***********************************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()


    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()



    """
    ******************************
    *       Cliente methods      *
    ******************************
    """
    def create_cliente(self, nombre, apellidoP, apellidoM, edad, tel, email, fechaPago):
        try:
            sql = 'INSERT INTO cliente (`cl_nombre`, `cl_apellido_p`, `cl_apellido_m`,`cl_edad`,`cl_telefono`,`cl_correo`,`cl_fecha_pago`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (nombre, apellidoP, apellidoM, edad, tel, email, fechaPago)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_cliente(self, id_cliente):
        try:
            sql =  'SELECT * FROM cliente WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_clientes(self): 
        try:
            sql =  'SELECT * FROM cliente'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_cliente_nombre(self, nombre):
        try:
            sql =  'SELECT * FROM cliente WHERE cl_nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_cliente_tel(self, tel):
        try:
            sql =  'SELECT * FROM cliente WHERE cl_telefono = %s'
            vals = (tel,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_cliente(self, fields, vals):
        try:
            sql = 'UPDATE cliente SET '+','.join(fields)+' WHERE id_cliente = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_cliente(self, id_cliente):
        try:
            sql =  'DELETE FROM cliente WHERE id_cliente = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    """
    ******************************
    *        Coach methods       *
    ******************************
    """
    def create_coach(self, horaInicio, horaFin, nombre, apellidoP, apellidoM, tel, email):
        try:
            sql = 'INSERT INTO coach (`co_hora_inicio`, `co_hora_termina`, `co_nombre`,`co_apellido_p`,`co_apellido_m`,`co_telefono`,`co_correo`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (horaInicio, horaFin, nombre, apellidoP, apellidoM, tel, email)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_coach(self, id_coach):
        try:
            sql =  'SELECT * FROM coach WHERE id_coach = %s'
            vals = (id_coach,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_coach(self): 
        try:
            sql =  'SELECT * FROM coach'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_coach_nombre(self, nombre):
        try:
            sql =  'SELECT * FROM coach WHERE cl_nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_coach_dia(self, dia):
        try:
            sql =  'SELECT * FROM coach WHERE DATE(co_hora_inicio) = %s'
            vals = (dia,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
            
    def update_coach(self, fields, vals):
        try:
            sql = 'UPDATE coach SET '+','.join(fields)+' WHERE id_coach = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_coach(self, id_coach):
        try:
            sql =  'DELETE FROM coach WHERE id_coach = %s'
            vals = (id_coach,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *       Material methods     *
    ******************************
    """
    def create_material(self, nombre, cantidad, descripcion):
        try:
            sql = 'INSERT INTO material (`m_nombre`, `m_cantidad`, `m_descripcion`) VALUES (%s, %s, %s)'
            vals = ( nombre, cantidad, descripcion )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_material(self, material):
        try:
            sql = 'SELECT * FROM material WHERE m_nombre = %s'
            vals = (material,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_materiales(self):   
        try:
            sql =  'SELECT * FROM material'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_material(self, fields, vals):
        try:
            sql = 'UPDATE material SET '+','.join(fields)+' WHERE m_nombre = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_material(self, material):
        try:
            sql =  'DELETE FROM material WHERE m_nombre = %s'
            vals = (material,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    """
    ******************************
    *       Ejercicio methods     *
    ******************************
    """
    def create_ejercicio(self, nombre, material, descripcion):
        try:
            sql = 'INSERT INTO ejercicio (`e_nombre`, `m_nombre`, `e_descripcion`) VALUES (%s, %s, %s)'
            vals = ( nombre, material, descripcion )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_ejercicio(self, ejercicio):
        try:
            sql = 'SELECT * FROM ejercicio WHERE e_nombre = %s'
            vals = (ejercicio,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_ejercicios(self):   
        try:
            sql =  'SELECT * FROM ejercicio'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ejercicio(self, fields, vals):
        try:
            sql = 'UPDATE ejercicio SET '+','.join(fields)+' WHERE e_nombre = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ejercicio(self, ejercicio):
        try:
            sql =  'DELETE FROM ejercicio WHERE e_nombre = %s'
            vals = (ejercicio,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *       WOD methods     *
    ******************************
    """
    def create_wod(self, ejercicio, tiempo, repeticiones):
        try:
            sql = 'INSERT INTO wod (`e_nombre`, `w_tiempo`, `w_repeticiones`) VALUES (%s, %s, %s)'
            vals = ( ejercicio, tiempo, repeticiones )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_wod(self, id_wod):
        try:
            sql = 'SELECT * FROM wod WHERE id_wod = %s'
            vals = (id_wod,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_wods(self):   
        try:
            sql =  'SELECT * FROM wod'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_wod(self, fields, vals):
        try:
            sql = 'UPDATE wod SET '+','.join(fields)+' WHERE id_wod = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_wod(self, id_wod):
        try:
            sql =  'DELETE FROM wod WHERE id_wod = %s'
            vals = (id_wod,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    """
    ******************************
    *       Clase methods     *
    ******************************
    """
    def create_clase(self, horaInicio, horaFin, wod, coach, cliente):
        try:
            sql = 'INSERT INTO clase (`hora_inicio`, `hora_termina`, `id_wod`, `id_coach`, `id_cliente`) VALUES (%s, %s, %s, %s, %s)'
            vals = ( horaInicio, horaFin, wod, coach, cliente )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_clase(self, id_clase):
        try:
            sql = 'SELECT * FROM clase WHERE id_clase = %s'
            vals = (id_clase,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_clases(self):   
        try:
            sql =  'SELECT * FROM clase'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_clase_coach(self, id_clase):
        try:
            sql = 'SELECT clase.*, coach.co_nombre, coach.co_apellido_p, coach.co_hora_inicio, coach.co_hora_termina FROM clase JOIN coach ON clase.id_coach = coach.id_coach and id_clase = %s'
            vals = (id_clase,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_clase_dia(self, dia):   
        try:
            sql = 'SELECT * FROM clase WHERE TIME(hora_inicio) = %s'
            vals = (dia,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_clase_horario(self, horrio):   
        try:
            sql = 'SELECT * FROM clase WHERE DATE(hora_inicio) = %s'
            vals = (horrio,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def update_clase(self, fields, vals):
        try:
            sql = 'UPDATE clase SET '+','.join(fields)+' WHERE id_clase = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_clase(self, id_clase):
        try:
            sql =  'DELETE FROM clase WHERE id_clase = %s'
            vals = (id_clase,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    *         User methods       *
    ******************************
    """
    def create_usuario(self, nombre, password):
        try:
            sql = 'INSERT INTO usuario (`nombre`, `pass`) VALUES (%s, %s)'
            vals = ( nombre, password )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_usuario(self, id_user):
        try:
            sql = 'SELECT * FROM usuario WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_usuario(self):   
        try:
            sql =  'SELECT * FROM usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_usuario(self, fields, vals):
        try:
            sql = 'UPDATE usuario SET '+','.join(fields)+' WHERE id_user = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_usuario(self, id_user):
        try:
            sql =  'DELETE FROM usuario WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err







    