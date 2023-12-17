USE netflix;

DELIMITER //
CREATE TRIGGER prevent_insert_additional
BEFORE INSERT ON additional_table
FOR EACH ROW
BEGIN
    DECLARE actor_count INT;

    SELECT COUNT(*) INTO actor_count FROM actor WHERE id = NEW.actor_id;

    IF actor_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert additional data without a valid actor';
    END IF;
END;
//
DELIMITER ;
DROP PROCEDURE IF EXISTS insert_actor;
DELIMITER //
CREATE PROCEDURE insert_actor(
    IN p_name VARCHAR(45),
    IN p_surname VARCHAR(45),
    IN p_age INT,
    IN p_film_id INT
)
BEGIN
    DECLARE last_actor_id INT;

    IF NOT (p_name IS NULL OR p_surname IS NULL OR p_age IS NULL OR p_film_id IS NULL) THEN
        INSERT INTO actor (name, surname, age, film_id) VALUES (p_name, p_surname, p_age, p_film_id);
        SET last_actor_id = LAST_INSERT_ID();
        SELECT * FROM actor WHERE id = last_actor_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'All parameters must be provided';
    END IF;
END;//
DELIMITER ;
DROP PROCEDURE IF EXISTS insert_data_procedure;
DELIMITER //

CREATE PROCEDURE insert_data_procedure(
    IN p_name VARCHAR(255),
    IN mark INT,
    IN p_person_id INT
)
BEGIN
    INSERT INTO film (name) VALUES (p_name);
    SET @table1_id = LAST_INSERT_ID();

    INSERT INTO rating (mark, person_id) VALUES (mark, p_person_id);
    SET @table2_id = LAST_INSERT_ID();

    INSERT INTO film_has_rating (film_id, rating_id) VALUES (@table1_id, @table2_id);
END //

DELIMITER ;
DROP PROCEDURE IF EXISTS insert_noname_actors;
DELIMITER //
CREATE PROCEDURE insert_noname_actors()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        INSERT INTO actor (name, surname, age, film_id)
        VALUES (CONCAT('Noname', counter), 'NonameSurname', 25, 1);

        SET counter = counter + 1;
    END WHILE;
	SELECT * FROM actor WHERE name LIKE 'Noname%';
END //
DELIMITER ;
DROP PROCEDURE IF EXISTS get_actor_statistics;
DELIMITER //

CREATE PROCEDURE get_actor_statistics()
BEGIN
    DECLARE max_age DECIMAL(18,2);
    DECLARE min_age DECIMAL(18,2);
    DECLARE sum_age DECIMAL(18,2);
    DECLARE avg_age DECIMAL(18,2);

    SELECT MAX(age) INTO max_age FROM actor;
    SELECT MIN(age) INTO min_age FROM actor;
    SELECT SUM(age) INTO sum_age FROM actor;
    SELECT AVG(age) INTO avg_age FROM actor;

    SELECT 'Max Age:', max_age;
    SELECT 'Min Age:', min_age;
    SELECT 'Sum Age:', sum_age;
    SELECT 'Avg Age:', avg_age;
END //

DELIMITER ;
DROP PROCEDURE IF EXISTS create_dynamic_tables;
DELIMITER //

CREATE PROCEDURE create_dynamic_tables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE table_name_cursor VARCHAR(255);
    DECLARE column_count INT;
    DECLARE column_name VARCHAR(255);

    DECLARE cur_tables CURSOR FOR
        SELECT name, created_at
        FROM table_with_timestamp;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur_tables;

    read_tables: LOOP
        FETCH cur_tables INTO table_name_cursor, column_name;
        IF done THEN
            LEAVE read_tables;
        END IF;

        SET column_count = FLOOR(1 + RAND() * 9);

        SET @sql = CONCAT('CREATE TABLE `', REPLACE(table_name_cursor, ' ', '_'), '_', UNIX_TIMESTAMP(NOW()), '` (');

        SET @column_definitions = '';
        SET @i = 0;

        WHILE @i < column_count DO
            SET @column_name = CONCAT('column', @i);
            SET @column_type = CASE FLOOR(1 + RAND() * 3)
                WHEN 1 THEN 'INT'
                WHEN 2 THEN 'VARCHAR(255)'
                WHEN 3 THEN 'DOUBLE'
            END;

            SET @column_definitions = CONCAT(@column_definitions, @column_name, ' ', @column_type);

            SET @i = @i + 1;
            IF @i < column_count THEN
                SET @column_definitions = CONCAT(@column_definitions, ', ');
            END IF;
        END WHILE;

        SET @sql = CONCAT(@sql, @column_definitions, ');');

        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur_tables;
END //

DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_double_zeros_description
BEFORE INSERT ON description
FOR EACH ROW
BEGIN
    IF NEW.description LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Value cannot end with double zeros';
    END IF;
END;
//
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_modification_update_description
BEFORE UPDATE ON description
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Modification of data is not allowed';
END;
//
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_deletion_description
BEFORE DELETE ON description
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Deletion of records is not allowed';
END;
//
DELIMITER ;



