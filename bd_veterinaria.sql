-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-05-2025 a las 06:55:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_veterinaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consultas`
--

CREATE TABLE `consultas` (
  `ID` int(11) NOT NULL,
  `Fecha` date NOT NULL,
  `Hora` time NOT NULL,
  `Tipo` varchar(20) NOT NULL,
  `MascotaId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `consultas`
--

INSERT INTO `consultas` (`ID`, `Fecha`, `Hora`, `Tipo`, `MascotaId`) VALUES
(2, '2024-01-25', '11:00:00', 'Consulta General', 1114),
(12, '2025-05-28', '04:00:00', 'Estilista', 1117),
(22, '2025-05-30', '03:00:00', 'Estilista', 1117),
(23, '2025-06-28', '01:00:00', 'Revición general', 1117),
(24, '2025-06-26', '01:00:00', 'Estilista', 1119),
(25, '2025-05-28', '03:00:00', 'Vacunación', 1114),
(26, '2025-06-06', '05:00:00', 'Revición general', 1123),
(28, '2025-05-28', '10:00:00', 'Revición general', 1126),
(29, '2025-06-08', '12:00:00', 'Vacunación', 1127);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascota`
--

CREATE TABLE `mascota` (
  `ID` int(11) NOT NULL,
  `Nombre` varchar(20) NOT NULL,
  `Dueño` varchar(20) NOT NULL,
  `Tipo` varchar(20) NOT NULL,
  `Raza` varchar(20) NOT NULL,
  `Edad` int(11) NOT NULL,
  `FechaRegistro` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mascota`
--

INSERT INTO `mascota` (`ID`, `Nombre`, `Dueño`, `Tipo`, `Raza`, `Edad`, `FechaRegistro`) VALUES
(1111, 'Luna', 'Carlos Gómez', 'Perro', 'Labrador', 0, '2024-01-15'),
(1112, 'Milo', 'Ana Ruiz', 'Gato', 'Siames', 0, '2024-02-10'),
(1113, 'Kiwi', 'Lucía Torres', 'Ave', 'Perico', 0, '2024-03-05'),
(1114, 'Rocky', 'Pedro Salinas', 'Perro', 'Pitbull', 0, '2024-01-20'),
(1115, 'Puka', 'Maria Tovar', 'Perro', 'Chihuhua', 1, '2025-05-18'),
(1116, 'Shiber', 'Maricarmen Lara', 'Perro', 'Mestizo', 11, '2025-05-20'),
(1117, 'Jin', 'Fernanda Camacho', 'Perro', 'Husky', 5, '2025-05-20'),
(1118, 'Zeus', 'Monica Hernandez', 'Perro', 'Husky', 2, '2025-05-21'),
(1119, 'kevin', 'Lupe Esparza', 'Ave', 'Cotorro', 1, '2025-05-21'),
(1120, 'Dora', 'Monica Hernandez', 'Perro', 'Mestizo', 4, '2025-05-21'),
(1121, 'mige', 'Monica Hernandez', 'Ave', 'perico', 4, '2025-05-21'),
(1122, 'Nita', 'Oscar Hernandez', 'Perro', 'Mestizo', 2, '2025-05-21'),
(1123, 'Juanis', 'Fernanda Camacho', 'Ave', 'Cotorro', 1, '2025-05-21'),
(1124, 'patricio', 'Carmen Salinas', 'Ave', 'Pato', 3, '2025-05-21'),
(1125, 'jumpyo', 'Rodolfo Lara', 'Perro', 'Pastor Aleman', 1, '2025-05-21'),
(1126, 'Firulais', 'Gabo ', 'Perro', 'Pastor Aleman ', 2, '2025-05-21'),
(1127, 'moli', 'Cecilia Lopez', 'Gato', 'Mestizo', 3, '2025-05-21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `veterinario`
--

CREATE TABLE `veterinario` (
  `Nombre` varchar(20) NOT NULL,
  `contraseña` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `veterinario`
--

INSERT INTO `veterinario` (`Nombre`, `contraseña`) VALUES
('lupeKill', '123');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `consultas`
--
ALTER TABLE `consultas`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `mascota`
--
ALTER TABLE `mascota`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `consultas`
--
ALTER TABLE `consultas`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `mascota`
--
ALTER TABLE `mascota`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1128;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
