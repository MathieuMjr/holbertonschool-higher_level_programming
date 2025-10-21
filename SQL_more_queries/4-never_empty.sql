-- scrit that create a data base with not null field id and default value is 1
CREATE TABLE IF NOT EXISTS `id_not_null`(
    `id` INT NOT NULL DEFAULT 1,
    `name` VARCHAR(256)
);