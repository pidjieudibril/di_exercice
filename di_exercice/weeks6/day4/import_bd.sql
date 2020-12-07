drop table if exists personne;
create table personne(id_personne serial primary key, first_name varchar(30) not null,last_name varchar(30) not null);
drop table if exists café;
create table café(id_café serial primary key, name varchar(30) not null,lacolisation varchar(20) not null)

insert into personne(first_name,last_name) value ("pidjjieu","dibril2"),("tarmo","minour"),("steve","hermane"),("tonton","djkf")
insert into café(name,lacolisation) value ("le_gou","rue 10 doul"),("fourchette","tamtam")