--what components would make the highest cost pc
--what components would make the lowest cost pc
--how many parts are made by each manufacturer
--which manyfacturers make the most parts for their respective categories



--insert into CPU
--values (name, price, manufacturer, corecount, coreclock, boostclock)
insert into CPU
values ('Intel Core i5-4460 3.2 GHz Quad-Core Processor', '214.95', 'Intel', 4, '3.2 GHz', '3.4 GHz')

--insert into CASE
--values (name, price, manufacturer, formfactor)
insert into Tower
values ('NZXT H510i ATX Mid Tower Case', 99.99, 'NZXT', 'ATX Mid Tower')

--insert into GPU ----would it be hard to swap boost/coreclock
--values (name, price, manufacturer, chipset, memory, boostclock, coreclock)
insert into GPU
values ('EVGA GeForce GTX 1060 3GB 3 GB SC GAMING Video Card', 259.99, 'EVGA', 'GeForce GTX 1060', '6 GB', '1830 MHz', '1530 MHz')

--insert into MB
--values (name, price, manufacturer, socket)
insert into MB
values ('Gigabyte GA-Z97X-Gaming 3 ATX LGA1150 Motherboard', 119.99, 'Gigabyte', 'LGA1150', 'ATX')

--insert into PSU
--values (name, price, manufacturer, formfactor, wattage, efficiency, modularity)
insert into PSU
values ('Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply', 119.99, 'Corsair', 'ATX', '750 W', '80+ Gold', 'Full')

--insert into RAM
--values (name, price, manufacturer, speed, modules)
insert into RAM
values ('Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory', 69.99, 'Crucial', 'Speed: 1600', '2 x 4GB')

--insert into Storage  ----should remove cache seems to be buggy maybe check type too
--values (name, price, manufacturer, capacity, type, cache)
insert into Storage
values ('Kingston HyperX Fury 120 GB 2.5" Solid State Drive', 79.99, 'Kingston', '120 GB', 'SSD', '500MB')

--insert into User
--values (name, password)
insert into Users
values ('girizarrytorres', 'notmyactualpassword73')

--insert into Build (cpu, gpu, motherboard, ram, storage, psu, tower) --should auto insert user + code
insert into Build (cpu, gpu, motherboard, ram, storage, psu, tower)
values ('Intel Core i5-4460 3.2 GHz Quad-Core Processor',
        'EVGA GeForce GTX 1060 3GB 3 GB SC GAMING Video Card',
        'Gigabyte GA-Z97X-Gaming 3 ATX LGA1150 Motherboard',
        'Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory',
        'Kingston HyperX Fury 120 GB 2.5" Solid State Drive',
        'Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply',
        'NZXT H510i ATX Mid Tower Case');

--updating build to simulate what website would do
update Build
set maker = 'girizarrytorres', code = 'L7ZX72L6'
where cpu = 'Intel Core i5-4460 3.2 GHz Quad-Core Processor'

--update table
--set price = newprice
--where name = nameofitem
update PSU
set price = 80.00
where name = 'Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply'

--update Users
--set password = newpassword
--where name = this.user
update Users
set password = 'myactualpword37'
where name = 'girizarrytorres'

--delete from Build
--where name = this.user and code = code
delete from Build
where name = 'girizarrytorres' and code = 'L7ZX72L6'

--delete from Users
--where name = this.user
delete from Users
where name = 'girizarrytorres'