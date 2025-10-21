-- script that list all cities with states name
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
INNER JOIN `states`
    ON `states`.`id` =  `cities`.`state_id`
ORDER BY `cities`.`id` ASC;