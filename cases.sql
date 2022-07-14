-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-07-14 11:17:08
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `chickenpt`
--

-- --------------------------------------------------------

--
-- 資料表結構 `cases`
--

CREATE TABLE `cases` (
  `id` varchar(30) NOT NULL,
  `content` varchar(30) NOT NULL,
  `price` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `boss` varchar(30) NOT NULL,
  `href` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `cases`
--

INSERT INTO `cases` (`id`, `content`, `price`, `place`, `boss`, `href`) VALUES
('BxV0bo672mjE', '徵求台灣藝術大學學士服(紫色)s/m', '單次$100', '在家兼職', '胡小姐', 'https://www.chickpt.com.tw/job'),
('BxV0boEeamjE', '8/6號下午1:30，幫忙公所點普渡祭品的香跟蠟燭', '單次$168', '南投縣南投市', '温小姐', 'https://www.chickpt.com.tw/job'),
('BZQ1oEbBA0qx', '帶動有氧運動', '單次$350', '台北市信義區', '徐先生', 'https://www.chickpt.com.tw/job'),
('DoVmk8ybB1XL', '#急7/15幫忙把家具搬樓下', '單次$800', '新北市新莊區', '王小姐', 'https://www.chickpt.com.tw/job'),
('dqQ0MRJ8ymoJ', '壁面水泥粉光', '單次$2000', '台中市龍井區', '胡小姐', 'https://www.chickpt.com.tw/job'),
('dqQ0MRJBomoJ', '餐飲業LOGO設計', '單次$3000', '在家兼職', '陳小姐', 'https://www.chickpt.com.tw/job'),
('G7e5Z32En0qX', '7/17神明安座需屬虎', '單次$800', '桃園市龜山區', '黃小姐', 'https://www.chickpt.com.tw/job'),
('jJo59VDeX0zw', '找線上英文老師', '單次$250', '在家兼職', '陳小姐', 'https://www.chickpt.com.tw/job'),
('K3N0Oojo20rb', '商品圖片設計（美編）', '單次$1200', '在家兼職', '陳先生', 'https://www.chickpt.com.tw/job'),
('k6z0r6A6V0pW', '逢甲商圈傳單發放', '單次$600', '台中市西屯區', '陳先生', 'https://www.chickpt.com.tw/job'),
('PQx5y9RLd5W2', '幫找台北房子（請看內文在找）', '單次$1500', '台北市信義區', '梁先生', 'https://www.chickpt.com.tw/job'),
('QJlmX7Znz0XZ', '暑期心理學閱讀眼動實驗', '單次$250', '台北市大安區', '吳小姐', 'https://www.chickpt.com.tw/job'),
('Qjnmz9abz0p9', '美甲彩繪', '單次$1200', '台南市永康區', '謝小姐', 'https://www.chickpt.com.tw/job'),
('qr3mAqAepm7P', '7/15打掃人員', '單次$1020', '新竹市東區', '謝先生', 'https://www.chickpt.com.tw/job'),
('VK8m2Dvxj5wo', '成功大學找人測血壓', '單次$100', '台南市東區', '張先生', 'https://www.chickpt.com.tw/job'),
('XqY08N3zo1n8', '8/5號，普渡貨品搬運，將貨品搬到指定的位置', '單次$504', '南投縣南投市', '温小姐', 'https://www.chickpt.com.tw/job'),
('xzlmpBErO59a', '7/16、17信義區場地整理打掃', '單次$700', '台北市信義區', '蘇先生', 'https://www.chickpt.com.tw/job'),
('Yn71VPeGO0j2', '教我考取重機駕照', '單次$1000', '宜蘭縣五結鄉', '張先生', 'https://www.chickpt.com.tw/job'),
('Yn71VPlPO0j2', '市場調查（流行事物）', '單次$30', '在家兼職', '陳先生', 'https://www.chickpt.com.tw/job'),
('YqRmJL4A25Zd', '中文系自傳檢查修正', '單次$300', '在家兼職', '陳小姐', 'https://www.chickpt.com.tw/job'),
('zrn0gaEAw1gE', '幫忙帶狗去打疫苗', '單次$300', '新北市板橋區', '游小姐', 'https://www.chickpt.com.tw/job');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `cases`
--
ALTER TABLE `cases`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
