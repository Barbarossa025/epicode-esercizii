DROP PROCEDURE IF EXISTS inserter_immagine;
DELIMITER //
CREATE PROCEDURE inserter_immagine()
BEGIN
	DECLARE app_img INT;
	DECLARE param_img INT;
	SET app_img = 0;
	SET param_img = 472;
	WHILE app_img < param_img DO
		SET app_img = app_img + 1;
		INSERT INTO `immagine`(`titolo`, `indirizzo`)
		VALUES (CONCAT("titolo_immagine_", app_img), CONCAT("home/DB_ecommerce/img_", app_img));
	END WHILE;
END; //
DELIMITER ;
