create database if not exists crossfit_db;

use crossfit_db;


create table if not exists material (
	nombre varchar(70) not null,
    cantidad int not null,
    descripcion varchar(200),
    
    primary key(nombre)
)engine = InnoDB;

create table if not exists ejercicio (
	nombre varchar(70) not null,
    descripcion varchar(200) not null,
    material varchar(70) not null,
    
    primary key(nombre),
    
    constraint fk_material foreign key(material)
		references material(nombre)
        on delete cascade
        on update cascade
)
 engine = InnoDB;
 
 create table if not exists coach (
	id_coach int not null auto_increment,
    hora_inicio datetime not null,
	hora_termina datetime not null,
    nombre varchar(50) not null,
    apellido_p varchar(50) not null,
    apellido_m varchar(50),
    telefono int,
    correo varchar(50),
    
    primary key(id_coach)
 )engine =  InnoDB;
 
 create table if not exists wod (
    fecha date not null,
    tiempo int not null,
    tipo varchar(30) not null,
		
	primary key(fecha)
        
 ) engine = InnoDB;
 
 create table if not exists clase (
	hora_inicio time not null,
	hora_termina time not null,
    fecha_wod date not null,
    id_coach int not null,
    
    primary key(hora_inicio),
    
    constraint fk_wod foreign key(fecha_wod)
		references wod(fecha)
        on delete cascade
        on update cascade,
        
	constraint fk_coach foreign key(id_coach)
		references coach(id_coach)
        on delete cascade
        on update cascade
    
 ) engine = InnoDB;
 
create table if not exists cliente (
	id_cliente int not null auto_increment,
    nombre varchar(50) not null,
    apellido_p varchar(50) not null,
    apellido_m varchar(50),
    edad int not null,
    telefono int,
    correo varchar(50),
    fecha_pago date not null,
    hora_clase time not null,
    
    primary key (id_cliente),
    
    constraint fk_clase foreign key(hora_clase)
		references clase(hora_inicio)
        on delete cascade
        on update cascade
    
) engine = InnoDB;

 
 create table if not exists ejercicios_wod (
	nombre_ejercicio varchar(70) not null,
    fecha_wod date not null,
    repeticiones int not null,
    
    primary key (nombre_ejercicio,fecha_wod),
    
    constraint fk_ejercicio foreign key(nombre_ejercicio)
		references ejercicio(nombre)
        on delete cascade
        on update cascade,
        
	constraint fk_ejercicio_wod foreign key(fecha_wod)
		references wod(fecha)
        on delete cascade
        on update cascade
 )engine = InnoDB;