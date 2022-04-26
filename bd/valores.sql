use poupay;

create table valores (
	id int primary key auto_increment,
	tipo varchar(25),
	regiao varchar(15),
	valor decimal(17, 2),
	quantidade int,
    ano int,
	mes varchar(12)
);

select * from valores order by regiao;
truncate table valores;
