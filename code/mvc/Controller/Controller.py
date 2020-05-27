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
        if sesion == True:
            o = '100'
            while o != '0':
                self.view.main_menu_user()
                self.view.option('3')
                o = input()
                if o == '1':
                    self.view.end_sesion()
                elif o == '2':
                    self.view.end_sesion()
                elif o == '3':
                    self.view.end_sesion()
                elif o == '4':
                    self.view.end_sesion()
                elif o == '0':
                    self.view.end_sesion()
                else:
                    self.view.not_valid_option()
        else:
            self.view.not_valid_option()
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

    def in_sesion_usario(self):
        correo, contrasenia = self.ask_sesion()
        find = self.model.read_usuario_sesion(correo, contrasenia)
        if type(find) == tuple:
            self.view.iniciar_sesion(correo)
            return True
        else:
            self.view.error(find)
            return False

    """
    **************************
    * Controllers for admins *
    **************************
    """

    def main_menu_admin(self):
        sesion = self.in_sesion_admin()
        if sesion == True:
            o = '100'
            while o != '0':
                self.view.main_menu_user()
                self.view.option('3')
                o = input()
                if o == '1':
                    self.view.end_sesion()
                elif o == '2':
                    self.view.end_sesion()
                elif o == '3':
                    self.view.end_sesion()
                elif o == '4':
                    self.view.end_sesion()
                elif o == '5':
                    self.view.end_sesion()
                elif o == '6':
                    self.view.end_sesion()
                elif o == '0':
                    self.view.end_sesion()
                else:
                    self.view.not_valid_option()
        else:
            self.view.not_valid_option()
        return

    def in_sesion_admin(self):
        correo, contrasenia = self.ask_sesion()
        find = self.model.read_administrador_sesion(correo, contrasenia)
        if type(find) == tuple:
            self.view.iniciar_sesion(correo)
            return True
        else:
            self.view.error(find)
            return False

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
        print(nombre)
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
