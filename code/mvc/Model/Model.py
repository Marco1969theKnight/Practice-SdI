from mysql import connector


class Model:

    """
    *******************************************
    * A data model with MySQL for a cinema DB *
    *******************************************
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
    ***************************
    * A model for a cinema DB *
    ***************************
    """

    """
    *************************
    * Administrator methods *
    *************************
    """

    def create_administrador(self, nombre, apellido_1, apellido_2, correo, telefono, contrasenia):
        try:
            sql = 'INSERT INTO  administrador (`nombre`, `apellido_1`, `apellido_2`, `correo`, `telefono`, `contrasenia`) VALUES(%s, %s, %s, %s, %s, %s)'
            vals = (nombre, apellido_1, apellido_2,
                    correo, telefono, contrasenia)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_pais = self.cursor.lastrowid
            return id_pais
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_administrador(self, id_administrador):
        try:
            sql = 'SELECT * FROM administrador WHERE id_administrador = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_administrador_sesion(self, correo, contrasenia):
        try:
            sql = 'SELECT * FROM administrador WHERE correo = %s AND contrasenia = %s'
            vals = (correo, contrasenia)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_administrador_correo(self, correo):
        try:
            sql = 'SELECT * FROM administrador WHERE correo = %s'
            vals = (correo, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_administrador_nombre_completo(self, nombre, apellido_1, apellido_2):
        try:
            sql = 'SELECT * FROM administrador WHERE nombre = %s AND apellido_1 = %s AND apellido_2 = %s'
            vals = (nombre, apellido_1, apellido_2)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_administrador(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_administrador(self, fields, vals):
        try:
            sql = 'UPDATE administrador SET ' + \
                ','.join(fields)+' WHERE id_administrador = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_administrador(self, id_administrador):
        try:
            sql = 'DELETE FROM administrador WHERE id_administrador = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * User methods *
    ****************
    """

    def create_usuario(self, nombre, apellido, correo, contrasenia):
        try:
            sql = 'INSERT INTO  usuario (`nombre`, `apellido`, `correo`, `contrasenia`) VALUES(%s, %s, %s, %s)'
            vals = (nombre, apellido, correo, contrasenia)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_usuario = self.cursor.lastrowid
            return id_usuario
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_usuario(self, id_usuario):
        try:
            sql = 'SELECT * FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_usuario_sesion(self, correo, contrasenia):
        try:
            sql = 'SELECT * FROM usuario WHERE correo = %s AND contrasenia = %s'
            vals = (correo, contrasenia)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_usuario(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM usuario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_usuario(self, fields, vals):
        try:
            sql = 'UPDATE usuario SET ' + \
                ','.join(fields)+' WHERE id_usuario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_usuario(self, id_usuario):
        try:
            sql = 'DELETE FROM usuario WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Schedule methods *
    ********************
    """

    def create_horario(self, fecha, hora_inicio):
        try:
            sql = 'INSERT INTO  horario (`fecha`, `hora_inicio`) VALUES(%s, %s)'
            vals = (fecha, hora_inicio)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_horario = self.cursor.lastrowid
            return id_horario
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_horario(self, id_horario):
        try:
            sql = 'SELECT * FROM horario WHERE id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_horario_particular(self, fecha, hora_inicio):
        try:
            sql = 'SELECT * FROM horario WHERE fecha = %s AND hora_inicio = %s'
            vals = (fecha, hora_inicio)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_all_horario(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM horario'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_horario_fecha(self, fecha):
        try:
            sql = 'SELECT * FROM horario WHERE fecha = %s'
            vals = (fecha, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_horario(self, fields, vals):
        try:
            sql = 'UPDATE horario SET ' + \
                ','.join(fields)+' WHERE id_horario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_horario(self, id_horario):
        try:
            sql = 'DELETE FROM horario WHERE id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    * Saloon methods *
    ******************
    """

    def create_sala(self, nombre, tipo, capacidad, precio):
        try:
            sql = 'INSERT INTO  sala (`nombre`, `tipo`, `capacidad`, `precio`) VALUES(%s, %s, %s, %s)'
            vals = (nombre, tipo, capacidad, precio)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_sala = self.cursor.lastrowid
            return id_sala
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_sala_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM sala WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_sala(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_sala_tipo(self, tipo):
        try:
            sql = 'SELECT * FROM sala WHERE tipo = %s'
            vals = (tipo, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE sala SET ' + \
                ','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Seat methods *
    ****************
    """

    def create_asientos(self, fila, numero, ocupado, id_sala):
        try:
            sql = 'INSERT INTO  asientos (`fila`, `numero`, `ocupado`, `id_sala`) VALUES(%s, %s, %s, %s)'
            vals = (fila, numero, ocupado, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_asientos = self.cursor.lastrowid
            return id_asientos
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_asientos(self, id_asientos):
        try:
            sql = 'SELECT asientos.*, sala.nombre FROM asientos JOIN sala ON asientos.id_sala = sala.id_sala WHERE asientos.id_asientos = %s'
            vals = (id_asientos,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_asientos_particulares(self, fila, numero):
        try:
            sql = 'SELECT asientos.*, sala.nombre FROM asientos JOIN sala ON asientos.id_sala = sala.id_sala WHERE asientos.fila = %s AND asientos.numero = %s'
            vals = (fila, numero)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_asientos(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT asientos.*, sala.nombre FROM asientos JOIN sala ON asientos.id_sala = sala.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_asientos_sala(self, id_sala):
        try:
            sql = 'SELECT asientos.*, sala.nombre FROM asientos JOIN sala ON asientos.id_sala = sala.id_sala WHERE asientos.id_sala = %s'
            vals = (id_sala, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_asientos(self, fields, vals):
        try:
            sql = 'UPDATE asientos SET ' + \
                ','.join(fields)+' WHERE id_asientos = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asientos(self, id_asientos):
        try:
            sql = 'DELETE FROM asientos WHERE id_asientos = %s'
            vals = (id_asientos,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***************************
    * cinema function methods *
    ***************************
    """

    def create_funcion(self, id_sala, id_horario, id_pelicula):
        try:
            sql = 'INSERT INTO  funcion (`id_sala`, `id_horario`, `id_pelicula`) VALUES(%s, %s, %s)'
            vals = (id_sala, id_horario, id_pelicula)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_sala = self.cursor.lastrowid
            return id_sala
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_funcion(self, id_sala, id_horario, id_pelicula):
        try:
            sql = 'SELECT sala.*, horario.*, peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM funcion JOIN sala ON funcion.id_sala = sala.id_sala JOIN horario ON funcion.id_horario = horario.id_horario JOIN peliculas ON funcion.id_pelicula = peliculas.id_pelicula JOIN genero ON peliculas.id_genero = genero.id_genero JOIN pais ON peliculas.id_pais = pais.id_pais JOIN directores ON peliculas.id_director = directores.id_director WHERE funcion.id_sala = %s AND funcion.id_horario = %s AND funcion.id_pelicula = %s'
            vals = (id_sala, id_horario, id_pelicula)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_funcion_sala(self, id_sala):
        try:
            sql = 'SELECT sala.*, horario.*, peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM funcion JOIN sala ON funcion.id_sala = sala.id_sala JOIN horario ON funcion.id_horario = horario.id_horario JOIN peliculas ON funcion.id_pelicula = peliculas.id_pelicula JOIN genero ON peliculas.id_genero = genero.id_genero JOIN pais ON peliculas.id_pais = pais.id_pais JOIN directores ON peliculas.id_director = directores.id_director WHERE funcion.id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_funcion_horario(self, id_horario):
        try:
            sql = 'SELECT sala.*, horario.*, peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM funcion JOIN sala ON funcion.id_sala = sala.id_sala JOIN horario ON funcion.id_horario = horario.id_horario JOIN peliculas ON funcion.id_pelicula = peliculas.id_pelicula JOIN genero ON peliculas.id_genero = genero.id_genero JOIN pais ON peliculas.id_pais = pais.id_pais JOIN directores ON peliculas.id_director = directores.id_director WHERE funcion.id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_funcion_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT sala.*, horario.*, peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM funcion JOIN sala ON funcion.id_sala = sala.id_sala JOIN horario ON funcion.id_horario = horario.id_horario JOIN peliculas ON funcion.id_pelicula = peliculas.id_pelicula JOIN genero ON peliculas.id_genero = genero.id_genero JOIN pais ON peliculas.id_pais = pais.id_pais JOIN directores ON peliculas.id_director = directores.id_director WHERE funcion.id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_funcion(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT sala.*, horario.*, peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM funcion JOIN sala ON funcion.id_sala = sala.id_sala JOIN horario ON funcion.id_horario = horario.id_horario JOIN peliculas ON funcion.id_pelicula = peliculas.id_pelicula JOIN genero ON peliculas.id_genero = genero.id_genero JOIN pais ON peliculas.id_pais = pais.id_pais JOIN directores ON peliculas.id_director = directores.id_director'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def delete_funcion(self, id_sala, id_horario, id_pelicula):
        try:
            sql = 'DELETE FROM funcion WHERE id_sala = %s AND id_horario = %s AND id_pelicula = %s'
            vals = (id_sala, id_horario, id_pelicula)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************
    * A model for a movie DB *
    **************************
    """

    """
    *******************
    * Country methods *
    *******************
    """

    def create_pais(self, nombre):
        try:
            sql = 'INSERT INTO  pais (`nombre`) VALUES(%s)'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_pais = self.cursor.lastrowid
            return id_pais
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_pais(self, id_pais):
        try:
            sql = 'SELECT * FROM pais WHERE id_pais = %s'
            vals = (id_pais,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_pais_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM pais WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_pais(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM pais'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_pais(self, fields, vals):
        try:
            sql = 'UPDATE pais SET '+','.join(fields)+' WHERE id_pais = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pais(self, id_pais):
        try:
            sql = 'DELETE FROM pais WHERE id_pais = %s'
            vals = (id_pais,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *****************
    * Genre methods *
    *****************
    """

    def create_genero(self, nombre, sub_gen):
        try:
            sql = 'INSERT INTO  genero (`nombre`, `sub_gen`) VALUES(%s, %s)'
            vals = (nombre, sub_gen)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_genero = self.cursor.lastrowid
            return id_genero
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_genero(self, id_genero):
        try:
            sql = 'SELECT * FROM genero WHERE id_genero = %s'
            vals = (id_genero,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_genero(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM genero'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_genero_sub_gen(self, sub_gen):
        try:
            sql = 'SELECT * FROM genero WHERE sub_gen = %s'
            vals = (sub_gen,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_genero_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM genero WHERE nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_genero(self, fields, vals):
        try:
            sql = 'UPDATE genero SET '+','.join(fields)+' WHERE id_genero = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_genero(self, id_genero):
        try:
            sql = 'DELETE FROM genero WHERE id_genero = %s'
            vals = (id_genero,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ********************
    * Director methods *
    ********************
    """

    def create_directores(self, nombre, apellido, anio_act_in, anio_act_fin):
        try:
            sql = 'INSERT INTO  directores (`nombre`, `apellido`, `anio_act_in`, `anio_act_fin`) VALUES(%s, %s, %s, %s)'
            vals = (nombre, apellido, anio_act_in, anio_act_fin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_director = self.cursor.lastrowid
            return id_director
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_directores(self, id_director):
        try:
            sql = 'SELECT * FROM directores WHERE directores.id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_directores(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT * FROM directores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM directores WHERE directores.nombre = %s'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_apellido(self, apellido):
        try:
            sql = 'SELECT * FROM directores WHERE directores.apellido = %s'
            vals = (apellido,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_anio_act_in(self, anio_act_in):
        try:
            sql = 'SELECT * FROM directores WHERE directores.anio_act_in = %s'
            vals = (anio_act_in,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_anio_act_fin(self, anio_act_fin):
        try:
            sql = 'SELECT * FROM directores WHERE directores.anio_act_fin = %s'
            vals = (anio_act_fin,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_anio_act_range(self, anio_ini, anio_end):
        try:
            sql = 'SELECT * FROM directores WHERE directores.anio_act_in >= %s AND directores.anio_act_fin <= %s'
            vals = (anio_ini, anio_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_directores(self, fields, vals):
        try:
            sql = 'UPDATE directores SET ' + \
                ','.join(fields)+' WHERE id_director = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_directores(self, id_director):
        try:
            sql = 'DELETE FROM directores WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************
    * Movies methods *
    ******************
    """

    def create_peliculas(self, titulo, id_genero, id_director, anio, id_pais, calif):
        try:
            sql = 'INSERT INTO  peliculas (`titulo`, `id_genero`, `id_director`, `anio`, `id_pais`, `calif`) VALUES(%s, %s, %s, %s, %s, %s)'
            vals = (titulo, id_genero, id_director, anio, id_pais, calif)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_pelicula = self.cursor.lastrowid
            return id_pelicula
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_peliculas(self, id_pelicula):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_peliculas_id_genero(self, genero):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.id_genero = %s'
            vals = (genero,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_titulo(self, titulo):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.titulo = %s'
            vals = (titulo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_id_director(self, director):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.id_director = %s'
            vals = (director,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_anio(self, anio):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.anio = %s'
            vals = (anio,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_anio_range(self, anio_ini, anio_end):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.anio >= %s AND peliculas.anio <= %s'
            vals = (anio_ini, anio_end)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_id_pais(self, pais):
        try:
            if pais == None:
                sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, peliculas.id_pais, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director AND peliculas.id_pais IS NULL'
                self.cursor.execute(sql)
            else:
                sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.id_pais = %s'
                vals = (pais,)
                self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_calif(self, calif):
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais WHERE peliculas.calif = %s'
            vals = (calif,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas(self):    # Caution if large ammount of data
        try:
            sql = 'SELECT peliculas.id_pelicula, peliculas.titulo, genero.nombre, directores.nombre, directores.apellido, peliculas.anio, pais.nombre, peliculas.calif FROM peliculas JOIN genero ON peliculas.id_genero = genero.id_genero JOIN directores ON peliculas.id_director = directores.id_director LEFT JOIN pais ON peliculas.id_pais = pais.id_pais'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_peliculas(self, fields, vals):
        try:
            sql = 'UPDATE peliculas SET ' + \
                ','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_peliculas(self, id_pelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
