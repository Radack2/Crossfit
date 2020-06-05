create database if not exists crossfit_db;

use crossfit_db;


create table if not exists cliente (
	id_cliente int not null auto_increment,
    nombre varchar(50) not null,
    apellido_p varchar(50) not null,
    apellido_m varchar(50),
    edad int not null,
    telefono int,
    correo varchar(50),
    fecha_pago date not null,
    
    primary key (id_cliente)
) engine = InnoDB;

create table if not exists material (
	nombre varchar(70) not null,
    cantidad int not null,
    descripcion varchar(200),
    
    primary key(nombre)
)engine = InnoDB;

create table if not exists ejercicio (
	nombre varchar(30) not null,
    descripcion varchar(200) not null,
    
    primary key(nombre)
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
	id_wod int not null auto_increment,
    nombre_ejercicio varchar(30) not null,
    tiempo int not null,
    repeticiones int not null,
		
	primary key(id_wod),
    constraint fk_ejercicio_wod foreign key(nombre_ejercicio)
		references ejercicio(nombre)
        on delete cascade
        on update cascade
        
 ) engine = InnoDB;
 
 create table if not exists clase (
	hora_inicio datetime not null,
	hora_termina datetime not null,
    id_wod int not null,
    id_coach int not null,
    
    primary key(hora_inicio)
    
 ) engine = InnoDB;
 
 create table if not exists box (
	id_box int not null auto_increment,
    id_cliente int not null,
    clase time not null,
    material varchar(70) not null,
    coach int not null,
    
    primary key(id_box),
    
    constraint fk_cliente foreign key(id_cliente)
		references cliente(id_cliente)
        on delete cascade
        on update cascade,
        
	constraint fk_clase foreign key(clase)
		references clase(hora_inicio)
        on delete cascade
        on update cascade,
        
        
	constraint fk_material foreign key(material)
		references material(nombre)
        on delete cascade
        on update cascade,
        
    constraint fk_coach foreign key(coach)
		references coach(id_coach)
        on delete cascade
        on update cascade
	
    
)engine = InnoDB;
    
