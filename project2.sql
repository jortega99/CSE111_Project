--insert into CPU
--values (name, price, manufacturer, corecount, coreclock, boostclock)
insert into CPU
values ('Intel Core i5-4460 3.2 GHz Quad-Core Processor', 214.95, 'Intel', 4, '3.2 GHz', '3.4 GHz')

--insert into CASE
--values (name, price, manufacturer, formfactor)
insert into Tower
values ('NZXT H510i ATX Mid Tower Case', 99.99, 'NZXT', 'ATX Mid Tower')

--insert into GPU
--values (name, price, manufacturer, chipset, memory, boostclock, coreclock)
insert into GPU
values ('EVGA GeForce GTX 1060 3GB 3 GB SC GAMING Video Card', 259.99, 'EVGA', 'GeForce GTX 1060', '6 GB', '1830 MHz', '1530 MHz')

--insert into MB
--values (name, price, manufacturer, socket)
insert into MotherBoard
values ('Gigabyte GA-Z97X-Gaming 3 ATX LGA1150 Motherboard', 119.99, 'Gigabyte', 'LGA1150', 'ATX')

--insert into PSU
--values (name, price, manufacturer, formfactor, wattage, efficiency, modularity)
insert into PSU
values ('Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply', 119.99, 'Corsair', 'ATX', '750 W', '80+ Gold', 'Full')

--insert into RAM
--values (name, price, manufacturer, speed, modules)
insert into RAM
values ('Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory', 69.99, 'Crucial', 'Speed: 1600', '2 x 4GB')

--insert into Storage
--values (name, price, manufacturer, capacity, type, cache)
insert into Storage
values ('Kingston HyperX Fury 120 GB 2.5" Solid State Drive', 79.99, 'Kingston', '120 GB', 'SSD')

--insert into User
--values (name, password)
insert into Users
values ('girizarrytorres', 'notmyactualpassword73')

--insert into Build (cpu, gpu, motherboard, ram, storage, psu, tower) --should auto insert user + code
insert into Build (b_user, b_code, b_cpu, b_gpu, b_motherboard, b_ram, b_storage, b_psu, b_tower)
values ('girizarrytorres',
        'L7ZX72L6',
        'Intel Core i5-4460 3.2 GHz Quad-Core Processor',
        'EVGA GeForce GTX 1060 3GB 3 GB SC GAMING Video Card',
        'Gigabyte GA-Z97X-Gaming 3 ATX LGA1150 Motherboard',
        'Crucial Ballistix Sport 8 GB (2 x 4 GB) DDR3-1600 CL9 Memory',
        'Kingston HyperX Fury 120 GB 2.5" Solid State Drive',
        'Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply',
        'NZXT H510i ATX Mid Tower Case');

--updating build to simulate what website would do
update Build
set b_user = 'girizarrytorres', b_code = 'L7ZX72L6'
where b_cpu = 'Intel Core i5-4460 3.2 GHz Quad-Core Processor'

--finding build price and updating build table
update Build
set b_price = (select sum(x.price) as total
from Build,
(
    select CPU_price as price
    from CPU
    where CPU_name = b_cpu
    union all
    select GPU_price
    from GPU
    where GPU_name = b_gpu
    union all
    select MB_price
    from MotherBoard
    where MB_name = b_motherboard
    union all
    select RAM_price
    from RAM
    where RAM_name = b_ram
    union all
    select Storage_price
    from Storage
    where Storage_name = b_storage
    union all
    select PSU_price
    from PSU
    where PSU_name = b_psu
    union all
    select Case_price
    from Tower
    where Case_name = b_tower
) x) 
where b_code = 'L7ZX72L6'

--update table
--set price = newprice
--where name = nameofitem
update PSU
set psu_price = 80.00
where psu_name = 'Corsair RM 750 W 80+ Gold Certified Fully Modular ATX Power Supply'

--update Users
--set password = newpassword
--where name = this.user
update Users
set u_password = 'myactualpword37'
where u_name = 'girizarrytorres'

--delete from Build
--where name = this.user and code = code
delete from Build
where b_user = 'girizarrytorres' and b_code = 'L7ZX72L6'

--delete from Users
--where name = this.user
delete from Users
where u_name = 'girizarrytorres'

UPDATE Build
set b_cpu = 'AMD Ryzen 5 3600 3.6 GHz 6-Core Processor', 199, 'AMD',6,'3.6 GHz', '4.2 GHz'
WHERE b_code = 'L7ZX72L6'

DROP TABLE user