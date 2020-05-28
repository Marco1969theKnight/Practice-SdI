create database if not exists cine_db;

use cine_db;

create table if not exists pais(
	id_pais int not null auto_increment,
    nombre varchar(30) not null,

    primary key(id_pais)
) engine = INNODB; 

create table if not exists genero(
	id_genero int not null auto_increment,
    nombre varchar(30) not null,
    sub_gen varchar(30),
    
    primary key(id_genero)
) engine = INNODB;

create table if not exists directores ( 
	id_director int not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    anio_act_in year not null,
    anio_act_fin year not null,
    
    primary key(id_director)
) engine=INNODB;

create table if not exists peliculas(
	id_pelicula int not null auto_increment,
    titulo varchar(40) not null,
    id_genero int not null,
    id_director int not null,
    anio year not null,
    id_pais int,
    calif int not null,
    
    primary key(id_pelicula),
    
    constraint fk_id_genero foreign key(id_genero)
		references genero(id_genero)
        on delete cascade
        on update cascade,
        
	constraint fk_id_director foreign key(id_director)
		references directores(id_director)
        on delete cascade
        on update cascade,
        
	constraint fk_id_pais_peliculas foreign key(id_pais)
		references pais(id_pais)
        on delete set null
        on update cascade
)engine=INNODB;

create table if not exists administrador(
    id_administrador int not null auto_increment,
    nombre varchar(50) not null,
    apellido_1 varchar(50) not null,
    apellido_2 varchar(50) not null,
    correo varchar(50) not null,
    telefono varchar(10),
    contrasenia varchar(50) not null,

    primary key(id_administrador)
)engine=INNODB;

create table if not exists usuario(
    id_usuario int not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    correo varchar(50) not null,
    contrasenia varchar(50) not null,

    primary key(id_usuario)
)engine=INNODB;

create table if not exists horario(
    id_horario int not null auto_increment,
    fecha date,
    hora_inicio time,

    primary key(id_horario),

    CONSTRAINT UC_horario UNIQUE (fecha,hora_inicio)
)engine=INNODB;

create table if not exists sala(
    id_sala int not null auto_increment,
    nombre varchar(10),
    tipo set('Normal', '3D', 'IMAX', 'VIP'),
    capacidad int,
    precio decimal(16,2),

    primary key(id_sala)
)engine=INNODB;

create table if not exists asientos(
    id_asientos int not null auto_increment,
    fila varchar(1),
    numero int,
    ocupado bool,
    id_sala int not null,

    primary key(id_asientos),

    CONSTRAINT UC_asiento UNIQUE (fila ,numero, id_sala),

    constraint fk_sala foreign key(id_sala)
		references sala(id_sala)
        on delete cascade
        on update cascade
)engine=INNODB;

create table if not exists funcion(
    id_sala int not null,
    id_horario int not null,
    id_pelicula int not null,

    primary key(id_sala, id_horario, id_pelicula),

    constraint fk_f_sala foreign key(id_sala)
		references sala(id_sala)
        on delete cascade
        on update cascade,

    constraint fk_f_horario foreign key(id_horario)
		references horario(id_horario)
        on delete cascade
        on update cascade,
        
    constraint fk_f_peliculas foreign key(id_pelicula)
		references peliculas(id_pelicula)
        on delete cascade
        on update cascade
);

create table if not exists boletos(
    id_boletos int not null auto_increment,
    id_usuario int not null,
    id_asientos int not null,

    primary key(id_boletos),

    constraint fk_b_usuario foreign key(id_usuario)
		references usuario(id_usuario)
        on delete cascade
        on update cascade,

    constraint fk_b_asientos foreign key(id_asientos)
		references asientos(id_asientos)
        on delete cascade
        on update cascade
);