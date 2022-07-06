-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 06-Jul-2022 às 20:42
-- Versão do servidor: 5.7.17
-- PHP Version: 7.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banco-empresa`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionarios`
--

CREATE TABLE `funcionarios` (
  `func_id` int(11) NOT NULL,
  `func_nome` varchar(200) NOT NULL,
  `func_sobrenome` varchar(100) NOT NULL,
  `func_rg` varchar(20) NOT NULL,
  `func_cpf` varchar(20) NOT NULL,
  `func_resid_rua` varchar(200) NOT NULL,
  `func_resid_n` int(5) NOT NULL,
  `func_email` varchar(200) NOT NULL,
  `func_telefone` varchar(20) NOT NULL,
  `func_salario` int(10) NOT NULL,
  `func_cargo` varchar(100) NOT NULL,
  `func_data_contrato` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `funcionarios`
--

INSERT INTO `funcionarios` (`func_id`, `func_nome`, `func_sobrenome`, `func_rg`, `func_cpf`, `func_resid_rua`, `func_resid_n`, `func_email`, `func_telefone`, `func_salario`, `func_cargo`, `func_data_contrato`) VALUES
(15, 'Yan Pablo', 'Rodrigues', '67590854', '21724468907', 'Francisca Rodrigues Becegato', 80, 'yan.pablo205@gmail.com', '18981541343', 15000, 'Desenvolvimento', '2001-07-22'),
(16, 'Anthony Sander ', 'Rodrigues', '14573906', '21723467785', 'Teofilo Nascimento', 576, 'anthony.sander204@gmail.com', '18997298584', 5000, 'Caminhoneiro', '2022-07-01'),
(17, 'Juliana Barbosa', 'Silva', '5672345', '35477890312', 'Almarir Souza Castelo', 34, 'jubarbosa.silva09@gmail.com', '18994567893', 2000, 'Serviços Gerais', '2022-07-01'),
(18, 'Giovanna Almeida', 'Medeiros', '2123468', '34588962890', 'Chico Budan Lourenzo', 112, 'almeida.giovanna1@gmail.com', '17995347780', 1500, 'Administração', '2022-07-01'),
(19, 'Jefferson Bonfim', 'Silverado', '5647889', '21143277894', 'Av. Manoel Goulart', 505, 'jefferson.silverado@gmail.com', '11996231156', 1570, 'Caminhoneiro', '2022-07-01'),
(23, 'Matheus Bara', 'Prado', '4578901', '45890137790', 'Coronel Lourenzo Marque', 890, 'matheus.prd77@hotmail.com', '1299655342', 3000, 'Auxiliar de Produção', '2022-07-05'),
(24, 'Maria Heloisa', 'Dourad Lima', '7812340', '78913995563', 'Luciano Hang Setinela', 4378, 'mariaheloisalima1@outlook.com', '17992045579', 4570, 'Desenvolvimento', '2022-07-05'),
(25, 'Phelips Brondilam ', 'Hasaki', '7482082', '14462874779', 'Better Loney Filter', 11, 'ppphelips.hasakiqq@hotmail.com', '22994526671', 3500, 'Financeiro', '2022-07-05'),
(26, 'Laura Monaco', 'Silveira', '3454245', '82099032134', 'Tierry Junior', 1388, 'laura.monacol615@gmail.com', '13997254377', 7000, 'Administração', '2022-07-05'),
(27, 'Sthefani Lima', 'Nakada', '3431154', '91073543568', 'José Diamond Portinari', 440, 'sthe.paninakada@outlook.com', '18992451168', 5000, 'Administração', '2022-07-05'),
(28, 'Cristiano de Souza', 'Gomes', '3243442', '84762699840', 'Av. Barone Marcondes', 12, 'cristiano.gomes22@hotmail.com', '23991023799', 2500, 'Caminhoneiro', '2022-07-05'),
(29, 'Tiffany Noronha', 'Nakada', '3456678', '32493289472', 'Major Centinela Phelps', 211, 'tiffany.nakada1@outlook.com', '23991203677', 9000, 'Desenvolvimento', '2022-07-05'),
(30, 'Giulia Souza', 'Bonfim', '7347892', '11234453598', 'Lourenzo Maquilone', 2, 'gi.bomfinsouz@gmail.com', '23997182362', 2000, 'Serviços Gerais', '2022-07-05'),
(31, 'Vinicius Marques', 'Mendonça', '2314323', '24577221439', 'Monte Carlo Viidal', 93, 'vini.ciusmend@hotmail.com', '21997615119', 3000, 'Caminhoneiro', '2022-07-05'),
(32, 'Derek Gabriel', 'David', '2123555', '63547719801', 'Av. Diretor Sergio Prado', 2122, 'derekered.gabriel@gmail.com', '21997554231', 2000, 'Auxiliar de Produção', '2022-07-05'),
(33, 'Monique Harishama', 'Nakada', '2135532', '19854883290', 'Coronel Marcondes', 933, 'harishama.monique2@gmail.com', '18996598872', 4000, 'Desenvolvimento', '2022-07-05');

-- --------------------------------------------------------

--
-- Estrutura da tabela `login`
--

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL,
  `log_nome` varchar(200) NOT NULL,
  `log_email` varchar(150) NOT NULL,
  `log_usuario` varchar(100) NOT NULL,
  `log_senha` varchar(100) NOT NULL,
  `log_data_criacao` date NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `login`
--

INSERT INTO `login` (`log_id`, `log_nome`, `log_email`, `log_usuario`, `log_senha`, `log_data_criacao`) VALUES
(1, 'Yan Pablo Rodrigues', 'yan.pablo205@gmail.com', 'admin', 'yan123', '2022-07-06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `funcionarios`
--
ALTER TABLE `funcionarios`
  ADD PRIMARY KEY (`func_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`log_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `funcionarios`
--
ALTER TABLE `funcionarios`
  MODIFY `func_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `log_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
