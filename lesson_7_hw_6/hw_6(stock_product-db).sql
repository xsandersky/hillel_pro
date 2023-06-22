create table stock_table(
	id int not null,
	stock_name varchar(50) not null primary key
);

create table product_table(
	name_product varchar(80) not null,
	description varchar(250),
	name_of_stock varchar(50) references stock_table(stock_name)
);

insert into stock_table values(1, 'electronics');
insert into stock_table values(2, 'sport_inventary');
insert into stock_table values(3, 'clothes');

insert into product_table values('Phone', 'Waterproof, shockproof, 6" screen', 'electronics');
insert into product_table values('TV', 'Experience vibrant picture and Dolby Atmos sound for a smooth gaming experience', 'electronics');
insert into product_table values('Laptop', 'Powerful, bright, flawless', 'electronics');

insert into product_table values('bicyle', '2 wheels and frame', 'sport_inventary');
insert into product_table values('ball', 'leather, round, for professionals', 'sport_inventary');
insert into product_table values('gloves', 'for boxing, leather', 'sport_inventary');

insert into product_table values('sneakers', 'leather, bright', 'clothes');
insert into product_table values('jeans', 'blue/black, different sizes', 'clothes');
insert into product_table values('pants', 'different sizes, different maerials', 'clothes');
insert into product_table values('cap', 'for men', 'clothes');

select * from product_table where name_of_stock = 'electronics';

select * from  product_table;

update product_table set description = 'use' where name_of_stock = 'electronics';

select * from  product_table;

delete from product_table where name_of_stock = 'clothes';

create index product_name_idx on product_table(name_product);