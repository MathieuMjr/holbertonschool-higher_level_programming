-- script that create a table with id field unique and 1 by default
CREATE TABLE IF NOT EXISTS `unique_id`(
    `id` INT UNIQUE DEFAULT 1,
    `name` VARCHAR(256)
).