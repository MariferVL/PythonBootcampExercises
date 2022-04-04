
-- CREATE DATABASE TLV_5_4;

-- Borrar y Crear basedatos
-- DROP SCHEMA IF EXISTS TLV_5_4;
-- CREATE SCHEMA IF NOT EXISTS TLV_5_4;

-- Borrar y Crear basedatos
USE TLV_5_4;
DROP TABLE cuentas;
CREATE TABLE cuentas (
    Cuenta VARCHAR(111) NOT NULL,
    Saldo int NOT NULL,
    PRIMARY KEY (Cuenta)
);
INSERT INTO cuentas
VALUES  ('A', 1000),
		('B', 1000),
		('C', 1000),
		('D', 1000);






-- Transferencias

-- 1) Transfiera 200 TLV Coins desde un usuario A un usuario B (se aplica rollback)
-- 2) Transfiera 150 TLV Coins desde un usuario B un usuario C (se aplica rollback)
-- 3) Transfiera 500 TLV Coins desde un usuario C un usuario D (se aplica commit)
-- 4) Transfiera 200 TLV Coins desde un usuario D un usuario A (se aplica commit)

-- Para todas las tranferencias:
-- verificar que la cuenta tenga saldo suficiente
-- verificar que la cuenta de destino exista
-- actualizar la cuenta de origen
-- actualizar la cuenta de destino
-- verificar que se haya actualizado la cuenta de origen
-- verificar que se haya modificado la cuenta de destino

SET autocommit = 0;

-- 1) Transferencia 200 Coins A a B
START TRANSACTION;
SET @transf = 200,
	@ori = 'A',
    @dst = 'B';
SET @flag = (SELECT Saldo from cuentas where Cuenta = @ori);
SET @exist_dst = IF(EXISTS(SELECT * from cuentas WHERE Cuenta=@dst), 1 , 0);
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo-@transf , Saldo) WHERE Cuenta = @ori;
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo+@transf , Saldo) WHERE Cuenta = @dst;
-- (SELECT * FROM cuentas WHERE Cuenta = @ori) union (SELECT * FROM cuentas WHERE Cuenta = @dst);
ROLLBACK;


-- 2) Transferencia 150 Coins B a C
START TRANSACTION;
SET @transf = 150,
	@ori = 'B',
    @dst = 'C';
SET @flag = (SELECT Saldo from cuentas where Cuenta = @ori);
SET @exist_dst = IF(EXISTS(SELECT * from cuentas WHERE Cuenta=@dst), 1 , 0);
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo-@transf , Saldo) WHERE Cuenta = @ori;
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo+@transf , Saldo) WHERE Cuenta = @dst;
-- (SELECT * FROM cuentas WHERE Cuenta = @ori) union (SELECT * FROM cuentas WHERE Cuenta = @dst);
ROLLBACK;



-- 3) Transferencia 500 Coins C a D
START TRANSACTION;
SET @transf = 500,
	@ori = 'C',
    @dst = 'D';
SET @flag = (SELECT Saldo from cuentas where Cuenta = @ori);
SET @exist_dst = IF(EXISTS(SELECT * from cuentas WHERE Cuenta=@dst), 1 , 0);
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo-@transf , Saldo) WHERE Cuenta = @ori;
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo+@transf , Saldo) WHERE Cuenta = @dst;
-- (SELECT * FROM cuentas WHERE Cuenta = @ori) union (SELECT * FROM cuentas WHERE Cuenta = @dst);
COMMIT;

-- 4) Transferencia 200 Coins D a A
START TRANSACTION;
SET @transf = 200,
	@ori = 'D',
    @dst = 'A';
SET @flag = (SELECT Saldo from cuentas where Cuenta = @ori);
SET @exist_dst = IF(EXISTS(SELECT * from cuentas WHERE Cuenta=@dst), 1 , 0);
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo-@transf , Saldo) WHERE Cuenta = @ori;
UPDATE cuentas SET Saldo = IF(@flag>@transf AND @exist_dst=1, Saldo+@transf , Saldo) WHERE Cuenta = @dst;
-- (SELECT * FROM cuentas WHERE Cuenta = @ori) union (SELECT * FROM cuentas WHERE Cuenta = @dst);
COMMIT;




SELECT * FROM cuentas;

