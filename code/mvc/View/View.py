class View:
    """
    **************************
    * A view for a cinema DB *
    **************************
    """

    def start(self):
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=')
        print('=.         ¡Bienvenido a nuestro cine!         .=')
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=')

    def end(self):
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=')
        print('=.  Que tengas un buen dia ¡Hasta la proxima!  .=')
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=')

    def main_menu(self):
        print('================================')
        print('=   --   Menu Principal   --   =')
        print('================================')
        print('1. Iniciar sesion usuario')
        print('2. Crear cuenta usuario')
        print('3. Iniciar sesion administrador')
        print('0. Salir')

    def end_sesion(self):
        print('==================================================')
        print('=    Que tengas un buen dia ¡Hasta la proxima!   =')
        print('==================================================')

    """
    ***********************
    * Views for user menu *
    ***********************
    """

    def main_menu_user(self):
        print('*****************************************')
        print('*   --   Menu Principal Usuarios   --   *')
        print('*****************************************')
        print('1. Consultar funciones por semana')
        print('2. Consultar funciones por pelicula')
        print('3. Ajustes de perfil')
        print('4. comprar boleto')
        print('0. Salir')

    """
    ************************
    * Views for admin menu *
    ************************
    """

    def main_menu_admin(self):
        print('**********************************************')
        print('*   --   Menu Principal Administrador   --   *')
        print('**********************************************')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Horarios')
        print('4. Asientos')
        print('5. Funciones')
        print('6. Administradores')
        print('0. Salir')

    """
    *************************
    * A view for a movie DB *
    *************************
    """

    def start_movie_db(self):
        print('==================================================')
        print('= ¡Bienvenido a nuestra biblioteca de peliculas! =')
        print('==================================================')

    def end_movie_db(self):
        print('==================================================')
        print('=    Que tengas un buen dia ¡Hasta la proxima!   =')
        print('==================================================')

    def main_menu_movie_db(self):
        print('******************************************')
        print('*   --   Menu Principal Peliculas   --   *')
        print('******************************************')
        print('1. Paises')
        print('2. Generos')
        print('3. Directores')
        print('4. Peliculas')
        print('0. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end='')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta otra opcion')

    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def iniciar_sesion(self, correo):
        print('+'*(len(str(correo))+25))
        print('+ ¡'+str(correo)+' ha iniciado sesion! +')
        print('+'*(len(str(correo))+25))

    def error(self, err):
        print(' ¡Error! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ***********************
    * Views for countries *
    ***********************
    """

    def pais_menu(self):
        print('********************************')
        print('*   --   Submenu Paises   --   *')
        print('********************************')
        print('1. Agregar pais')
        print('2. Mostrar pais')
        print('3. Mostrar todos los paises')
        print('4. Mostrar pais por nombre')
        print('5. Actualizar nombre del pais')
        print('6. Eliminar pais')
        print('0. Regresar')

    def show_a_pais(self, record):
        print(f'{record[0]:<6}|{record[1]:<30}')

    def show_pais_header(self, header):
        print(header.center(38, '*'))
        print('ID Pais'.ljust(6)+'|'+'Nombre'.ljust(30))
        print('-'*38)

    def show_pais_midder(self):
        print('-'*38)

    def show_pais_footer(self):
        print('*'*38)

    """
    ********************
    * Views for genres *
    ********************
    """

    def genero_menu(self):
        print('*********************************')
        print('*   --   Submenu Generos   --   *')
        print('*********************************')
        print('1. Agregar genero')
        print('2. Mostrar genero')
        print('3. Mostrar todos los generos')
        print('4. Mostrar generos por nombre')
        print('5. Mostrar generos por subgenero')
        print('6. Actualizar genero')
        print('7. Eliminar genero')
        print('0. Regresar')

    def show_a_genero(self, record):
        print(f'{record[0]:<6}|{record[1]:<30}|{record[2]:<30}')

    def show_genero_header(self, header):
        print(header.center(68, '*'))
        print('ID Genero'.ljust(6)+'|' +
              'Nombre'.ljust(30)+'|'+'Subgenero'.ljust(30))
        print('-'*68)

    def show_genero_midder(self):
        print('-'*68)

    def show_genero_footer(self):
        print('*'*68)

    """
    ***********************
    * Views for directors *
    ***********************
    """

    def directores_menu(self):
        print('************************************************')
        print('*      --      Submenu Directores      --      *')
        print('************************************************')
        print('1. Agregar director')
        print('2. Mostrar director')
        print('3. Mostrar todos los directores')
        print('4. Mostrar directores por nombre')
        print('5. Mostrar directores por apellido')
        print('6. Mostrar directores por año inical de carrera')
        print('7. Mostrar directores por año final de carrera')
        print('8. Mostrar directores por rango de años')
        print('9. Actualizar director')
        print('10. Eliminar director')
        print('0. Regresar')

    def show_a_directores(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])
        print('Año de inicio de carrera: ', record[3])
        print('Año final de carrera: ', record[4])

    def show_directores_header(self, header):
        print(header.center(62, '*'))
        print('-'*62)

    def show_directores_midder(self):
        print('-'*62)

    def show_directores_footer(self):
        print('*'*62)


    """
    ********************
    * Views for movies *
    ********************
    """

    def peliculas_menu(self):
        print('***********************************************')
        print('*      --      Submenu peliculas      --      *')
        print('***********************************************')
        print('1. Agregar pelicula')
        print('2. Mostrar pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por titulo')
        print('5. Mostrar peliculas por genero')
        print('6. Mostrar peliculas por director')
        print('7. Mostrar peliculas por año')
        print('8. Mostrar peliculas por rango de años')
        print('9. Mostrar peliculas por pais')
        print('10. Mostrar peliculas por calificacion')
        print('11. Actualizar pelicula')
        print('12. Eliminar pelicula')
        print('0. Regresar')

    def show_a_peliculas(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Genero: ', record[2])
        print('Director: '+record[3]+' '+record[4])
        print('Año: ', record[5])
        print('Pais: ', record[6])
        print('Calificacion: ', record[7])

    def show_peliculas_header(self, header):
        print(header.center(113, '*'))
        print('-'*113)

    def show_peliculas_midder(self):
        print('-'*113)

    def show_peliculas_footer(self):
        print('*'*113)
