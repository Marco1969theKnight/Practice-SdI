from Model.Model import Model
from View.View import View

class Controller:
    """
    *******************************
    * A controller for a movie DB *
    *******************************
    """

    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ******************************
    * General cinema controllers *
    ******************************
    """

    def main_menu(self):
        o = '100'
        while o != '0':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.main_menu_users()
            elif o == '2':
                self.crear_usario()
            elif o == '3':
                self.main_menu_admin()
            elif o == '0':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_sesion(self):
        self.view.ask('correo: ')
        correo = input()
        self.view.ask('contraseña: ')
        contrasenia = input()
        return[correo, contrasenia]

    def update_list(self, fs, vs):
        fields = []
        vals = []
        for f, v in zip(fs, vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    *************************
    * Controllers for users *
    *************************
    """

    def main_menu_users(self):
        sesion = self.in_sesion_usario()
        if type(sesion) == tuple:
            o = '100'
            while o != '0':
                self.view.main_menu_user()
                self.view.option('4')
                o = input()
                if o == '1':
                    self.read_funcion_fecha_horario()
                elif o == '2':
                    self.read_funcion_pelicula_titulo()
                elif o == '3':
                    self.usuario_menu(sesion)
                elif o == '4':
                    self.comprar_boleto(sesion)
                elif o == '5':
                    self.read_boletos_usuario(sesion)
                elif o == '0':
                    self.view.end_sesion()
                else:
                    self.view.not_valid_option()
        else:
            self.view.error_sesion(sesion)
        return

    def ask_usuario(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('correo: ')
        correo = input() 
        self.view.ask('contraseña: ')
        contrasenia = input()
        return [nombre, apellido, correo, contrasenia]

    def crear_usario(self):
        nombre, apellido, correo, contrasenia = self.ask_usuario()
        out = self.model.create_usuario(
            nombre, apellido, correo, contrasenia)
        print(out)
        if type(out) == int:
            self.view.ok(correo, 'ha dado de alta')
        else:
            if out.errno == 1062:
                self.view.error('EL USUARIO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO DAR DE ALTA EL USUARIO. REVISA')
        return

    def read_funcion_fecha_horario(self):
        self.view.ask('Ingresa fecha (YYYY-MM-DD): ')
        fecha = input()
        funciones = self.model.read_funcion_fecha_horario(fecha)
        if type(funciones) == list:
            self.view.show_funcion_header(
                ' Funciones para el dia '+fecha+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funcion_pelicula_titulo(self):
        self.view.ask('Ingresa el titulo de la pelicula: ')
        titulo = input()
        funciones = self.model.read_funcion_pelicula_titulo(titulo)
        if type(funciones) == list:
            self.view.show_funcion_header(
                ' Funciones para la pelicula '+titulo+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def in_sesion_usario(self):
        correo, contrasenia = self.ask_sesion()
        find = self.model.read_usuario_sesion(correo, contrasenia)
        if type(find) == tuple:
            self.view.iniciar_sesion(correo)
            return find
        else:
            self.view.error(find)
            return find

    """
    *************************
    * Controllers for users *
    *************************
    """

    def usuario_menu(self, usuario):
        o = '100'
        while o != '0':
            self.view.usuario_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_a_usuario(usuario)
            elif o == '2':
                self.update_usuario(usuario)
            elif o == '3':
                self.delete_usuario(usuario)
                self.view.end_sesion()
                return
            elif o == '0':
                self.view.end_sesion()
            else:
                self.view.not_valid_option()
        return

    def read_a_usuario(self, usuario):
        id_usuario = usuario[0]
        if type(usuario) == tuple:
            self.view.show_usuario_header(
                ' Datos del Usuario '+str(id_usuario)+' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error('USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA')
        return

    def update_usuario(self, usuario):
        id_usuario = usuario[0]
        if type(usuario) == tuple:
            self.view.show_usuario_header(' Datos del usuario '+str(id_usuario)+' ')
            self.view.show_a_usuario(usuario)
            self.view.show_usuario_midder()
            self.view.show_usuario_footer()
        else:
            if usuario == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL USUARIO. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('correo: ')
        correo = input()
        self.view.ask('contraseña: ')
        contrasenia = input()
        whole_vals = [nombre, apellido, correo, contrasenia]
        fields, vals = self.update_list(
            ['nombre', 'apellido', 'correo', 'contrasenia'], whole_vals)
        vals.append(id_usuario)
        vals = tuple(vals)
        out = self.model.update_usuario(fields, vals)
        if out == True:
            self.view.ok(id_usuario, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL USUARIO. REVISA')
        return

    def delete_usuario(self, usuario):
        id_usuario = usuario[0]
        count = self.model.delete_usuario(id_usuario)
        if count != 0:
            self.view.ok(str(id_usuario), 'borro')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL USUARIO. REVISA')
        return

    """
    ***************************
    * Controllers for tickets *
    ***************************
    """

    def comprar_boleto(self, usuario):
        id_usuario = usuario[0]
        self.view.ask('Clave de la funcion(S-H-P): ')
        clave = input()
        clave = clave.split('-')
        print(clave)
        id_sala = clave[0]
        id_horario = clave[1]
        id_pelicula = clave[2]
        asientos = self.model.read_asientos_sala(id_sala)
        if type(asientos) == list:
            self.view.show_asientos_header(' Asientos de la sala '+id_sala+' ')
            for asiento in asientos:
                self.view.show_a_asientos(asiento)
                self.view.show_asientos_midder()
            self.view.show_asientos_footer()
            self.view.ask('ID del asiento que quiere reservar: ')
            id_asientos = input()
            out = self.model.create_boletos(
                id_usuario, id_asientos, id_pelicula, id_horario)
            if type(out) == int:
                self.view.ok(str(id_usuario)+'-'+str(id_asientos)+'-' +
                             str(id_pelicula)+'-'+str(id_horario), 'agrego')
            else:
                if out.errno == 1062:
                    self.view.error('EL BOLETO ESTA REPETIDO')
                else:
                    self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA')
                return
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA')
        return

    def read_boletos_usuario(self, usuario):
        id_usuario = usuario[0]
        boletos = self.model.read_boletos_usuario(id_usuario)
        #print(boletos)
        if type(boletos) == list:
            self.view.show_boletos_header(
                ' Todos los Boletos comprados por el usuario '+str(id_usuario)+' ')
            for boleto in boletos:
                self.view.show_a_boletos(boleto)
                self.view.show_boletos_midder()
            self.view.show_boletos_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS. REVISA')
        return


    """
    **************************
    * Controllers for admins *
    **************************
    """

    def main_menu_admin(self):
        sesion = self.in_sesion_admin()
        if type(sesion) == tuple:
            o = '100'
            while o != '0':
                self.view.main_menu_admin()
                self.view.option('6')
                o = input()
                if o == '1':
                    self.main_menu_movie_db()
                elif o == '2':
                    self.sala_menu()
                elif o == '3':
                    self.horario_menu()
                elif o == '4':
                    self.asientos_menu()
                elif o == '5':
                    self.funcion_menu()
                elif o == '6':
                    self.administrador_menu()
                elif o == '0':
                    self.view.end_sesion()
                else:
                    self.view.not_valid_option()
        else:
            self.view.error_sesion(sesion)
        return

    def administrador_menu(self):
        o = '100'
        while o != '0':
            self.view.administrador_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_administrador()
            elif o == '2':
                self.read_a_administrador()
            elif o == '3':
                self.read_all_administrador()
            elif o == '4':
                self.read_administrador_correo()
            elif o == '5':
                self.read_administrador_nombre_completo()
            elif o == '6':
                self.update_administrador()
            elif o == '7':
                self.delete_administrador()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_administrador(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Primer apellido: ')
        apellido_1 = input()
        self.view.ask('Segundo apellido: ')
        apellido_2 = input()
        self.view.ask('Correo: ')
        correo = input()
        self.view.ask('Telefono: ')
        telefono = input()
        self.view.ask('Contrasenia: ')
        contrasenia = input()
        return [nombre, apellido_1, apellido_2, correo, telefono, contrasenia]

    def create_administrador(self):
        nombre, apellido_1, apellido_2, correo, telefono, contrasenia = self.ask_administrador()
        out = self.model.create_administrador(
            nombre, apellido_1, apellido_2, correo, telefono, contrasenia)
        if type(out) == int:
            self.view.ok(nombre+'|'+correo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ASMINISTRADOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ADMINISTRADOR. REVISA')
        return

    def read_a_administrador(self):
        self.view.ask('ID del administrador: ')
        id_administrador = input()
        administrador = self.model.read_a_administrador(id_administrador)
        if type(administrador) == tuple:
            self.view.show_administrador_header(
                ' Datos del Administrador '+id_administrador+' ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if administrador == None:
                self.view.error('ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
        return

    def read_all_administrador(self):
        administradores = self.model.read_all_administrador()
        if type(administradores) == list:
            self.view.show_administrador_header(' Todos los Administradores ')
            for administrador in administradores:
                self.view.show_a_administrador(administrador)
                self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINISTRADORES. REVISA')
        return

    def read_administrador_correo(self):
        self.view.ask('Correo: ')
        correo = input()
        administrador = self.model.read_administrador_correo(
            correo)
        if type(administrador) == tuple:
            self.view.show_administrador_header(' Datos del Administrador ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
        return

    def read_administrador_nombre_completo(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Primer apellido: ')
        apellido_1 = input()
        self.view.ask('Segundo apellido: ')
        apellido_2 = input()
        administradores = self.model.read_administrador_nombre_completo(
            nombre, apellido_1, apellido_2)
        if type(administradores) == list:
            self.view.show_administrador_header(' Administradores con el nombre '+ nombre+' '+apellido_1+' '+apellido_2+' ')
            for administrador in administradores:
                self.view.show_a_administrador(administrador)
                self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINISTRADORES. REVISA')
        return

    def update_administrador(self):
        self.view.ask('ID del administrador: ')
        id_administrador = input()
        administrador = self.model.read_a_administrador(id_administrador)
        if type(administrador) == tuple:
            self.view.show_administrador_header(' Datos del administrador '+id_administrador+' ')
            self.view.show_a_administrador(administrador)
            self.view.show_administrador_midder()
            self.view.show_administrador_footer()
        else:
            if administrador == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ADMINISTRADOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Nombre: ')
        nombre=input()
        self.view.ask('Primer apellido: ')
        apellido_1=input()
        self.view.ask('Segundo apellido: ')
        apellido_2=input()
        self.view.ask('Correo: ')
        correo=input()
        self.view.ask('Telefono: ')
        telefono=input()
        self.view.ask('Contrasenia: ')
        contrasenia=input()
        whole_vals = [nombre, apellido_1, apellido_2, correo, telefono, contrasenia]
        fields, vals = self.update_list(
            ['nombre', 'apellido_1', 'apellido_2', 'correo', 'telefono', 'contrasenia'], whole_vals)
        vals.append(id_administrador)
        vals = tuple(vals)
        out = self.model.update_administrador(fields, vals)
        if out == True:
            self.view.ok(id_administrador, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ADMINISTRADOR. REVISA')
        return

    def delete_administrador(self):
        self.view.ask('ID del administrador: ')
        id_administrador = input()
        if id_administrador == '1':
            self.view.error('NO SE PUEDE BORRAR EL ADMINISTRADOR PRINCIPAL')
            return
        count = self.model.delete_administrador(id_administrador)
        if count != 0:
            self.view.ok(id_administrador, 'borro')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ADMINISTRADOR. REVISA')
        return

    def in_sesion_admin(self):
        correo, contrasenia = self.ask_sesion()
        find = self.model.read_administrador_sesion(correo, contrasenia)
        if type(find) == tuple:
            self.view.iniciar_sesion(correo)
            return find
        else:
            self.view.error(find)
            return find

    """
    ****************************
    * Controllers for schedule *
    ****************************
    """

    def horario_menu(self):
        o = '100'
        while o != '0':
            self.view.horario_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_horario()
            elif o == '2':
                self.read_a_horario()
            elif o == '3':
                self.read_all_horario()
            elif o == '4':
                self.read_horario_particular()
            elif o == '5':
                self.read_horario_fecha()
            elif o == '6':
                self.update_horario()
            elif o == '7':
                self.delete_horario()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_horario(self):
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Hora de inicio: ')
        hora_inicio = input()
        return [fecha, hora_inicio]

    def create_horario(self):
        fecha, hora_inicio = self.ask_horario()
        out = self.model.create_horario(fecha, hora_inicio)
        if type(out) == int:
            self.view.ok(fecha+'va las '+hora_inicio, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL HORARIO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL HORARIO. REVISA')
        return

    def read_a_horario(self):
        self.view.ask('ID del horario: ')
        id_horario = input()
        horario = self.model.read_a_horario(id_horario)
        if type(horario) == tuple:
            self.view.show_horario_header(' Datos del Horario '+id_horario+' ')
            self.view.show_a_horario(horario)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            if horario == None:
                self.view.error('HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL HORARIO. REVISA')
        return

    def read_all_horario(self):
        horarios = self.model.read_all_horario()
        if type(horarios) == list:
            self.view.show_horario_header(' Todos los Horarios ')
            for horario in horarios:
                self.view.show_a_horario(horario)
                self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS HORARIOS. REVISA')
        return

    def read_horario_particular(self):
        fecha, hora_inicio = self.ask_horario()
        horario_part = self.model.read_horario_particular(fecha, hora_inicio)
        if type(horario_part) == tuple:
            self.view.show_horario_header(' Datos del Horario ')
            self.view.show_a_horario(horario_part)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL HORARIO. REVISA')
        return

    def read_horario_fecha(self):
        self.view.ask('Fecha: ')
        fecha = input()
        horarios = self.model.read_horario_fecha(fecha)
        if type(horarios) == list:
            self.view.show_horario_header(' Horarios con la fecha '+fecha+' ')
            for horario in horarios:
                self.view.show_a_horario(horario)
                self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS HORARIOS. REVISA')
        return

    def update_horario(self):
        self.view.ask('ID del horario: ')
        id_horario = input()
        horario = self.model.read_a_horario(id_horario)
        if type(horario) == tuple:
            self.view.show_horario_header(' Datos del horario '+id_horario+' ')
            self.view.show_a_horario(horario)
            self.view.show_horario_midder()
            self.view.show_horario_footer()
        else:
            if horario == None:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL HORARIO. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Fecha: ')
        fecha = input()
        self.view.ask('Hora de inicio: ')
        hora_inicio = input()
        whole_vals = [fecha, hora_inicio]
        fields, vals = self.update_list(
            ['fecha', 'hora_inicio'], whole_vals)
        vals.append(id_horario)
        vals = tuple(vals)
        out = self.model.update_horario(fields, vals)
        if out == True:
            self.view.ok(id_horario, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL HORARIO. REVISA')
        return

    def delete_horario(self):
        self.view.ask('ID del horario: ')
        id_horario = input()
        count = self.model.delete_horario(id_horario)
        if count != 0:
            self.view.ok(id_horario, 'borro')
        else:
            if count == 0:
                self.view.error('EL HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL HORARIO. REVISA')
        return

    """
    **************************
    * Controllers for saloon *
    **************************
    """

    def sala_menu(self):
        o = '100'
        while o != '0':
            self.view.sala_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_sala()
            elif o == '4':
                self.read_sala_nombre()
            elif o == '5':
                self.read_sala_tipo()
            elif o == '6':
                self.update_sala()
            elif o == '7':
                self.delete_sala()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_sala(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Escribe tipo (Normal|3D|IMAX|VIP): ')
        tipo = input()
        self.view.ask('Capacidad: ')
        capacidad = input()
        self.view.ask('Precio: ')
        precio = input()
        return [nombre, tipo, capacidad, precio]

    def create_sala(self):
        nombre, tipo, capacidad, precio = self.ask_sala()
        out = self.model.create_sala(nombre, tipo, capacidad, precio)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA SALA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA')
        return

    def read_a_sala(self):
        self.view.ask('ID del sala: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la Sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA')
        return

    def read_all_sala(self):
        salas = self.model.read_all_sala()
        if type(salas) == list:
            self.view.show_sala_header(' Todas las Salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA')
        return

    def read_sala_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        salas = self.model.read_sala_nombre(nombre)
        if type(salas) == list:
            self.view.show_sala_header(' Salas con el nombre '+nombre+' ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA')
        return

    def read_sala_tipo(self):
        self.view.ask('Escribe tipo (Normal|3D|IMAX|VIP): ')
        tipo = input()
        salas = self.model.read_sala_tipo(tipo)
        if type(salas) == list:
            self.view.show_sala_header(' Salas del tipo '+tipo+' ')
            for sala in salas:
                self.view.show_a_sala(sala)
                self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS HORARIOS. REVISA')
        return

    def update_sala(self):
        self.view.ask('ID de la sala: ')
        id_sala = input()
        sala = self.model.read_a_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header(' Datos de la Sala '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Escribe tipo (Normal|3D|IMAX|VIP): ')
        tipo = input()
        self.view.ask('Capacidad: ')
        capacidad = input()
        self.view.ask('Precio: ')
        precio = input()
        whole_vals = [nombre, tipo, capacidad, precio]
        fields, vals = self.update_list(
            ['nombre', 'tipo', 'capacidad', 'precio'], whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields, vals)
        if out == True:
            self.view.ok(id_sala, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA')
        return

    def delete_sala(self):
        self.view.ask('ID del sala: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala, 'borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA')
        return

    """
    ************************
    * Controllers for seat *
    ************************
    """

    def asientos_menu(self):
        o = '100'
        while o != '0':
            self.view.asientos_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_asientos()
            elif o == '2':
                self.read_a_asientos()
            elif o == '3':
                self.read_all_asientos()
            elif o == '4':
                self.read_asientos_particulares()
            elif o == '5':
                self.read_asientos_sala()
            elif o == '6':
                self.update_asientos()
            elif o == '7':
                self.delete_asientos()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_asientos(self):
        self.view.ask('Fila: ')
        fila = input()
        self.view.ask('Numero: ')
        numero = input()
        self.view.ask('Ocupado (1-SI|0-NO): ')
        ocupado = input()
        self.view.ask('ID sala: ')
        id_sala = input()
        return [fila, numero, ocupado, id_sala]

    def create_asientos(self):
        fila, numero, ocupado, id_sala = self.ask_asientos()
        out = self.model.create_asientos(fila, numero, ocupado, id_sala)
        if type(out) == int:
            self.view.ok(fila+''+numero, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ASIENTO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ASIENTO. REVISA')
        return

    def read_a_asientos(self):
        self.view.ask('ID del asiento: ')
        id_asientos = input()
        asientos = self.model.read_a_asientos(id_asientos)
        if type(asientos) == tuple:
            self.view.show_asientos_header(' Datos del Asiento '+id_asientos+' ')
            self.view.show_a_asientos(asientos)
            self.view.show_asientos_midder()
            self.view.show_asientos_footer()
        else:
            if asientos == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA')
        return

    def read_all_asientos(self):
        asientos = self.model.read_all_asientos()
        print(asientos)
        if type(asientos) == list:
            self.view.show_asientos_header(' Todos los Asientos ')
            for asiento in asientos:
                self.view.show_a_asientos(asiento)
                self.view.show_asientos_midder()
            self.view.show_asientos_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA')
        return

    def read_asientos_particulares(self):
        self.view.ask('Fila: ')
        fila = input()
        self.view.ask('Numero: ')
        numero = input()
        asientos = self.model.read_asientos_particulares(
            fila, numero)
        if type(asientos) == list:
            self.view.show_asientos_header(
                ' Asientos con la fila '+fila+' y numero '+numero+' ')
            for asiento in asientos:
                self.view.show_a_asientos(asiento)
                self.view.show_asientos_midder()
            self.view.show_asientos_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA')
        return

    def read_asientos_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        asientos = self.model.read_asientos_sala(id_sala)
        if type(asientos) == list:
            self.view.show_asientos_header(' Asientos de la sala '+id_sala+' ')
            for asiento in asientos:
                self.view.show_a_asientos(asiento)
                self.view.show_asientos_midder()
            self.view.show_asientos_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS. REVISA')
        return

    def update_asientos(self):
        self.view.ask('ID del asiento: ')
        id_asientos = input()
        asientos = self.model.read_a_asientos(id_asientos)
        if type(asientos) == tuple:
            self.view.show_asientos_header(
                ' Datos del asiento '+id_asientos+' ')
            self.view.show_a_asientos(asientos)
            self.view.show_asientos_midder()
            self.view.show_asientos_footer()
        else:
            if asientos == None:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Fila: ')
        fila = input()
        self.view.ask('Numero: ')
        numero = input()
        self.view.ask('Ocupado (1-SI|0-NO): ')
        ocupado = input()
        self.view.ask('ID sala: ')
        id_sala = input()
        whole_vals = [fila, numero, ocupado, id_sala]
        fields, vals = self.update_list(
            ['fila', 'numero', 'ocupado', 'id_sala'], whole_vals)
        vals.append(id_asientos)
        vals = tuple(vals)
        out = self.model.update_asientos(fields, vals)
        if out == True:
            self.view.ok(id_asientos, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ASIENTO. REVISA')
        return

    def delete_asientos(self):
        self.view.ask('ID del asiento: ')
        id_asientos = input()
        count = self.model.delete_asientos(id_asientos)
        if count != 0:
            self.view.ok(id_asientos, 'borro')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ASIENTO. REVISA')
        return

    """
    ***********************************
    * Controllers for cinema function *
    ***********************************
    """

    def funcion_menu(self):
        o = '100'
        while o != '0':
            self.view.funcion_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.read_all_peliculas()
            elif o == '2':
                self.read_all_horario()
            elif o == '3':
                self.read_all_sala()
            elif o == '4':
                self.create_funcion()
            elif o == '5':
                self.read_a_funcion()
            elif o == '6':
                self.read_all_funcion()
            elif o == '7':
                self.read_funcion_pelicula()
            elif o == '8':
                self.read_funcion_horario()
            elif o == '9':
                self.read_funcion_sala()
            elif o == '10':
                self.delete_funcion()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_funcion(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        self.view.ask('ID horario: ')
        id_horario = input()
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        return [id_sala, id_horario, id_pelicula]

    def create_funcion(self):
        id_sala, id_horario, id_pelicula = self.ask_funcion()
        out = self.model.create_funcion(id_sala, id_horario, id_pelicula)
        if type(out) == int:
            self.view.ok(id_sala+' '+id_horario+' '+id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA FUNCION ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA')
        return

    def read_a_funcion(self):
        id_sala, id_horario, id_pelicula = self.ask_funcion()
        funcion = self.model.read_a_funcion(id_sala, id_horario, id_pelicula)
        if type(funcion) == tuple:
            self.view.show_funcion_header(
                ' Datos de la funcion '+id_sala+'|'+id_horario+'|'+id_pelicula+' ')
            self.view.show_a_funcion(funcion)
            self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            if funcion == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA')
        return

    def read_all_funcion(self):
        funciones = self.model.read_all_funcion()
        if type(funciones) == list:
            self.view.show_funcion_header(' Todas las Funciones ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funcion_pelicula(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        funciones = self.model.read_funcion_pelicula(id_pelicula)
        if type(funciones) == list:
            self.view.show_funcion_header(' Funciones de la peilicula '+id_pelicula+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funcion_horario(self):
        self.view.ask('ID horario: ')
        id_horario = input()
        funciones = self.model.read_funcion_horario(id_horario)
        if type(funciones) == list:
            self.view.show_funcion_header(' Funciones del horario '+id_horario+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def read_funcion_sala(self):
        self.view.ask('ID sala: ')
        id_sala = input()
        funciones = self.model.read_funcion_sala(id_sala)
        if type(funciones) == list:
            self.view.show_funcion_header(' Funciones de la sala '+id_sala+' ')
            for funcion in funciones:
                self.view.show_a_funcion(funcion)
                self.view.show_funcion_midder()
            self.view.show_funcion_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA')
        return

    def delete_funcion(self):
        id_sala, id_horario, id_pelicula = self.ask_funcion()
        count = self.model.delete_funcion(id_sala, id_horario, id_pelicula)
        if count != 0:
            self.view.ok(id_sala+'|'+id_horario+'|'+id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION. REVISA')
        return

    """
    ********************************
    * General movie DB controllers *
    ********************************
    """

    def main_menu_movie_db(self):
        o = '100'
        while o != '0':
            self.view.main_menu_movie_db()
            self.view.option('4')
            o = input()
            if o == '1':
                self.pais_menu()
            elif o == '2':
                self.genero_menu()
            elif o == '3':
                self.directores_menu()
            elif o == '4':
                self.peliculas_menu()
            elif o == '0':
                self.view.end_movie_db()
            else:
                self.view.not_valid_option()
        return

    """
    *****************************
    * Controllers for countries *
    *****************************
    """

    def pais_menu(self):
        o = '100'
        while o != '0':
            self.view.pais_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_pais()
            elif o == '2':
                self.read_a_pais()
            elif o == '3':
                self.read_all_pais()
            elif o == '4':
                self.read_pais_nombre()
            elif o == '5':
                self.update_pais()
            elif o == '6':
                self.delete_pais()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def create_pais(self):
        self.view.ask('Nombre: ')
        nombre = input()
        out = self.model.create_pais(nombre)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL PAIS ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL PAIS. REVISA')
        return

    def read_a_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        pais = self.model.read_a_pais(id_pais)
        if type(pais) == tuple:
            self.view.show_pais_header(' Datos del Pais '+id_pais+' ')
            self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            if pais == None:
                self.view.error('PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PAIS. REVISA')
        return

    def read_all_pais(self):
        paises = self.model.read_all_pais()
        if type(paises) == list:
            self.view.show_pais_header(' Todos los Paises ')
            for pais in paises:
                self.view.show_a_pais(pais)
                self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PAISES. REVISA')
        return

    def read_pais_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        paises = self.model.read_pais_nombre(nombre)
        if type(paises) == list:
            self.view.show_pais_header(' Paises con el nombre de '+nombre+' ')
            for pais in paises:
                self.view.show_a_pais(pais)
                self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PAISES. REVISA')
        return

    def update_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        pais = self.model.read_a_pais(id_pais)
        if type(pais) == tuple:
            self.view.show_pais_header(' Nombre del pais '+id_pais+' ')
            self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            if pais == None:
                self.view.error('EL PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PAIS. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Nombre: ')
        nombre = input()
        nombre = [nombre]
        fields, vals = self.update_list(['nombre'], nombre)
        vals.append(id_pais)
        vals = tuple(vals)
        out = self.model.update_pais(fields, vals)
        if out == True:
            self.view.ok(id_pais, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL PAIS. REVISA')
        return

    def delete_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        count = self.model.delete_pais(id_pais)
        if count != 0:
            self.view.ok(id_pais, 'borro')
        else:
            if count == 0:
                self.view.error('EL PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL PAIS. REVISA')
        return

    """
    **************************
    * Controllers for genres *
    **************************
    """

    def genero_menu(self):
        o = '100'
        while o != '0':
            self.view.genero_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_genero()
            elif o == '2':
                self.read_a_genero()
            elif o == '3':
                self.read_all_genero()
            elif o == '4':
                self.read_genero_nombre()
            elif o == '5':
                self.read_genero_sub_gen()
            elif o == '6':
                self.update_genero()
            elif o == '7':
                self.delete_genero()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_genero(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Subgenero: ')
        subgenero = input()
        return[nombre, subgenero]

    def create_genero(self):
        nombre, subgenero = self.ask_genero()
        out = self.model.create_genero(nombre, subgenero)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL GENERO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL GENERO. REVISA')
        return

    def read_a_genero(self):
        self.view.ask('ID del genero: ')
        id_genero = input()
        genero = self.model.read_a_genero(id_genero)
        if type(genero) == tuple:
            self.view.show_genero_header(' Datos del Pais '+id_genero+' ')
            self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            if genero == None:
                self.view.error('GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL GENERO. REVISA')
        return

    def read_all_genero(self):
        generos = self.model.read_all_genero()
        if type(generos) == list:
            self.view.show_genero_header(' Todos los Generos ')
            for genero in generos:
                self.view.show_a_genero(genero)
                self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def read_genero_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        generos = self.model.read_genero_nombre(nombre)
        if type(generos) == list:
            self.view.show_genero_header(
                ' Generos con el nombre de '+nombre+' ')
            for genero in generos:
                self.view.show_a_genero(genero)
                self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def read_genero_sub_gen(self):
        self.view.ask('Subgenero: ')
        subgenero = input()
        generos = self.model.read_genero_sub_gen(subgenero)
        if type(generos) == list:
            self.view.show_genero_header(
                ' Generos con el subgenero de '+subgenero+' ')
            for genero in generos:
                self.view.show_a_genero(genero)
                self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def update_genero(self):
        self.view.ask('ID del genero a modificar: ')
        id_genero = input()
        genero = self.model.read_a_genero(id_genero)
        if type(genero) == tuple:
            self.view.show_genero_header(' Datos del genero '+id_genero+' ')
            self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL GENERO. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_genero()
        fields, vals = self.update_list(['nombre', 'sub_gen'], whole_vals)
        vals.append(id_genero)
        vals = tuple(vals)
        out = self.model.update_genero(fields, vals)
        if out == True:
            self.view.ok(id_genero, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL GENERO. REVISA')
        return

    def delete_genero(self):
        self.view.ask('ID del genero: ')
        id_genero = input()
        count = self.model.delete_genero(id_genero)
        if count != 0:
            self.view.ok(id_genero, 'borro')
        else:
            if count == 0:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL GENERO. REVISA')
        return


    """
    *****************************
    * Controllers for directors *
    *****************************
    """

    def directores_menu(self):
        o = '100'
        while o != '0':
            self.view.directores_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_directores()
            elif o == '2':
                self.read_a_directores()
            elif o == '3':
                self.read_all_directores()
            elif o == '4':
                self.read_directores_nombre()
            elif o == '5':
                self.read_directores_apellido()
            elif o == '6':
                self.read_directores_anio_act_in()
            elif o == '7':
                self.read_directores_anio_act_fin()
            elif o == '8':
                self.read_directores_anio_act_range()
            elif o == '9':
                self.update_directores()
            elif o == '10':
                self.delete_directores()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_directores(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('Año de inicio: ')
        anio_act_in = input()
        self.view.ask('Año fin: ')
        anio_act_fin = input()
        return [nombre, apellido, anio_act_in, anio_act_fin]

    def create_directores(self):
        nombre, apellido, anio_act_in, anio_act_fin = self.ask_directores()
        out = self.model.create_directores(
            nombre, apellido, anio_act_in, anio_act_fin)
        if type(out) == int:
            self.view.ok(nombre+' '+apellido, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL DIRECTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL DIRECTOR. REVISA')
        return

    def read_a_directores(self):
        self.view.ask('ID director: ')
        id_director = input()
        director = self.model.read_a_directores(id_director)
        if type(director) == tuple:
            self.view.show_directores_header(
                ' Datos del director '+id_director+' ')
            self.view.show_a_directores(director)
            self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_all_directores(self):
        directores = self.model.read_all_directores()
        if type(directores) == list:
            self.view.show_directores_header(' Todos los directores ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR')
        return

    def read_directores_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        directores = self.model.read_directores_nombre(nombre)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que tienen el nombre '+nombre+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_apellido(self):
        self.view.ask('Apellido: ')
        apellido = input()
        directores = self.model.read_directores_apellido(apellido)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que tienen el apellido '+apellido+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_in(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = input()
        directores = self.model.read_directores_anio_act_in(anio_act_in)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que su carrera empezo en '+anio_act_in+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_fin(self):
        self.view.ask('Año fin: ')
        anio_act_fin = input()
        directores = self.model.read_directores_anio_act_fin(anio_act_fin)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que su carrera finalizo en '+anio_act_fin+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_range(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = input()
        self.view.ask('Año fin: ')
        anio_act_fin = input()
        directores = self.model.read_directores_anio_act_range(
            anio_act_in, anio_act_fin)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores donde su carrera se encuentra entre '+anio_act_in+' y '+anio_act_fin+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def update_directores(self):
        self.view.ask('ID del director modificar: ')
        id_director = input()
        director = self.model.read_a_directores(id_director)
        if type(director) == tuple:
            self.view.show_directores_header(
                ' Datos del director '+id_director+' ')
            self.view.show_a_directores(director)
            self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_directores()
        fields, vals = self.update_list(
            ['nombre', 'apellido', 'id_alma_mater', 'anio_act_in', 'anio_act_fin'], whole_vals)
        vals.append(id_director)
        vals = tuple(vals)
        out = self.model.update_directores(fields, vals)
        if out == True:
            self.view.ok(id_director, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL DIRECTOR. REVISA')
        return

    def delete_directores(self):
        self.view.ask('ID del director: ')
        id_director = input()
        count = self.model.delete_directores(id_director)
        if count != 0:
            self.view.ok(id_director, 'borro')
        else:
            if count == 0:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL DIRECTOR. REVISA')
        return


    """
    ***************************
    * Controllers for movies  *
    ***************************
    """

    def peliculas_menu(self):
        o = '100'
        while o != '0':
            self.view.peliculas_menu()
            self.view.option('12')
            o = input()
            if o == '1':
                self.create_peliculas()
            elif o == '2':
                self.read_a_peliculas()
            elif o == '3':
                self.read_all_peliculas()
            elif o == '4':
                self.read_peliculas_titulo()
            elif o == '5':
                self.read_peliculas_id_genero()
            elif o == '6':
                self.read_peliculas_id_director()
            elif o == '7':
                self.read_peliculas_anio()
            elif o == '8':
                self.read_peliculas_anio_range()
            elif o == '9':
                self.read_peliculas_id_pais()
            elif o == '10':
                self.read_peliculas_calif()
            elif o == '11':
                self.update_peliculas()
            elif o == '12':
                self.delete_peliculas()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_peliculas(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('ID Genero: ')
        id_genero = input()
        self.view.ask('ID Director: ')
        id_director = input()
        self.view.ask('Año de lanzamiento: ')
        anio = input()
        self.view.ask('ID Pais: ')
        id_pais = input()
        if id_pais == 'None':
            id_pais = None
        self.view.ask('Calificacion: ')
        calif = input()
        return [titulo, id_genero, id_director, anio, id_pais, calif]

    def create_peliculas(self):
        titulo, id_genero, id_director, anio, id_pais, calif = self.ask_peliculas()
        out = self.model.create_peliculas(
            titulo, id_genero, id_director, anio, id_pais, calif)
        if type(out) == int:
            self.view.ok(titulo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA PELICULA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA')
        return

    def read_a_peliculas(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_peliculas(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_peliculas_header(
                ' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_peliculas(pelicula)
            self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_peliculas_header(' Todas las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS')
        return

    def read_peliculas_titulo(self):
        self.view.ask('Titulo: ')
        titulo = input()
        peliculas = self.model.read_peliculas_titulo(titulo)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen el titulo '+titulo+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_id_genero(self):
        self.view.ask('ID Genero: ')
        id_genero = input()
        peliculas = self.model.read_peliculas_id_genero(id_genero)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen el genero '+id_genero+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_id_director(self):
        self.view.ask('ID Director: ')
        id_director = input()
        peliculas = self.model.read_peliculas_id_director(id_director)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen como director '+id_director+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_anio(self):
        self.view.ask('Año de lanzamiento: ')
        anio = input()
        peliculas = self.model.read_peliculas_anio(anio)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que se publicaron en el año '+anio+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_anio_range(self):
        self.view.ask('Desde el año: ')
        anio_in = input()
        self.view.ask('Hasta el año: ')
        anio_fin = input()
        peliculas = self.model.read_peliculas_anio_range(
            anio_in, anio_fin)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas donde su año de lanzamiento se encuentra entre '+anio_in+' y '+anio_fin+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_peliculas_id_pais(self):
        self.view.ask('ID Pais: ')
        id_pais = input()
        peliculas = self.model.read_peliculas_id_pais(id_pais)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas donde su pais se filmo en '+id_pais+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_peliculas_calif(self):
        self.view.ask('Calificacion: ')
        calif = input()
        peliculas = self.model.read_peliculas_calif(calif)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que su calificacion fue '+calif+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def update_peliculas(self):
        self.view.ask('ID de la pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.read_a_peliculas(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_peliculas_header(
                ' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_peliculas(pelicula)
            self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_peliculas()
        fields, vals = self.update_list(
            ['titulo', 'id_genero', 'id_director', 'anio', 'id_pais', 'calif'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_peliculas(fields, vals)
        if out == True:
            self.view.ok(id_pelicula, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA')
        return

    def delete_peliculas(self):
        self.view.ask('ID de la pelicula: ')
        id_pelicula = input()
        count = self.model.delete_peliculas(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA')
        return
