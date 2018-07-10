-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Июл 10 2018 г., 18:38
-- Версия сервера: 10.1.33-MariaDB
-- Версия PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `schedule`
--
CREATE DATABASE IF NOT EXISTS `schedule` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `schedule`;

DELIMITER $$
--
-- Процедуры
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_group_id` (IN `_group` VARCHAR(128) CHARSET utf8)  NO SQL
select g.id
from groups as g
where g.name = _group$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `get_week_schedule` (IN `_group` VARCHAR(128) CHARSET utf8, IN `_week` INT)  NO SQL
select d.day, d.name, s.time, s.type, s.name, s.teacher, s.classroom
from weeks as w
inner join groups as g
on g.name = _group
inner join days as d
on w.id_day = d.id
inner join subject as s
on s.id = d.id_subject
where w.week = _week$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `set_day` (IN `_day` INT, IN `_id_subject` INT, IN `_name` VARCHAR(45) CHARSET utf8)  NO SQL
BEGIN
	INSERT INTO days (day, id_subject, name) VALUES(_day, _id_subject, _name);
    SELECT last_insert_id();
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `set_group` (IN `_name` VARCHAR(128) CHARSET utf8)  NO SQL
begin
    insert into groups (name) VALUES(_name);
    SELECT last_insert_id();
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `set_subject` (IN `_name` VARCHAR(45) CHARSET utf8, IN `_type` VARCHAR(45) CHARSET utf8, IN `_teacher` VARCHAR(45) CHARSET utf8, IN `_classroom` VARCHAR(45) CHARSET utf8, IN `_time` VARCHAR(45) CHARSET utf8)  NO SQL
begin
    insert into subject (name, type, teacher, classroom, time)
    VALUES(_name, _type, _teacher, _classroom, _time);
    SELECT last_insert_id();
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `set_week` (IN `_week` INT, IN `_id_group` INT, IN `_id_day` INT)  NO SQL
insert into weeks (week, id_group, id_day) values(_week, _id_group, _id_day)$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `days`
--

CREATE TABLE `days` (
  `id` int(11) NOT NULL,
  `id_subject` int(11) NOT NULL,
  `day` int(11) NOT NULL,
  `name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `name` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `subject`
--

CREATE TABLE `subject` (
  `id` int(11) NOT NULL,
  `time` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `teacher` varchar(45) DEFAULT NULL,
  `classroom` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `weeks`
--

CREATE TABLE `weeks` (
  `id` int(11) NOT NULL,
  `week` int(11) NOT NULL,
  `id_group` int(11) NOT NULL,
  `id_day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `days`
--
ALTER TABLE `days`
  ADD PRIMARY KEY (`id`,`id_subject`,`day`),
  ADD KEY `fk_day_subject1_idx` (`id_subject`);

--
-- Индексы таблицы `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`,`name`),
  ADD UNIQUE KEY `name_UNIQUE` (`name`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- Индексы таблицы `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `weeks`
--
ALTER TABLE `weeks`
  ADD PRIMARY KEY (`id`,`week`,`id_group`,`id_day`),
  ADD KEY `fk_week_groups1_idx` (`id_group`),
  ADD KEY `fk_week_id_group_idx` (`id_day`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `days`
--
ALTER TABLE `days`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `subject`
--
ALTER TABLE `subject`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `weeks`
--
ALTER TABLE `weeks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `days`
--
ALTER TABLE `days`
  ADD CONSTRAINT `fk_day_subject1` FOREIGN KEY (`id_subject`) REFERENCES `subject` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Ограничения внешнего ключа таблицы `weeks`
--
ALTER TABLE `weeks`
  ADD CONSTRAINT `fk_week_groups1` FOREIGN KEY (`id_group`) REFERENCES `groups` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_week_id_group` FOREIGN KEY (`id_day`) REFERENCES `days` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
