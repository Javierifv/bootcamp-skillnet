
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `x`
--
CREATE DATABASE IF NOT EXISTS `x` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `x`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `tweet_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `favoritos`
--

INSERT INTO `favoritos` (`id`, `usuario_id`, `tweet_id`, `created_at`, `updated_at`) VALUES
(1, 2, 1, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(2, 2, 2, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(3, 3, 4, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(4, 4, 3, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(5, 1, 9, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(6, 1, 10, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(7, 1, 11, '2010-02-01 00:00:01', '2010-02-01 00:00:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `seguidores`
--

CREATE TABLE `seguidores` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `seguidor_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `seguidores`
--

INSERT INTO `seguidores` (`id`, `usuario_id`, `seguidor_id`, `created_at`, `updated_at`) VALUES
(1, 1, 2, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(2, 1, 3, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(3, 1, 4, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(4, 1, 5, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(5, 3, 4, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(6, 3, 5, '2010-02-01 00:00:01', '2010-02-01 00:00:01'),
(7, 2, 4, '2010-02-01 00:00:01', '2010-02-01 00:00:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tweets`
--

CREATE TABLE `tweets` (
  `id` int(11) NOT NULL,
  `tweet` varchar(140) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tweets`
--

INSERT INTO `tweets` (`id`, `tweet`, `usuario_id`, `created_at`, `updated_at`) VALUES
(1, 'Hay poder en comprender el viaje de los demás para ayudar a crear el propio.', 1, '2002-02-01 00:00:01', '2002-02-01 00:00:01'),
(2, '¡Felicidades, Coach K! Logro increíble #1KparaCoachK #Duke', 1, '2005-02-01 00:00:01', '2005-02-01 00:00:01'),
(3, 'Esto es lo que sucede cuando paso demasiado. #HombroEnShock Gracias a todos por sus oraciones. #equipo @DrinkBODYARMOR @Lakers #oneluv', 1, '2004-02-01 00:00:01', '2004-02-01 00:00:01'),
(4, 'Siento una mezcla de emociones que no he sentido en 18 años como profesional. #viaje #19a', 1, '2012-02-01 00:00:01', '2012-02-01 00:00:01'),
(5, 'Gracias a todos por los buenos deseos de cumpleaños. Los aprecio mucho.', 2, '2011-02-01 00:00:01', '2011-02-01 00:00:01'),
(6, 'Me gustaría desear a todos una muy Feliz Navidad. Mucho amor para todos. Cuídense.', 2, '2009-02-01 00:00:01', '2009-02-01 00:00:01'),
(7, 'Gracias a todos los que ayudaron con las canastas de comida de Navidad hoy. Su tiempo es muy apreciado. ¡Amor y respeto!', 2, '2008-02-01 00:00:01', '2008-02-01 00:00:01'),
(8, 'Acepté el desafío ALS de Monta Ellis. Desafío a @coolkesh42 Jameer Nelson, Dionne Calhoun ...', 2, '2003-02-01 00:00:01', '2003-02-01 00:00:01'),
(9, '¡Bien hecho, hermanito, te lo mereces! @KingJames', 3, '2006-02-01 00:00:01', '2006-02-01 00:00:01'),
(10, 'Para la clínica de baloncesto con @manilacone el 4/11/14, aún hay algunos lugares para el juego. Nos vemos el 5/11/14 en Filipinas.', 3, '2001-02-01 00:00:01', '2001-02-01 00:00:01'),
(11, 'Siempre la paso genial con mi hermanito mayor.', 4, '2011-02-01 00:00:01', '2011-02-01 00:00:01'),
(12, '¡Feliz Día del Trabajo!', 4, '2014-02-01 00:00:01', '2014-02-01 00:00:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `nombre_usuario` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `nombre_usuario`, `fecha_nacimiento`, `created_at`, `updated_at`) VALUES
(1, 'Kobe', 'Bryant', 'kobebryant', '1978-08-23', '2010-02-01 00:00:01', '2011-07-01 00:00:01'),
(2, 'Vince', 'Carter', 'mrvincecarter15', '1977-01-26', '2007-08-11 00:00:01', '2010-01-01 00:00:01'),
(3, 'Allen', 'Iverson', 'alleniverson', '1975-06-07', '2005-09-01 00:00:01', '2011-04-21 00:00:01'),
(4, 'Tracy', 'McGrady', 'Real_T_Mac', '1979-05-24', '2002-12-01 00:00:01', '2005-11-21 00:00:01'),
(5, 'Rajon', 'Rondo', 'RajonRondo', '1986-02-22', '2001-02-01 00:00:01', '2002-01-01 00:00:01');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_faves_users1_idx` (`usuario_id`),
  ADD KEY `fk_faves_tweets1_idx` (`tweet_id`);

--
-- Indices de la tabla `seguidores`
--
ALTER TABLE `seguidores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_follows_users_idx` (`usuario_id`);

--
-- Indices de la tabla `tweets`
--
ALTER TABLE `tweets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tweets_users1_idx` (`usuario_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `seguidores`
--
ALTER TABLE `seguidores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tweets`
--
ALTER TABLE `tweets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD CONSTRAINT `fk_faves_tweets1` FOREIGN KEY (`tweet_id`) REFERENCES `tweets` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_faves_users1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `seguidores`
--
ALTER TABLE `seguidores`
  ADD CONSTRAINT `fk_follows_users` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `tweets`
--
ALTER TABLE `tweets`
  ADD CONSTRAINT `fk_tweets_users1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
