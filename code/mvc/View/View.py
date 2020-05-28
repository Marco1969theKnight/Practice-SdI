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
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.')
        print('=.   --    Menu Principal   --    .=')
        print('=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.')
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
        print('=========================================')
        print('=   --   Menu Principal Usuarios   --   =')
        print('=========================================')
        print('1. Consultar funciones por dia')
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
        print('==============================================')
        print('=   --   Menu Principal Administrador   --   =')
        print('==============================================')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Horarios')
        print('4. Asientos')
        print('5. Funciones')
        print('6. Administradores')
        print('0. Salir')

    """
    *******************
    * Views for admin *
    *******************
    """

    def administrador_menu(self):
        print('*************************************************')
        print('*     --     Submenu Administradores     --     *')
        print('*************************************************')
        print('1. Crear administrador')
        print('2. Ver administrador')
        print('3. Ver todos los administradores')
        print('4. Ver administrador por correo')
        print('5. Ver administrador por nombre completo')
        print('6. Actualizar administrador')
        print('7. Eliminar administrador')
        print('0. Salir')

    def show_a_administrador(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Primer apellido: ', record[2])
        print('Segundo apellido: '+record[3])
        print('Correo: ', record[4])
        print('Telefono: ', record[5])
        print('Contrasenia: ', record[6])

    def show_administrador_header(self, header):
        print(header.center(70, '*'))
        print('-'*70)

    def show_administrador_midder(self):
        print('-'*70)

    def show_administrador_footer(self):
        print('*'*70)

    """
    **********************
    * Views for Schedule *
    **********************
    """

    def horario_menu(self):
        print('**********************************')
        print('*   --   Submenu Horarios   --   *')
        print('**********************************')
        print('1. Agregar horario')
        print('2. Mostrar horario')
        print('3. Mostrar todos los horarios')
        print('4. Mostrar horario por fecha y hora de inicio')
        print('5. Mostrar horario por fecha')
        print('6. Actualizar horario')
        print('7. Eliminar horario')
        print('0. Regresar')

    def show_a_horario(self, record):
        print(f'{record[0]:<6}|{str(record[1]):<10}|{str(record[2]):<8}')

    def show_horario_header(self, header):
        print(header.center(56, '*'))
        print('ID horario'.ljust(6)+'|'+'fecha'.ljust(10)+'|'+'hora de inicio'.ljust(8))
        print('-'*56)

    def show_horario_midder(self):
        print('-'*56)

    def show_horario_footer(self):
        print('*'*56)

    """
    ********************
    * Views for Saloon *
    ********************
    """

    def sala_menu(self):
        print('******************************')
        print('*   --   Submenu Sala   --   *')
        print('******************************')
        print('1. Agregar sala')
        print('2. Mostrar sala')
        print('3. Mostrar todas las salas')
        print('4. Mostrar sala por nombre')
        print('5. Mostrar sala por tipo')
        print('6. Actualizar sala')
        print('7. Eliminar sala')
        print('0. Regresar')

    def show_a_sala(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Tipo: ', record[2])
        print('Capacidad: ', record[3])
        print('Precio: ', record[4])

    def show_sala_header(self, header):
        print(header.center(29, '*'))
        print('-'*29)

    def show_sala_midder(self):
        print('-'*29)

    def show_sala_footer(self):
        print('*'*29)

    """
    ******************
    * Views for Seat *
    ******************
    """

    def asientos_menu(self):
        print('**********************************')
        print('*   --   Submenu Asientos   --   *')
        print('**********************************')
        print('1. Agregar asiento')
        print('2. Mostrar asiento')
        print('3. Mostrar todos los asiento')
        print('4. Mostrar asientos por fila y numero')
        print('5. Mostrar asientos por sala')
        print('6. Actualizar asiento')
        print('7. Eliminar asiento')
        print('0. Regresar')

    def show_a_asientos(self, record):
        print('ID: ', record[0])
        print('Fila: ', record[1])
        print('Numero: ', record[2])
        print('Ocupado: ', record[3])
        print('ID sala: ', record[4])
        print('Sala: ', record[5])

    def show_asientos_header(self, header):
        print(header.center(18, '*'))
        print('-'*18)

    def show_asientos_midder(self):
        print('-'*18)

    def show_asientos_footer(self):
        print('*'*18)

    """
    *****************************
    * Views for Cinema function *
    *****************************
    """

    def funcion_menu(self):
        print('***********************************')
        print('*   --   Submenu Funciones   --   *')
        print('***********************************')
        print('1. Ver lista peliculas')
        print('2. Ver lista horarios')
        print('3. Ver lista salas')
        print('4. Agregar funcion')
        print('5. Mostrar funcion')
        print('6. Mostrar todas las funciones')
        print('7. Mostrar funciones por pelicula')
        print('8. Mostrar funciones por horarios')
        print('9. Mostrar funciones por salas')
        print('10. Eliminar funcion')
        print('0. Regresar')

    def show_a_funcion(self, record):
        print('ID Sala: ', record[0])
        print('Nombre: ', record[1])
        print('Tipo: ', record[2])
        print('Capacidad: ', record[3])
        print('Precio: ', record[4])
        print(f'{record[5]:<6}|{str(record[6]):<10}|{str(record[7]):<8}')
        print('ID Pelicula: ', record[8])
        print('Titulo: ', record[9])
        print('Genero: ', record[10])
        print('Director: '+record[11]+' '+record[12])
        print('Año: ', record[13])
        print('Pais: ', record[14])
        print('Calificacion: ', record[15])

    def show_funcion_header(self, header):
        print(header.center(18, '*'))
        print('-'*113)

    def show_funcion_midder(self):
        print('-'*113)

    def show_funcion_footer(self):
        print('*'*113)

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

    def error_sesion(self, err):
        print(' ¡Error al iniciar sesion! '.center(len(err)+4, '-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

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
