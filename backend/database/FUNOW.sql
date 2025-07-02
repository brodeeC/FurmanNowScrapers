PRAGMA foreign_keys = ON;
-- phpMyAdmin SQL Dump
-- version 4.4.15.10
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 16, 2025 at 02:19 PM
-- Server version: 5.5.68-MariaDB
-- PHP Version: 5.4.16

--
-- Database: FUNOW
--

-- --------------------------------------------------------

--
-- Table structure for table athletics
--

CREATE TABLE IF NOT EXISTS athletics (
  eventdate TEXT NOT NULL,
  time TEXT NOT NULL,
  conference INTEGER NOT NULL,
  location_indicator TEXT NOT NULL,
  location TEXT NOT NULL,
  sportTitle TEXT NOT NULL,
  sportShort TEXT NOT NULL,
  opponent TEXT NOT NULL,
  noplayText TEXT NOT NULL,
  resultStatus TEXT NOT NULL,
  resultUs TEXT NOT NULL,
  resultThem TEXT NOT NULL,
  prescore_info TEXT NOT NULL,
  postscore_info TEXT NOT NULL,
  url TEXT NOT NULL,
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--
-- Dumping data for table athletics
--

-- INSERT INTO athletics (eventdate, time, conference, location_indicator, location, sportTitle, sportShort, opponent, noplayText, resultStatus, resultUs, resultThem, prescore_info, postscore_info, url, id, lastUpdated) VALUES
-- ('2025-06-13 00:00:00', 'ALL DAY', 0, 'A', 'Eugene, Ore.', 'Cross Country / Track & Field', 'TRACK', 'NCAA Championship', '', '', '', '', '', '', '/news/2025/6/13/cross-country-track-field-furmans-williams-places-third-in-steeplechase-at-ncaa-championship.aspx', 141412, '2025-06-16 14:00:02'),
-- ('2025-06-19 00:00:00', 'ALL DAY', 0, 'A', 'Eugene, Ore.', 'Cross Country / Track & Field', 'TRACK', 'USATF U20 Championship', '', '', '', '', '', '', 'null', 141413, '2025-06-16 14:00:02'),
-- ('2025-06-19 00:00:00', 'ALL DAY', 0, 'A', 'Eugene, Ore.', 'Cross Country / Track & Field', 'TRACK', 'USATF U20 Championship', '', '', '', '', '', '', 'null', 141414, '2025-06-16 14:00:02'),
-- ('2025-06-19 00:00:00', 'ALL DAY', 0, 'A', 'Eugene, Ore.', 'Cross Country / Track & Field', 'TRACK', 'USATF U20 Championship', '', '', '', '', '', '', 'null', 141415, '2025-06-16 14:00:02'),
-- ('2025-06-19 00:00:00', 'ALL DAY', 0, 'A', 'Eugene, Ore.', 'Cross Country / Track & Field', 'TRACK', 'USATF U20 Championship', '', '', '', '', '', '', 'null', 141416, '2025-06-16 14:00:02');

-- --------------------------------------------------------

--
-- Table structure for table benches
--

CREATE TABLE IF NOT EXISTS benches (
  benchid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  material TEXT CHECK('Metal' IN ('Metal','Plastic','Wooden','Concrete')) NOT NULL,
  description TEXT NOT NULL,
  dedication TEXT NOT NULL,
  swinging INTEGER NOT NULL DEFAULT '0',
  lakeview INTEGER NOT NULL DEFAULT '0',
  picnic INTEGER NOT NULL DEFAULT '0',
  latitude REAL NOT NULL,
  longitude REAL NOT NULL
);

--
-- Dumping data for table benches
--

INSERT INTO benches (benchid, material, description, dedication, swinging, lakeview, picnic, latitude, longitude) VALUES
(1, 'Metal', 'Outside Plyler Hall entrance along Milford Mall', 'In honor of Gayle Warth for her more than 45 years of dedicated service to Furman University', 0, 0, 0, 34.92366259, -82.43815116),
(2, 'Metal', 'Next to Milford Mall fountains, outside Riley Hall, overlooking the Joseph Vaughn Plaza and the James Duke Library', '', 0, 0, 0, 34.92406354, -82.43852017),
(3, 'Metal', 'Overlooking Milford Mall fountains and Daniel Chapel', '', 0, 0, 0, 34.92365861, -82.43764694),
(4, 'Metal', 'Overlooking Milford Mall fountain and Daniel Chapel', '', 0, 0, 0, 34.92382938, -82.43749179),
(5, 'Metal', 'Outside Furman Hall overlooking Milford Mall and Library', '', 0, 0, 0, 34.92414942, -82.43742038),
(6, 'Wooden', 'Outside Furman Hall overlooking Milford Mall fountains and Plyler', 'In honor of Judith Bainbridge, Professor of English, for her exception service to Furman University and it’s students', 0, 0, 0, 34.92420416, -82.43753782),
(7, 'Wooden', 'Outside Furman Hall entrance overlooking courtyard', 'In honor of John S. McCutcheon, M.D. A joyful and ageless student. ', 0, 0, 0, 34.92489937, -82.4372377),
(8, 'Wooden', 'Outside Furman Hall', 'In honor of Robert H. Lutz Jr. Furman trustee. ', 0, 0, 0, 34.92482686, -82.43732068),
(9, 'Metal', 'Overlooking Library', 'In honor of Philip and Hazel Winstead', 0, 0, 0, 34.92453229, -82.43814737),
(10, 'Wooden', 'Overlooks brick pathway', 'In Loving Memory of Tom Carter', 0, 0, 0, 34.92415248, -82.43930181),
(11, 'Wooden', '', 'Come sit and share a smile! Live life to the fullest. Dedicated by Buddy Price and Dinah Cisson, August 2022 ', 0, 0, 0, 34.92419012, -82.43939523),
(12, 'Wooden', '', 'Bloom where you are planted!!! Drs. Christine Caputo Winn ‘90 and Robert J. Winn ‘91', 0, 0, 0, 34.92399438, -82.43926429),
(13, 'Wooden', '', '', 0, 0, 0, 34.92401019, -82.4394152),
(14, 'Wooden', '', '', 0, 0, 0, 34.92407146, -82.43946706),
(15, 'Wooden', 'Dining Hall Picnic Table near lake', '', 0, 1, 1, 34.9261133, -82.44020108),
(16, 'Wooden', 'DH Picnic Table near lake', '', 0, 1, 1, 34.9261224, -82.4400133),
(17, 'Metal', 'Outside chapel overlooking Milford Mall and ', 'In memory of H.C. Williams and Louise McClellan Williams, parents of Louise Williams Stanford, ‘66', 0, 0, 0, 34.92332801, -82.43661657),
(18, 'Metal', 'Outside chapel overlooking Furman mall ', 'In Memory of John Wilbert Wood, 1917, and Essie Meares Wood, 1919. By Kathleen Wood Brown ‘44 and Mary Louise Wood Bagby, ‘69', 0, 0, 0, 34.92317124, -82.43673758),
(19, 'Metal', 'In center of Furman Mall', 'SAE Chapter Eternal', 0, 0, 0, 34.92314707, -82.43698673),
(20, 'Wooden', 'Overlooking chapel & mall', 'In memory of “The Prez” Alan S. Altman, ‘79, our ??? brother.', 0, 0, 0, 34.92331547, -82.43709033),
(21, 'Wooden', 'Overlooking Milford Mall and fountains. ', 'In memory of Wayne Anthony “Tony” Hux, ‘80, our ??? brother. ', 0, 0, 0, 34.92333529, -82.43711382),
(22, 'Wooden', 'Overlooks chapel ', 'In memory of Martin Wright Foster, ‘79, our ??? brother. ', 0, 0, 0, 34.92350426, -82.43694345),
(23, 'Wooden', 'Looks down Furman Mall to main loop. ', 'In memory of James Edward “Jim” Hollis, ‘80, our ??? brother.', 0, 0, 0, 34.92351741, -82.43695734),
(24, 'Metal', 'Looks up Furman Mall to Lays Physical Activities Center', 'SAE Chapter Eternal. In memory of Jasper “Jay” William Huff III, ‘77, William Carl “Wally” Schilling, ‘79, and Eugene H. “Gene” Howe, Jr. ‘81, our SAE brothers.  ', 0, 0, 0, 34.92350725, -82.43670181),
(25, 'Metal', 'Outside Furman Hall breezeway.', '', 0, 0, 0, 34.92423602, -82.43767959),
(26, 'Wooden', 'Overlooking Echo Circle', 'In honor of Joseph and Evelyn Shi', 0, 0, 0, 34.92449302, -82.43770276),
(27, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Mall', '', 0, 0, 0, 34.92469719, -82.4368903),
(28, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Mall', '', 0, 0, 0, 34.9246705, -82.43691043),
(29, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Mall', '', 0, 0, 0, 34.92464175, -82.43693504),
(30, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Mall', '', 0, 0, 0, 34.92462277, -82.43694866),
(31, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Hall. ', '', 0, 0, 0, 34.92460539, -82.43689427),
(32, 'Wooden', 'Outside Furman Hall and 9/11 Memorial. Overlooking Furman Hall. ', '', 0, 0, 0, 34.92467146, -82.43682885),
(33, 'Metal', 'Overlooks Furman Hall. ', 'In memory of Raymond W. Heatwole, Professor of Business Administration Emeritus, 1941-1972', 0, 0, 0, 34.92447699, -82.43699719),
(34, 'Metal', 'Part of Joseph Vaughn Plaza. ', 'In memory of George A. Fant, ‘33, Father, Scholar, Friend, Athlete.', 0, 0, 0, 34.92444954, -82.43854638),
(35, 'Metal', 'Part of Joseph Vaughn Plaza. ', 'In memory of Norvelle and Charlie Shaw, Mullins, SC', 0, 0, 0, 34.92428211, -82.43865483),
(36, 'Plastic', 'Library Porch ', '', 0, 0, 0, 34.92435912, -82.43875392),
(37, 'Plastic', 'Library Porch', '', 0, 0, 0, 34.92447672, -82.43868762),
(38, 'Wooden', 'Outside Plyler Hall overlooking rock garden. ', 'In memory of Lois and Ken Hopping, with love. Connie and Noel Kane-Maguire', 0, 0, 0, 34.92323089, -82.43865564),
(39, 'Wooden', 'Rock Garden Compass', '', 0, 0, 0, 34.92318781, -82.43902185),
(40, 'Wooden', 'Rock Garden Compass', '', 0, 0, 0, 34.92321534, -82.4391138),
(41, 'Wooden', 'Rock Garden compass', '', 0, 0, 0, 34.92326447, -82.43906763),
(42, 'Plastic', 'Outside Art Building overlooking Lakeside Loop', '', 0, 0, 0, 34.92669915, -82.43592269),
(43, 'Metal', 'Chiles Patio. ', '', 0, 0, 0, 34.92725502, -82.43710225),
(44, 'Wooden', 'Swing overlooking Chiles Patio & Chiles', '', 1, 0, 0, 34.92728734, -82.43691678),
(45, 'Wooden', 'Swing overlooking Chiles Patio and Art Building. ', '', 1, 0, 0, 34.92737624, -82.43719996),
(46, 'Wooden', 'Playhouse Porch', '', 0, 0, 0, 34.92812303, -82.4344483),
(47, 'Metal', 'Overlooks main loop', '“Sam and Louise’s Bench.” From the Musical “In the Silence” by Robert Phillip Cushing, ‘20', 0, 0, 0, 34.9262374, -82.43466753),
(48, 'Metal', 'Overlooks main loop. ', '“Everything you sing must ring!” In honor of Dr. Ramon Kyser, Professor of Voice 1971-1997, by his students, colleagues and friends. September 1, 2010. ', 0, 0, 0, 34.92616472, -82.43437525),
(49, 'Wooden', 'Outside McAlister Auditorium. ', '', 0, 0, 0, 34.92634495, -82.4349504),
(50, 'Wooden', 'Outside McAlister Auditorium. ', '', 0, 0, 0, 34.92643781, -82.43521793),
(51, 'Wooden', 'Outside McAlister Auditorium. ', '', 0, 0, 0, 34.92646886, -82.43518684),
(52, 'Wooden', 'Outside McAlister Auditorium. ', '', 0, 0, 0, 34.92649125, -82.43514984),
(53, 'Metal', 'Beside admissions parking lot & patio', 'This site honors the memory of John E. Johns, ‘47. President - Furman University, 1976-1994. ', 0, 0, 0, 34.92569251, -82.43624574),
(54, 'Metal', 'Overlooks brickyard between Johns Hall, Furman Hall and Earle Health', 'In memory of Gordon L. Blackwell, Jr, ‘60. Furman Trustee, 1999-2006. ', 0, 0, 0, 34.92544187, -82.43698395),
(55, 'Metal', 'Overlooks Johns Hall. ', 'In memory of Laxton Hamrick, Class of 1932. Given by his family. ', 0, 0, 0, 34.92555468, -82.4370805),
(56, 'Wooden', 'Pier with benches over the lake, beside PalaDen dining area ', 'Carrozza Shade Pavilion', 0, 1, 0, 34.92486277, -82.44087173),
(57, 'Wooden', 'Pier outside Paddock overlooking lake. ', 'Fowler Shade Pavilion, Generously provided by Vicki C. and Stephen S. Fowler, in honor of their daughter Casey S. Fowler, ‘16.', 0, 1, 0, 34.92502212, -82.44072996),
(58, 'Metal', 'Bench outside Rose Garden overlooking lake. ', '', 0, 1, 0, 34.92532319, -82.44026224),
(59, 'Metal', 'Bench outside Rose Garden overlooking lake. ', '', 0, 1, 0, 34.9253515, -82.44023034),
(60, 'Concrete', 'Gazebo in center of Rose Garden. ', 'This gazebo is the gift of Ted Douglas Smith and Wanda Huskey-Smith. Brought to Greenville from Florence, Italy in the 1960s by Guy and Dorothy Hipp Gunter, it was given to Furman University in December of 2000. ', 0, 0, 0, 34.92519368, -82.44004597),
(61, 'Concrete', '', '', 0, 1, 0, 34.92562893, -82.44031395),
(62, 'Concrete', '', '', 0, 1, 0, 34.92571716, -82.44039182),
(63, 'Concrete', '', '', 0, 1, 0, 34.92579875, -82.44045142),
(64, 'Concrete', '', '', 0, 1, 0, 34.92591164, -82.44047347),
(65, 'Wooden', 'DH lakeside picnic table ', '', 0, 1, 1, 34.92593865, -82.44039756),
(66, 'Concrete', '', '', 0, 1, 0, 34.92601997, -82.44046175),
(67, 'Concrete', '', '', 0, 1, 0, 34.92612149, -82.44042237),
(68, 'Concrete', '', '', 0, 1, 0, 34.92620947, -82.4403565),
(69, 'Concrete', '', '', 0, 1, 0, 34.92628719, -82.44026777),
(70, 'Concrete', '', '', 0, 1, 0, 34.92635051, -82.44014541),
(71, 'Wooden', 'DH lakeside picnic table. Regularly moves. ', '', 0, 1, 1, 34.92633782, -82.44003995),
(72, 'Concrete', '', '', 0, 1, 0, 34.92638207, -82.44001735),
(73, 'Concrete', '', '', 0, 1, 0, 34.92639488, -82.43990939),
(74, 'Wooden', 'Riley Institute porch patio bench, looking over DH’s parking lot entrance.  ', '', 0, 1, 0, 34.92601476, -82.43931372),
(75, 'Concrete', 'Bench walls around fountain. ', 'Golden Reunion Plaza - Provided by the classes of 1954 and 1955 in recognition of their 50th reunions. ', 0, 0, 0, 34.92491009, -82.43952352),
(76, 'Wooden', 'Near grill', '', 0, 0, 0, 34.92961068, -82.43486792),
(77, 'Wooden', '', '', 0, 0, 0, 34.92962081, -82.43489936),
(78, 'Wooden', 'Near path behind A and B. ', '', 0, 0, 0, 34.9298333, -82.43502032),
(79, 'Wooden', 'Behind C looking into forest ', '', 0, 0, 0, 34.93125322, -82.43479656),
(80, 'Wooden', 'Behind E looking into woods', '', 0, 0, 0, 34.93086212, -82.43554884),
(81, 'Wooden', 'Behind E and F looking into woods. ', '', 0, 0, 0, 34.93032959, -82.43560677),
(82, 'Wooden', 'Small covered wooden structure in Asian gardens near place of peace. ', '', 0, 0, 0, 34.92893186, -82.43645219),
(83, 'Metal', '', 'This bench honors the memory of Shirley G. Mangles. Continuing Education 1987-2008. ', 0, 1, 0, 34.92858652, -82.43809886),
(84, 'Metal', 'Overlooks lake outside eco cabins. ', 'Megan B. Gallagher Class of 2007. Forever a rising junior. ', 0, 1, 0, 34.92853034, -82.43861253),
(85, 'Metal', '', 'In memory of Larry D. Estridge ‘66. Esteemed member of the Furman University Board of Trustees. ', 0, 1, 0, 34.9285296, -82.43903839),
(86, 'Metal', '', 'Beulah Jean Hinchman. 2022, who through her perseverance made Furman a reality for her daughter. ', 0, 1, 0, 34.92849631, -82.43933439),
(87, 'Wooden', 'Bell Tower Point bench at the base of Bell Tower. ', '', 0, 1, 0, 34.92785366, -82.43992879),
(88, 'Wooden', 'Bell Tower Point bench', 'Given in memory of Peggy and Ken Lingerfelt, loving parents of Laura Lingerfelt Ritter, ‘90', 0, 1, 0, 34.92778144, -82.43995631),
(89, 'Wooden', 'Bell Tower Point bridge. ', 'Sondra Ann Langweil 5/19/1934 - 7/6/2022. Always loved, never forgotten, forever missed. ', 0, 1, 0, 34.92780761, -82.44003031),
(90, 'Wooden', 'Bell Tower Point bench. ', '', 0, 1, 0, 34.92787315, -82.43999422),
(91, 'Concrete', 'One of two F benches outside Shi gardens. ', '1925 Dr. John Todd Anderson. Furman Student. Medical missionary to China. Born 1887. Died 1918. Memorial erected by classes of 1909, 1910, 1911. ', 0, 1, 0, 34.9292148, -82.43978193),
(92, 'Concrete', 'One of two F benches outside Shi Center. Transported from Old Campus. ', '1925 Dr. John Todd Anderson. Furman Student. Medical missionary to China. Born 1887. Died 1918. Memorial erected by classes of 1909, 1910, 1911. ', 0, 1, 0, 34.92924382, -82.4398004),
(93, 'Wooden', '', 'Donated by the class of 2017. ', 1, 1, 0, 34.92969543, -82.4398817),
(94, 'Wooden', '', 'This memorial is in honor of Caroline Smith ‘21. Kappa Delta sister, talented artist and loving friend. A light to this campus and in this world.  ', 1, 1, 0, 34.92749695, -82.43809238),
(95, 'Wooden', '', 'This memorial is in honor of Caroline Smith ‘21. Kappa Delta sister, talented artist and loving friend. A light to this campus and in this world.', 1, 1, 0, 34.92744846, -82.43798423),
(96, 'Concrete', '', '', 0, 1, 0, 34.93004096, -82.44021446),
(97, 'Wooden', '', '', 0, 1, 0, 34.93069102, -82.4412132),
(98, 'Wooden', '', '', 0, 1, 0, 34.93066366, -82.44120513),
(99, 'Concrete', '', '', 0, 1, 1, 34.92924267, -82.44110104),
(100, 'Concrete', '', '', 0, 1, 0, 34.92919653, -82.4418229),
(101, 'Concrete', '', '', 0, 1, 0, 34.92907382, -82.44169937),
(102, 'Metal', '', 'Salvatore Vincent Ardizzone and Vincent Frank Ardizzone. Forever in our hearts and dreams. ', 0, 1, 0, 34.92884877, -82.44207674),
(103, 'Concrete', '', '', 0, 1, 0, 34.92886876, -82.44165321),
(104, 'Concrete', '', '', 0, 1, 0, 34.92855522, -82.44138787),
(105, 'Wooden', '', 'In loving memory of Christopher Joseph Cahill, May 21, 1981 - May 29, 2002. Mt. Pleasant, SC. Christopher Cahill’s life was cut tragically short as the victim of a drunk driving accident his Junior year…', 0, 1, 0, 34.92846418, -82.44099292),
(106, 'Concrete', '', '', 0, 1, 0, 34.92807204, -82.44140572),
(107, 'Wooden', '', 'In memory of Grady Baldwin Anthony, Class of 2010', 1, 1, 0, 34.92739953, -82.44132995),
(108, 'Wooden', '', 'Donated by the class of 2012. ', 1, 1, 0, 34.927311, -82.44152921),
(109, 'Concrete', '', '', 0, 1, 0, 34.92769719, -82.44209351),
(110, 'Concrete', '', '', 0, 1, 1, 34.92761636, -82.44234678),
(111, 'Concrete', '', '', 0, 1, 1, 34.92735463, -82.44234215),
(112, 'Wooden', '', '', 0, 1, 0, 34.9272749, -82.44186193),
(113, 'Concrete', '', '', 0, 1, 0, 34.92750856, -82.4422348),
(114, 'Concrete', '', '', 0, 1, 0, 34.92646889, -82.44266725),
(115, 'Concrete', '', '', 0, 1, 0, 34.92598644, -82.44304791),
(116, 'Concrete', '', '', 0, 1, 0, 34.92580602, -82.4432439),
(117, 'Metal', '', '', 0, 1, 0, 34.92551837, -82.44386114),
(118, 'Metal', '', '', 0, 1, 0, 34.92546319, -82.4439321),
(119, 'Concrete', '', '', 0, 1, 0, 34.93087541, -82.44135742),
(120, 'Metal', 'Nature’s Shrine', '', 0, 0, 0, 34.93213955, -82.44138787),
(121, 'Metal', 'Morgan Meditation Garden. ', 'Morgan Meditation Garden. Given by Martha Frances Morgan, ‘35, and Ethel Elizabeth Morgan, ‘37. In memory of our parents Frank Burt and Ethel Robinson Morgan, Jr. Dedicated May 1, 2001.  ', 0, 0, 0, 34.93291282, -82.44199376),
(122, 'Metal', 'Morgan Meditation Garden. ', 'Morgan Meditation Garden. Given by Martha Frances Morgan, ‘35, and Ethel Elizabeth Morgan, ‘37. In memory of our parents Frank Burt and Ethel Robinson Morgan, Jr. Dedicated May 1, 2001.  ', 0, 0, 0, 34.93294579, -82.44204707),
(123, 'Concrete', '', '', 0, 1, 0, 34.9297639, -82.43993055),
(124, 'Plastic', 'Between Manley and McGlo and Blackwell', '', 0, 0, 0, 34.92297859, -82.44125725),
(125, 'Metal', 'Soho Square', '', 0, 0, 1, 34.92290828, -82.44145324),
(126, 'Plastic', 'McGlo Entrance', '', 0, 0, 0, 34.92274291, -82.44150193),
(127, 'Metal', '', 'In Memory of Halle Cathryn Mikel Ching. February 3, 2010 – November 7, 2023. Though Halle could not communicate in the tradition sense, Halle radiated love and all who knew her felt it, and felt better in her presence. Donated with love, Furman Community.', 0, 1, 0, 34.92536449, -82.44042587);

-- --------------------------------------------------------

--
-- Table structure for table buildingHours
--

CREATE TABLE IF NOT EXISTS buildingHours (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  buildingID INTEGER NOT NULL,
  day TEXT NOT NULL,
  dayorder INTEGER NOT NULL,
  Start time DEFAULT NULL,
  End time DEFAULT NULL,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (buildingID) REFERENCES buildingLocations(buildingID)
);

--
-- Triggers buildingHours
--
-- BEFORE UPDATE: Delete from updateTimes
CREATE TRIGGER buildingHours_beforeUpdate
BEFORE UPDATE ON buildingHours
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingHours';
END;

-- BEFORE DELETE: Delete from updateTimes
CREATE TRIGGER buildingHours_deleteUpdateTimesOnDelete
BEFORE DELETE ON buildingHours
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingHours';
END;

-- BEFORE INSERT: Delete from updateTimes
CREATE TRIGGER buildingHours_deleteUpdateTimesOnInsert
BEFORE INSERT ON buildingHours
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingHours';
END;

-- AFTER DELETE: Insert into updateTimes
CREATE TRIGGER buildingHours_deleted
AFTER DELETE ON buildingHours
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingHours');
END;

-- AFTER INSERT: Insert into updateTimes
CREATE TRIGGER buildingHours_inserted
AFTER INSERT ON buildingHours
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingHours');
END;

-- AFTER UPDATE: Insert into updateTimes
CREATE TRIGGER buildingHours_updated
AFTER UPDATE ON buildingHours
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingHours');
END;


-- --------------------------------------------------------

--
-- Table structure for table buildingLocations
--

CREATE TABLE IF NOT EXISTS buildingLocations (
  buildingID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  nickname TEXT DEFAULT NULL,
  category TEXT NOT NULL,
  hasHours INTEGER NOT NULL DEFAULT '0',
  website TEXT NOT NULL,
  location TEXT DEFAULT NULL,
  latitude REAL DEFAULT NULL,
  longitude REAL DEFAULT NULL,
  polyline TEXT DEFAULT NULL,
  description TEXT DEFAULT NULL,
  frequency INTEGER NOT NULL DEFAULT '10',
  last_updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--
-- Dumping data for table buildingLocations
--

INSERT INTO buildingLocations (buildingID, name, nickname, category, hasHours, website, location, latitude, longitude, polyline, description, frequency, last_updated) VALUES
(1, 'Earle Health Center', 'Infirmary', 'auxiliary', 1, 'https://www.furman.edu/offices-services/student-health-center/', 'Between Lakeside Housing and Johns Hall', 34.9257, -82.4377, 'gndtEhcdvNH[LFDINFEJPJCNGCCJWOMG', 'Earle Health is the primary medical provider on campus. Students can make appointments to speak with a doctor from Prisma Health.', 10, '2020-07-26 00:42:18'),
(2, 'Trone Student Center', 'Trone', 'auxiliary', 1, 'https://www.furman.edu/campus-life/trone-student-center/', 'Near the Furman lake and South Housing', 34.9245, -82.4405, 'ghdtEhrdvNP]ZXHMn@d@KP@BDC\\VEJNN\\TGHFFMTGAADS\\k@g@Re@a@_@GLHDS^IGm@c@\\o@DG[Y', 'Trone is the central hub for student activity on campus; it also has various dining options, the campus mail room, a theater, conference rooms, career services, international travel, and more.', 10, '2020-07-26 00:42:18'),
(3, 'Bell Tower Bookstore & Bistro', 'Bookstore', 'auxiliary', 1, 'https://www.bkstr.com/furmanstore/home', 'Bottom floor of Trone Student Center near P2X', 34.9244, -82.441, NULL, 'The main Furman bookstore, for all merchandise needs.', 5, '2020-07-26 00:42:18'),
(4, 'Print & Post Express', 'P2X', 'auxiliary', 1, 'https://www.furman.edu/p2x/', 'Bottom floor of Trone Student Center near Barnes & Noble', 34.9245, -82.4406, NULL, 'P2X provides printing services and mail boxes for students on campus.', 0, '2020-07-26 00:42:18'),
(5, 'Physical Activities Center', 'The PAC', 'auxiliary', 1, 'https://www.furman.edu/campus-recreation/facilities-hours/', 'Near the Football Stadium and Soccer Field', 34.9211, -82.4396, 'gpctEzndvN@f@f@o@e@i@c@p@', 'The PAC is the main student gym, and exercise equipment and recreational basketball courts.', 10, '2020-07-26 00:42:18'),
(6, 'James B. Duke Library', 'Duke Library', 'academic', 1, 'https://www.furman.edu/virtual-campus-tour/james-b-duke-library/', 'Big building - center of campus', 34.9244, -82.4387, 'gfdtErhdvNNJRNEJJJFH\\T_AnBUUEBICGCIIIIGKEKUSbAsB@CNJ', 'The Duke Library is the main library for campus. Research services, the IT service center (ITS), and the writing and media lab (WML) are all located in the building.', 10, '2020-07-26 00:42:18'),
(7, 'Enrollment Services', '', 'auxiliary', 1, 'https://www.furman.edu/enrollment-services/', 'First floor of the Furman Administration Building near Furman Hall  ADM-102', 34.9255, -82.4366, '', 'Enrollment services helps students with any issues related to their time at Furman.', 10, '2020-07-26 00:42:18'),
(8, 'Counseling Center', NULL, 'auxiliary', 1, 'https://www.furman.edu/counseling-center/appointment/', 'Bottom floor of Earle Student Health Center', 34.9257, -82.4379, '', 'The Trone Center for Mental Fitness provides free counseling services for students. ', 0, '2020-07-26 00:42:18'),
(16, 'Riley Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/riley-hall/', NULL, 34.9236, -82.4389, 'wadtElhdvNfBrBXa@mBwB', 'Riley Hall is home to the Mathematics (MTH), Economics (ECN), and Computer Science (CSC) departments.', 5, '2020-07-26 00:45:07'),
(17, 'Hipp Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/hipp-hall/', NULL, 34.9235, -82.4399, 'madtExqdvNHICGHIAC?AHGACNMEG\\_@f@z@iAjAY_@', 'Hipp Hall is home to the Business (BUS), Education (EDU), and Accounting (ACT) departments.', 5, '2020-07-26 00:45:07'),
(18, 'Plyler Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/charles-townes-center-plyler-hall/', NULL, 34.923, -82.4386, 'i|ctEbldvN]j@NPPPDBXc@EGl@u@D@HIh@t@X]e@q@MMDGW[GDSWKN_@_@JO[]BG[]EHw@u@Sd@n@l@KNlBrBa@l@', 'Plyler Hall is the main science building. Physics (PHY), Chemistry (CHM), Biology (BIO), and Earth, Environmental, and Sustainability Sciences (EES) departments.', 5, '2020-07-26 01:51:58'),
(19, 'Johns Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/john-e-johns-hall/', NULL, 34.925, -82.4377, 'ihdtEdcdvNtA~@Ne@cBeASMNe@c@UM@GCEDK@DBCLZNHO@Z', 'Johns Hall is the main social sciences building. The Politics and International Affairs (POL), Psychology (PSY), and Sociology (SOC)  departments are all in Johns, as well as the Sleep Lab and the Riley Institute. ', 5, '2020-07-26 01:51:58'),
(20, 'Furman Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/furman-hall/', NULL, 34.9245, -82.4372, 'ujdtEx|cvNNi@|A|@FBBE^PCFdBlAOf@iBmACLa@UBGaB_A', 'Furman Hall is the main humanities and languages building. The Religion (REL), Classics (CLS), Philosophy (PHL), Modern Language & Literature (including Spanish (SPN), French (FRN), and German (GRM)), Asian Studies (AST) and History (HST) departments are located here.', 5, '2020-07-26 22:44:11'),
(21, 'Chapel', NULL, 'auxiliary', 0, 'https://www.furman.edu/spiritual-life/daniel-chapel/', NULL, 34.9231, -82.4365, 'k}ctEj{cvNTP@IFDNUGGb@y@YS_@v@GEMVHHGH', 'The Daniel Chapel is the center of religious life at Furman. The Chaplin''s offices, and the Office of Spiritual Life, are housed in the basement.', 5, '2020-07-26 22:46:24'),
(22, 'Amphitheater', NULL, 'auxiliary', 0, 'https://www.furman.edu/academics/music/facilities/lakeside-amphitheater/', NULL, 34.9303, -82.4399, 'ojetExrdvN|@SBOB?Ji@KMDEBK@ECMIACE?KGEK?MDGFIJEFEPCPATAT@N@J?J', 'The amphitheater offers a great space for outdoor events.', 5, '2020-07-26 22:53:06'),
(23, 'Shi Center for Sustainability', NULL, 'auxiliary', 0, 'https://www.furman.edu/shi-institute/', NULL, 34.9292, -82.4389, 'acetEvkdvNT?@KBA@o@GA?UG??UUA?X?DF?AjA', 'The Shi Center is dedicated to helping promote sustainable living, on campus and off. It is flanked by the Furman Farm and the Asian Gardens. ', 5, '2020-07-26 22:54:08'),
(24, 'Golf Course', 'Golf Course', 'athletics', 0, 'https://www.furmangolfclub.com/', 'Entrance is off of Hwy 25', 34.9318, -82.4499, 'kretEplfvN[g@a@Za@d@]]Kq@G{@@m@FgB@_Cf@cBdAqEf@eB|BoBh@m@j@iAz@_@xFeAdGdBhBXj@MpBJnAx@@d@TQv@ErBp@x@FjAD|@t@RLv@FnCr@?b@QTu@hA_Ap@e@|B@lAXb@?r@}@hAaBb@i@v@s@pAs@z@SpAoBpCuFfCsG~AeFgAyBeAeF}Cu@{@F{@?k@', NULL, 5, '2020-07-28 14:01:24'),
(25, 'Administration Building', 'Admin', 'auxiliary', 0, 'https://www.furman.edu/about/leadership/senior-administrators/', 'North end of Furman Hall', 34.9254, -82.4366, 'yldtEl{cvNx@b@Ng@{@a@Md@', 'Home to administrative offices, including the President''s office, Admissions, and  Enrollment', 0, '2021-06-15 14:55:29'),
(26, 'Timmons Arena', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/timmons-arena/8', 'Just past the football stadium', 34.9181, -82.4378, 'a~btEdcdvNF??BlADBAF?POISr@q@KQCDc@w@@CKO?UeAICj@WXQSSXi@l@r@fAPOJR', 'Timmons is the main basketball arena.', 5, '2021-06-15 14:53:24'),
(27, 'Cherrydale Alumni House', 'Cherrydale', 'auxiliary', 0, 'https://www.furman.edu/younts/cherrydale-alumni-house/', 'Top of the hill behind the PAC', 34.9176, -82.4407, 'yzbtEludvNPJAJTJPo@k@SCFCAAACLBDAF', 'Built in the 1850''s, this was the home of Furman''s first president. In 1999, it was moved onto campus and now is the headquarters of the alumni association.', 5, '2021-06-15 16:53:52'),
(29, 'Younts Conference Center', NULL, 'auxiliary', 0, 'https://www.furman.edu/younts/', 'Up-across parking lot from Timmons Arena', 34.9173, -82.44, '_zbtEfrdvNLc@CABEAADOB@@C|@ZAFPFEPOEOj@UIAESMCFMI', NULL, 5, '2021-06-15 16:57:33'),
(30, 'McAlister Auditorium', NULL, 'academic', 0, 'https://www.furman.edu/mcalister-auditorium/', 'On main traffic circle', 34.9265, -82.435, 'gudtEbqcvNV}@rAh@@G\\NWpAa@MBGuAk@', NULL, 5, '2021-06-15 16:59:36'),
(31, 'Furman Playhouse', 'Theatre', 'academic', 0, 'https://www.furman.edu/academics/theatre-arts/facilities-resources/playhouse/', 'Behind McAlister Auditorim', 34.9282, -82.4344, '{{dtE|ncvNH]c@QKZb@R', NULL, 5, '2021-06-15 17:01:53'),
(32, 'Estridge Commons', 'FUPO Building', 'auxiliary', 0, 'https://www.furman.edu/university-police/', 'Between North Village A and pedestrian bridge', 34.9288, -82.4354, '}etEhtcvNFLJIBDLKM_@G@CCKFFLIJ', NULL, 5, '2021-06-15 17:03:42'),
(33, 'Blackwell Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/blackwell-hall/', NULL, 34.923, -82.4416, 'a~ctElydvNPQ@p@BCNREDf@v@MNg@s@GBOWDEa@o@', NULL, 5, '2021-07-08 18:28:17'),
(34, 'McGlothlin Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/mcglothlin-hall/', NULL, 34.9226, -82.4418, '{yctE|zdvNz@|ADAVd@QP[e@CB{@}A', NULL, 5, '2021-07-08 18:29:56'),
(35, 'Poteat Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/poteat-hall/', NULL, 34.9222, -82.4416, 'cvctEj|dvNV@NOWg@@C_AeBQP|@jB', NULL, 5, '2021-07-08 18:29:56'),
(37, 'Paladin Stadium', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/paladin-stadium/6', NULL, 34.9202, -82.4371, '_nctEnddvNVWGI\\SHNPPBAl@Az@k@Zf@A_AISIKKM^_@Ue@S]ACDI@K@GBGDMBQ@QAMGUGGWI[EKAK@IFEFk@}@cChCDNa@xALRH?JXUTZh@HJ', NULL, 5, '2021-07-08 18:51:30'),
(38, 'John S. Roberts Rugby Field', 'Rugby Field', 'athletics', 0, 'https://rec.furman.edu/Facility/GetFacility?facilityId=109409b8-ca8f-4afb-bf63-67ae050cc153', NULL, 34.919, -82.4393, 'eectEtmdvNt@iClCrAq@dC', NULL, 5, '2021-07-08 18:51:30'),
(39, 'Manly Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/manly-hall/', NULL, 34.9232, -82.441, 'g_dtEttdvN|AhCTS_BkC', NULL, 5, '2021-07-08 18:54:40'),
(40, 'Geer Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/geer-hall/', NULL, 34.9229, -82.4405, 'e}ctEnrdvNR]n@|@t@fASVcB{B', NULL, 5, '2021-07-08 18:54:40'),
(41, 'Marshall and Vera Lea Rinker Hall', 'Rinker Hall', 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/charles-townes-center-plyler-hall/', NULL, 34.9234, -82.4387, 'i~ctEjidvNZi@]_@[j@\\\\', NULL, 0, '2021-07-08 18:54:40'),
(42, 'Roe Art Building', NULL, 'academic', 0, 'https://www.furman.edu/academics/art/facilities-resources/', NULL, 34.927, -82.4358, '_tdtEnycvNl@{Bs@]i@bCj@V', NULL, 5, '2021-07-08 18:54:40'),
(44, 'McBee Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/mcbee-hall/', NULL, 34.9265, -82.4382, '}qdtEffdvNXgA\\PWdAWK', NULL, 5, '2021-07-08 18:54:40'),
(45, 'Judson Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/judson-hall/', NULL, 34.9267, -82.4376, '}tdtEvadvNDUb@N|@@IV_Bo@', NULL, 5, '2021-07-08 18:54:40'),
(46, 'Townes Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/townes-hall/', NULL, 34.9265, -82.4379, 'urdtEzcdvNF[|@ZGZu@W', NULL, 5, '2021-07-08 18:54:40'),
(47, 'Ramsay Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/ramsay-hall/', NULL, 34.9271, -82.4376, 'qvdtEvadvNF[A^I\\}@_@', NULL, 5, '2021-07-08 18:54:40'),
(48, 'Haynsworth Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/haynsworth-hall/', NULL, 34.9273, -82.4377, 'owdtEhcdvNV_AZNU~@', NULL, 5, '2021-07-08 18:54:40'),
(49, 'Chiles Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/chiles-hall/', NULL, 34.9275, -82.4373, 'wxdtEfdvNHY|@^IVy@[', NULL, 5, '2021-07-08 18:54:40'),
(50, 'Gambrell Hall', NULL, 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/gambrell-hall/', NULL, 34.9276, -82.4369, 'sydtE|_dvNn@}BVLm@|B', NULL, 5, '2021-07-08 18:54:40'),
(51, 'Place of Peace', NULL, 'auxiliary', 0, 'https://www.furman.edu/place-peace/', NULL, 34.9282, -82.4366, 'k|dtEp{cvNPFFUSIER', NULL, 5, '2021-07-08 18:54:40'),
(52, 'North Village A', 'A', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9293, -82.4346, 'odetEvlcvNjAD\\SUo@MJISXSMa@YRMYJGOa@', NULL, 5, '2021-07-08 18:54:40'),
(53, 'North Village B', 'B', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.93, -82.4346, 'ieetEtmcvNDf@uC^Ci@\\GBPPCCa@@GD^REAQh@G', NULL, 5, '2021-07-08 18:54:40'),
(54, 'North Village C', 'C', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9311, -82.4344, 'spetEdmcvNH[j@RCLHBJ]@PI^JDFMh@VMd@qCmA', NULL, 5, '2021-07-08 18:54:40'),
(55, 'North Village D', 'D', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9315, -82.4357, 'yretE~scvNZ]bBlCY@Yg@HKKQSV[e@TUKQIJ', NULL, 5, '2021-07-08 18:54:40'),
(56, 'North Village E', 'E', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9307, -82.4359, 'enetElxcvN?k@tC@?l@e@??UU?@d@c@??c@Q??P', NULL, 5, '2021-07-08 18:54:40'),
(57, 'North Village F', 'F', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9298, -82.4361, '}hetExwcvN^RDKPFOb@^TN]LHELVPBELFLYgC_BM^', NULL, 5, '2021-07-08 18:54:40'),
(58, 'North Village G', 'G', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9323, -82.4367, '{uetEl~cvNKGFY\\JF_@GC?GSGFYNDHg@e@Qo@lD@PJg@', NULL, 5, '2021-07-08 18:54:40'),
(59, 'North Village H', 'H', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.933, -82.437, 'qxetEhdvNyAwCYZR\\HILVYXRZTSLRIHVh@XY', NULL, 5, '2021-07-08 18:54:40'),
(60, 'North Village I', 'I', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9332, -82.4358, 'u{etE|ycvNnAqC]YS@JHMRYUQb@VRKTMKO@', NULL, 5, '2021-07-08 18:54:40'),
(61, 'North Village K', 'K', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9344, -82.4372, 'ieftE~~cvNpCx@Hi@c@MEPQGHc@g@KGb@QGBSc@K', NULL, 5, '2021-07-08 18:54:40'),
(62, 'North Village J', 'J', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/residences/north-village/', NULL, 34.9326, -82.4349, 'wyetEzpcvNbCu@Jb@_@NEOQHRbAe@NMaAUFBN]J', NULL, 10, '2021-07-08 18:54:40'),
(63, 'Eugene Stone Soccer Stadium', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/stone-stadium/12', NULL, 34.9215, -82.4411, 'euctEbtdvNo@t@CL@HFTJVLVx@zAPG^n@DBFCDCRYJNj@k@QYd@_@?GKQLMm@mAw@qAIKIGMEK?EDEDGFGHIJEBGDCF', NULL, 5, '2021-07-08 18:57:37'),
(64, 'Mickel Tennis Center', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/mickel-tennis-center/13', NULL, 34.9191, -82.4425, 'u_ctEv_evNAqDCMEAK?U?Q?GH?H?P?\\@d@OQMGQ?QDOPCX@VFJKB?ZFBAJK??_@cACAhEbA??gA~B?@_BTAFC', NULL, 5, '2021-07-08 18:57:37'),
(65, 'Furman Belltower', NULL, 'auxiliary', 0, 'https://www.furman.edu/news/history-of-the-bell-tower/', NULL, 34.9278, -82.44, NULL, NULL, 5, '2021-07-08 18:57:37'),
(66, 'Greenbelt Engaged Living Community', 'Eco-Cabins', 'housing', 0, 'https://www.furman.edu/engaged-living/greenbelt-community/', NULL, 34.9288, -82.4389, 'setEvddvNNIH|@D~@Bz@It@ILGCCOBOBc@AsAAy@EU', NULL, 5, '2021-07-08 18:57:37'),
(67, 'Latham Baseball Stadium', NULL, 'athletics', 0, 'https://furmanpaladins.com/sports/2019/5/1/athletics-facilities-latham-baseball-stadium.aspx', NULL, 34.9218, -82.4426, 'etctEfaevNDL|@jAHIbAzAFBF?HAJIVOZ[JUNa@Da@Cg@Ke@K[IUO[S_@KOIAKHEMo@l@HLs@r@KKm@t@GJ', NULL, 5, '2021-07-08 18:57:37'),
(68, 'Pepsi Stadium', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/pepsi-stadium/11', NULL, 34.921, -82.4449, 'cqctEdpevN^?|@hAHEFHBCDAHIFIFGFOFO@Q@SAQCMCOGQEIGKGEKGKEgArAa@?Ap@', NULL, 5, '2021-07-08 18:58:54'),
(69, 'Student Office for Accessibility Resources', 'SOAR', 'auxiliary', 0, 'https://www.furman.edu/accessibility/accommodations/', 'Lower level of Hipp Hall in Suite 011', 34.9236, -82.4398, NULL, NULL, 0, '2021-07-28 13:47:45'),
(71, 'PalaDen', 'P-Den', 'dining', 1, 'https://www.furman.edu/campus-life/housing-dining/', 'First floor of Trone Student Center', 34.9247, -82.4405, NULL, NULL, 10, '2024-02-01 18:34:49'),
(75, 'Aquatic Center', 'PAC Pools', 'auxiliary', 1, 'https://www.furman.edu/campus-recreation/aquatics/', 'Located inside the back of the PAC.', 34.9207, -82.4399, 'snctEzpdvNJJ^e@MMa@b@', NULL, 10, '2024-02-01 19:00:32'),
(76, 'Daniel Dining Hall', 'DH', 'dining', 1, 'https://furman.cafebonappetit.com/', 'Alongside the lake.', 34.9257, -82.4395, '{ndtEpldvNNa@xAdACJRPO@IFI@M@MAMAIGGECGCIAKAI?O@GDIMO', NULL, 10, '2024-02-01 19:03:56'),
(77, 'The Paddock', NULL, 'dining', 1, 'https://www.furman.edu/campus-life/housing-dining/', 'Located alongside the lake on the first floor of Trone.', 34.9248, -82.4402, NULL, NULL, 10, '2024-02-01 19:06:20'),
(78, 'Traditions Grille', 'Golf Club', 'dining', 1, 'https://www.furmangolfclub.com/golf-course/traditions-grille', 'Located inside the Golf Club at the Furman Golf Course.', 34.9318, -82.4498, 'ksetEhofvNBSEABOB@BQTDGr@UC', NULL, 10, '2024-02-01 19:09:29'),
(79, 'Blend and Bowl', NULL, 'dining', 1, 'https://www.furman.edu/campus-life/housing-dining/', 'Located upstairs in the Dining Hall.', 34.9256, -82.4395, NULL, NULL, 10, '2024-02-01 19:11:05'),
(80, 'The Library Café', 'LibCaf', 'dining', 1, 'https://libguides.furman.edu/library/floor-plans/24-hours', 'Located off of the Duke Library porch.', 34.9244, -82.4389, '', NULL, 10, '2024-02-01 19:12:13'),
(81, 'Maxwell Music Library', 'Music Library', 'academic', 1, 'https://www.furman.edu/academics/music/facilities/maxwell-music-library/', 'Within the Daniel Music Building next to the campus'' main gate.', 34.9267, -82.4341, NULL, NULL, 10, '2024-02-22 19:12:32'),
(82, 'Sanders Science Library', 'Science Library', 'academic', 1, 'https://libguides.furman.edu/science/home', 'Within Plyler Hall', 34.9229, -82.4386, 'k{ctEngdvNKPTXLQGG?AF@DA@A@A@C@EAIEEECC@EBABAB?D?B?B', NULL, 10, '2024-02-22 19:20:46'),
(83, 'Special Collections & Archives', NULL, 'academic', 1, 'https://libguides.furman.edu/library/divisions/special-collections', 'Top floor of the James Duke library.', 34.9248, -82.439, '', NULL, 10, '2024-02-22 19:21:40'),
(84, 'Patrick Lecture Hall', NULL, 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/charles-townes-center-plyler-hall/', 'Main lecture hall in Plyler.', 34.9231, -82.4388, 'w|ctEzhdvNCFAH?FBH@BBBB@DBD@B?@ADCFEg@g@', NULL, 10, '2024-03-15 19:54:59'),
(85, 'Tailgating Field', NULL, 'athletics', 0, '', 'Next to football stadium', 34.9205, -82.438, '}mctEnddvNHMJIGI\\SHNPPBAl@bAOBQBO@Q?KAIGIGKOGK', NULL, 10, '2024-03-15 20:02:40'),
(86, '24-Hour Study Room', NULL, 'academic', 0, 'https://libguides.furman.edu/library/floor-plans/24-hours', 'Inside the LibCaf', 34.9244, -82.439, 'uddtEjdvNGJTRNUIKGJIK', NULL, 10, '2024-03-15 20:22:24'),
(87, 'Herring Center', NULL, 'auxillary', 0, 'https://www.furman.edu/academics/continuing-education/', NULL, 34.9168, -82.4391, 'oubtEzkdvNJ]DBRw@\\LAJLJEPBBCTFBEXB@I\\aAc@BS', NULL, 10, '2024-03-15 21:34:29'),
(88, 'DeSantis Pavilion ', NULL, 'auxillary', 0, 'https://www.furman.edu/younts/about/', 'Near the Cherrydale House', -82.4402, 34.9178, 'u{btElrdvNVJFYAA@GMGEHCAGV', NULL, 10, '2024-03-15 21:37:15'),
(89, 'The Riley Institute', NULL, 'auxillary', 0, 'https://www.furman.edu/riley/', 'Within Johns Hall', 34.9249, -82.4379, NULL, NULL, 10, '2024-03-15 21:42:48'),
(90, 'Hartness Pavilion', '', 'dining', 0, 'https://www.furman.edu/younts/other-venues-at-furman/', 'On Dining Hall top floor', 34.9255, -82.4395, 'okdtEnodvNLYUUBIl@d@Sh@MMGG', NULL, 10, '2024-03-15 21:52:02'),
(91, 'Daniel Music Building', 'MUBU', 'academic', 0, 'https://www.furman.edu/virtual-campus-tour/daniel-music-building/', NULL, 34.9265, -82.4346, 'ksdtElocvNz@Z^aBw@]ELGCBMc@UOf@C?Kd@DBADj@PGN', NULL, 10, '2024-03-15 22:14:24'),
(92, 'Alley Gymnasium', NULL, 'athletics', 0, 'https://furmanpaladins.com/facilities/alley-gymnasium/5', NULL, 34.9212, -82.4441, 'qsctEtkevN^_@AEn@u@JPDET\\GFDFSVDF{@z@c@o@', NULL, 10, '2024-03-15 23:54:58'),
(93, 'Belk Track Complex', 'Track', 'athletics', 0, 'https://furmanpaladins.com/facilities/irwin-belk-complex/14', NULL, 34.9197, -82.4415, 'ckctE|zdvNfDgDDDHAHCJ@PFTNLXDR?V?RITIJ]@o@n@e@d@c@b@KDMFO?OAOKOOKSESCY@WFS', NULL, 10, '2024-03-16 00:04:59'),
(94, 'Football Practice Fields', NULL, 'athletics', 0, 'https://www.furman.edu/news/furman-spring-athletic-festival-set-for-saturday/', NULL, 34.9204, -82.4407, 'ioctEhudvNrC{CpB~C_DfDiBiD', NULL, 10, '2024-03-16 00:23:29'),
(95, 'North Village Housing & Residence Life Office', 'Housing OFfices', 'housing', 0, 'https://www.furman.edu/campus-life/housing-residence-life/', 'Inside North Village J', 34.9324, -82.4351, NULL, NULL, 10, '2024-03-16 00:41:05'),
(96, 'Writing and Media Lab', 'WML', 'auxiliary', 0, 'https://www.furman.edu/academics/center-academic-success/writing-resources/', 'Basement floor of the library', 34.9244, -82.4389, NULL, 'The Writing and Media Lab''s trained student Consultants provide one-on-one or small group assistance with student writing and multimedia projects.. Located in the basement.', 10, '2024-04-04 18:12:40'),
(97, 'Bookstore Café', NULL, 'auxiliary', 0, 'https://furman.cafebonappetit.com/cafe/bookstore-cafe/', NULL, 34.9245, -82.4409, NULL, 'The Bookstore Café is a bistro-style café. Grab a coffee and pastry while you read your new textbooks!', 10, '2024-04-11 17:29:51');

--
-- Triggers buildingLocations
--
-- AFTER DELETE: Insert into updateTimes
CREATE TRIGGER buildingLocations_afterDelete
AFTER DELETE ON buildingLocations
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingLocations');
END;

-- AFTER UPDATE: Insert into updateTimes
CREATE TRIGGER buildingLocations_afterUpdate
AFTER UPDATE ON buildingLocations
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingLocations');
END;

-- BEFORE DELETE: Delete from updateTimes
CREATE TRIGGER buildingLocations_beforeDelete
BEFORE DELETE ON buildingLocations
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingLocations';
END;

-- BEFORE UPDATE: Delete from updateTimes
CREATE TRIGGER buildingLocations_beforeUpdate
BEFORE UPDATE ON buildingLocations
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingLocations';
END;

-- BEFORE INSERT: Delete from updateTimes
CREATE TRIGGER buildingLocations_deleteUpdateTimesOnInsert
BEFORE INSERT ON buildingLocations
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'buildingLocations';
END;

-- AFTER INSERT: Insert into updateTimes
CREATE TRIGGER buildingLocations_inserted
AFTER INSERT ON buildingLocations
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('buildingLocations');
END;

-- --------------------------------------------------------

--
-- Table structure for table BusStops
--

CREATE TABLE IF NOT EXISTS BusStops (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  stop TEXT NOT NULL,
  shortname TEXT NOT NULL,
  latitude REAL NOT NULL,
  longitude REAL NOT NULL,
  route TEXT NOT NULL,
  vehicleName TEXT NOT NULL
);

--
-- Dumping data for table BusStops
--

INSERT INTO BusStops (id, stop, shortname, latitude, longitude, route, vehicleName) VALUES
(1, 'Furman University Main Entrance', 'Front Gate', 34.9254, -82.4345, '503 Bus', 'bus503'),
(2, 'Cherrydale Point Shopping Center', 'Cherrydale', 34.8897668, -82.4027424, '503 Bus', 'bus503'),
(3, 'Greenlink Transit Center', 'Greenlink ', 34.8508135, -82.4008488, '503 Bus', 'bus503'),
(4, 'PAC', '', 34.9213, -82.4393, 'Daily Shuttle', 'amshuttle'),
(5, 'Library', '', 34.9243, -82.4385, 'Daily Shuttle', 'amshuttle'),
(6, 'DH', '', 34.926717, -82.438806, 'Daily Shuttle', 'amshuttle'),
(7, 'Chapel', '', 34.923302, -82.436785, 'Daily Shuttle', 'amshuttle'),
(8, 'McAlister', '', 34.926275, -82.43546, 'Daily Shuttle', 'amshuttle'),
(9, 'North Village J', '', 34.93243, -82.435527, 'Daily Shuttle', 'amshuttle'),
(10, 'Judson Hall', '', 34.9267, -82.4375, 'Walmart Shuttle', 'walmart'),
(44, 'W Washington St & N Academy St ', '', 34.8518433, -82.4025679, '503 Bus', 'bus503'),
(45, 'W Washington St & Butler Ave ', '', 34.852715, -82.4048255, '503 Bus', 'bus503'),
(46, 'W Washington St & N Hudson St ', '', 34.8537254, -82.4073869, '503 Bus', 'bus503'),
(47, 'W Washington St & Lloyd St ', '', 34.8555633, -82.4098646, '503 Bus', 'bus503'),
(48, 'W Washington St & Capital Ct ', '', 34.8573782, -82.4123499, '503 Bus', 'bus503'),
(49, 'Mulberry St & Hampton Ave ', '', 34.8592928, -82.4104185, '503 Bus', 'bus503'),
(50, 'Mulberry St & Jay St ', '', 34.8605959, -82.4077744, '503 Bus', 'bus503'),
(51, 'Rutherford St & W Earle St ', '', 34.86407, -82.4044987, '503 Bus', 'bus503'),
(52, 'Poinsett Hwy & Cathey St ', '', 34.869521, -82.404481, '503 Bus', 'bus503'),
(53, 'Poinsett Hwy & Lila St ', '', 34.8724127, -82.4044596, '503 Bus', 'bus503'),
(54, 'Poinsett Hwy & Old Paris Mountain Rd ', '', 34.876616, -82.4044357, '503 Bus', 'bus503'),
(55, 'Furman Hall Rd & City Heights Ct ', '', 34.8836437, -82.4024488, '503 Bus', 'bus503'),
(56, 'N Pleasantburg Dr & Furman Hall Rd ', '', 34.8893098, -82.3995061, '503 Bus', 'bus503'),
(57, 'N Pleasantburg Rd & State Park Rd ', '', 34.8912037, -82.4027201, '503 Bus', 'bus503'),
(58, 'Poinsett Hwy & Crestwood Dr ', '', 34.8944803, -82.409498, '503 Bus', 'bus503'),
(59, 'Poinsett Hwy & Mulligan St ', '', 34.8976834, -82.412723, '503 Bus', 'bus503'),
(61, 'New Plaza Dr & Poinsett Hwy ', 'Publix', 34.9118011, -82.427437, '503 Bus', 'bus503'),
(62, 'Poinsett Hwy & Abelia Dr ', 'Near the Pumphouse', 34.9018583, -82.4169132, '503 Bus', 'bus503'),
(63, 'N Pleasantburg Rd & Poinsett Hwy ', '', 34.8905881, -82.4050364, '503 Bus', 'bus503'),
(65, 'Furman Hall Rd & Cherrydale Dr ', '', 34.8828699, -82.4029729, '503 Bus', 'bus503'),
(66, 'Poinsett Hwy & Henry Street ', '', 34.875035, -82.4047125, '503 Bus', 'bus503'),
(67, 'Rutherford St & Stall St ', '', 34.8651417, -82.4045068, '503 Bus', 'bus503'),
(68, 'Rutherford St & James St ', '', 34.863733, -82.4045825, '503 Bus', 'bus503'),
(69, 'Mulberry St & Pinckney St ', '', 34.8601415, -82.4087085, '503 Bus', 'bus503'),
(70, 'Mulberry St & Pine St ', '', 34.8588073, -82.4113521, '503 Bus', 'bus503'),
(71, 'West Washington St & Shirley St ', '', 34.8572882, -82.4124268, '503 Bus', 'bus503'),
(72, 'West Washington St & Madison St ', '', 34.8556266, -82.409952, '503 Bus', 'bus503'),
(73, 'West Washington St & S Hudson St ', '', 34.8536495, -82.4072271, '503 Bus', 'bus503'),
(74, 'West Washington St & S Academy St ', '', 34.8518433, -82.4025679, '503 Bus', 'bus503'),
(75, 'Walmart in Travelers Rest', 'Walmart', 34.960352, -82.431366, 'Walmart Shuttle', 'walmart'),
(76, 'South Housing', 'SoHo', 34.922471, -82.440974, 'Daily Shuttle', 'amshuttle');

--
-- Triggers BusStops
--
CREATE TRIGGER AfterInsert
AFTER INSERT ON BusStops
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('stopData');
END;

-- --------------------------------------------------------

--
-- Table structure for table clps
--

CREATE TABLE IF NOT EXISTS clps (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL DEFAULT '-',
  description TEXT NOT NULL DEFAULT '-',
  location TEXT NOT NULL DEFAULT '-',
  date date DEFAULT NULL,
  start time DEFAULT NULL,
  end time DEFAULT NULL,
  organization TEXT NOT NULL DEFAULT '-',
  eventType TEXT NOT NULL DEFAULT 'CLP',
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--
-- Triggers clps
--
-- BEFORE INSERT: Update updateTimes
CREATE TRIGGER cl_onupdate
BEFORE INSERT ON clps
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'clps';
END;

-- AFTER INSERT: Update updateTimes
CREATE TRIGGER clps_on_insert
AFTER INSERT ON clps
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'clps';
END;

-- AFTER DELETE: Update updateTimes
CREATE TRIGGER clps_onDelete
AFTER DELETE ON clps
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'clps';
END;

-- --------------------------------------------------------

--
-- Table structure for table contacts
--

CREATE TABLE IF NOT EXISTS contacts (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  buildingID INTEGER NOT NULL,
  room TEXT NOT NULL,
  name TEXT DEFAULT NULL,
  number TEXT NOT NULL,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  priorityLevel INTEGER NOT NULL DEFAULT '0'
);

--
-- Dumping data for table contacts
--

INSERT INTO contacts (id, buildingID, room, name, number, lastUpdated, priorityLevel) VALUES
(1, 32, '', 'University Police', '8642942111', '2020-07-23 20:49:35', 99),
(2, 0, '', 'Furman Operator', '8642942000', '2020-06-30 02:26:42', 29),
(3, 0, '', 'Housing and Residence Life', '8642942092', '2020-06-30 02:31:10', 28),
(4, 0, '', 'RA for Lakeside / Clark Murphy', '8645468694', '2020-06-30 02:31:10', 27),
(5, 0, '', 'RA for South Housing', '8643319360', '2020-06-30 02:31:10', 27),
(6, 0, '', 'RA for North Village', '8644143533', '2020-06-30 02:31:10', 27),
(7, 0, '', 'RA for the Vinings', '8642464028', '2020-06-30 02:31:10', 27),
(11, 25, 'ADM-102', 'Registrar (Transcripts)', '8642942030', '2020-06-30 02:31:10', 0),
(12, 25, 'ADM-102', 'Student Accounts', '8642942030', '2020-06-30 02:31:58', 0),
(13, 25, 'ADM-101', 'Financial Aid', '8642942030', '2020-06-30 02:30:21', 0),
(15, 8, '', 'Counseling Center', '8642943031', '2020-07-14 18:54:34', 0),
(16, 1, '', 'Earle Student Health Center', '8645222000', '2020-07-14 18:54:34', 0),
(17, 7, 'ADM-102', 'Enrollment Services', '8642942030', '2020-07-14 18:56:39', 0),
(18, 26, 'Lobby', 'Athletic Ticket Office', '8642943099', '2020-06-30 02:29:30', 0),
(20, 30, '', 'Student Health Services', '8642942180', '2020-06-30 02:31:58', 0),
(22, 17, 'HIP-011', 'SOAR (Student Office of Accessibility Resources)', '8642942320', '2021-06-15 17:22:45', 0),
(29, 16, '002', 'Tutoring (Center for Academic Success)', '8642942244', '2021-06-15 17:43:52', 0),
(30, 31, '', 'Student Life', '8642942202', '2020-06-30 02:32:16', 0),
(32, 25, 'ADM-101', 'Admissions', '8642942034', '2020-06-30 02:28:01', 0),
(35, 31, 'TRN-209', 'Internship Office', '8642943110', '2021-06-15 17:29:15', 0),
(37, 14, 'LIB-033', 'IT Computer Services Help Desk', '8642943277', '2021-06-15 17:50:43', 0),
(38, 25, 'ADM-209', 'Academic Deans Office', '8642942064', '2021-06-15 17:25:00', 0),
(39, 3, '', 'Barnes & Noble', '8642942164', '2021-07-23 15:29:33', 0),
(41, 4, '', 'Post (Office) & Print Express', '8642942107', '2021-07-23 15:32:17', 0),
(80, 6, '', 'Library', '8642942190', '2020-07-14 18:56:39', 0),
(96, 27, '', 'Alumni Association', '8642943464', '2020-06-30 02:29:30', 0),
(99, 0, '', 'Give to Furman', '8642942475', '2020-06-30 02:30:21', 0),
(100, 21, '', 'Furman Chapel / Office of Spiritual Life', '8642942133', '2024-02-27 00:30:56', 0);

--
-- Triggers contacts
--
-- AFTER DELETE: Update updateTimes
CREATE TRIGGER contacts_afterDelete
AFTER DELETE ON contacts
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'contacts';
END;

-- AFTER UPDATE: Update updateTimes
CREATE TRIGGER contacts_afterUpdate
AFTER UPDATE ON contacts
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'contacts';
END;

-- AFTER INSERT: Update updateTimes
CREATE TRIGGER contacts_inserted
AFTER INSERT ON contacts
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'contacts';
END;

-- --------------------------------------------------------

--
-- Table structure for table DHmenu
--

CREATE TABLE IF NOT EXISTS DHmenu (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  meal TEXT NOT NULL,
  itemName TEXT NOT NULL,
  station TEXT NOT NULL,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--
-- Triggers DHmenu
--
CREATE TRIGGER dh_insert
AFTER INSERT ON DHmenu
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'DHmenu';
END;

-- --------------------------------------------------------

--
-- Table structure for table foodService
--

CREATE TABLE IF NOT EXISTS foodService (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT DEFAULT NULL,
  fullname TEXT NOT NULL DEFAULT '',
  location TEXT DEFAULT NULL,
  latitude REAL DEFAULT NULL,
  longitude REAL DEFAULT NULL,
  frequency INTEGER NOT NULL DEFAULT '0',
  busyness INTEGER NOT NULL DEFAULT '0',
  url TEXT NOT NULL DEFAULT ''
);

--
-- Dumping data for table foodService
--

INSERT INTO foodService (id, name, fullname, location, latitude, longitude, frequency, busyness, url) VALUES
(10, NULL, 'Papa John''s Pizza', 'Off Campus: 1507 Poinsett Hwy', 34.887977, -82.405793, 10, 0, 'https://www.papajohns.com/order/stores-near-me'),
(13, 'DH', 'Daniel Dining Hall', 'on the Lower level, by the lake', 34.925749, -82.439605, 10, 0, ''),
(17, NULL, 'Bread and Bowl', 'above the Dining Hall', 34.92584, -82.4396, 0, 0, ''),
(18, 'Lib Cafe', 'The Library Cafe', 'in the Library, enter on left side of Library porch', 34.9243, -82.4389, 0, 0, ''),
(21, 'Chik-Fil-A', 'Chick-Fil-A', 'in the PalaDen, lower level of Trone', 34.924727, -82.440253, 0, 0, ''),
(22, 'Moe''s', 'Moe''s', 'in the PalaDen, lower level of Trone', 34.924811, -82.440318, 0, 0, ''),
(23, 'Sushi', 'Sushi with Gusto', 'in the PalaDen, lower level of Trone', 34.924553, -82.440353, 0, 0, ''),
(25, NULL, 'The Paddock', 'next to PalaDen, lower level of Trone', 34.924872, -82.440564, 0, 0, ''),
(28, 'BN Cafe', 'Barnes & Noble Cafe', 'inside the Bookstore, lower level of Trone', 34.92441, -82.44094, 0, 0, ''),
(29, NULL, 'Traditions Grille', 'in the Clubhouse of the Golf Course', 34.931827, -82.449969, 0, 0, ''),
(30, NULL, 'P-Den', 'Lower level of Trone', 34.924735, -82.440381, 0, 0, '');

--
-- Triggers foodService
--
-- AFTER DELETE: Update updateTimes
CREATE TRIGGER foodService_afterDelete
AFTER DELETE ON foodService
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'foodService';
END;

-- AFTER UPDATE: Update updateTimes
CREATE TRIGGER foodService_afterUpdate
AFTER UPDATE ON foodService
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'foodService';
END;

-- AFTER INSERT: Update updateTimes
CREATE TRIGGER foodService_inserted
AFTER INSERT ON foodService
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'foodService';
END;

-- --------------------------------------------------------

--
-- Table structure for table FU20_RestaurantHours
--

CREATE TABLE IF NOT EXISTS FU20_RestaurantHours (
  hoursID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ManuallyEntered INTEGER NOT NULL DEFAULT '0',
  id INTEGER NOT NULL,
  meal TEXT DEFAULT NULL,
  start time DEFAULT NULL,
  end time DEFAULT NULL,
  dayOfWeek TEXT DEFAULT NULL,
  dayOrder INTEGER NOT NULL
);

-- --------------------------------------------------------

--
-- Table structure for table GolfDay
--

CREATE TABLE IF NOT EXISTS GolfDay (
  day date NOT NULL PRIMARY KEY,
  startTime time NOT NULL DEFAULT '16:30:00',
  teeInterval INTEGER NOT NULL DEFAULT '10',
  specialType TEXT DEFAULT NULL,
  scheduled INTEGER NOT NULL DEFAULT '0',
  scored INTEGER NOT NULL DEFAULT '0',
  purpleTotal INTEGER NOT NULL,
  whiteTotal INTEGER NOT NULL,
  notes TEXT NOT NULL
);

--
-- Dumping data for table GolfDay
--

INSERT INTO GolfDay (day, startTime, teeInterval, specialType, scheduled, scored, purpleTotal, whiteTotal, notes) VALUES
('0000-00-00', '16:30:00', 9, 'none', 0, 0, 0, 0, ''),
('2023-03-21', '16:30:00', 9, 'none', 1, 1, 0, 6, ''),
('2023-03-23', '16:30:00', 9, 'none', 1, 1, 7, 3, ''),
('2023-03-28', '16:30:00', 9, 'none', 1, 1, 2, 3, ''),
('2023-03-30', '16:30:00', 9, 'none', 1, 1, 3, -1, ''),
('2023-04-04', '16:30:00', 9, 'none', 0, 1, 6, 4, ''),
('2023-04-06', '16:30:00', 9, 'none', 1, 1, 0, 1, ''),
('2023-04-11', '16:30:00', 9, 'none', 1, 1, 11, 5, ''),
('2023-04-13', '16:30:00', 9, 'none', 1, 1, 0, 1, ''),
('2023-04-18', '16:30:00', 9, 'none', 1, 1, 3, 5, ''),
('2023-04-20', '16:30:00', 9, 'none', 1, 1, 2, -1, ''),
('2023-04-25', '16:30:00', 9, 'none', 1, 1, 5, 5, ''),
('2023-05-02', '16:30:00', 9, 'none', 1, 1, 2, 2, ''),
('2023-05-04', '16:30:00', 9, 'none', 1, 1, 1, -3, ''),
('2023-05-09', '16:30:00', 9, 'none', 1, 1, 4, 4, ''),
('2023-05-11', '16:30:00', 9, 'none', 1, 1, 2, -1, ''),
('2023-05-16', '16:30:00', 9, 'none', 1, 1, 6, 4, ''),
('2023-05-18', '16:30:00', 9, 'none', 1, 1, 1, 2, ''),
('2023-05-23', '16:30:00', 9, 'none', 1, 1, 6, 0, ''),
('2023-05-25', '16:30:00', 9, 'none', 1, 1, 4, 5, ''),
('2023-05-30', '16:30:00', 9, 'none', 1, 1, 3, 3, ''),
('2023-06-01', '16:30:00', 9, 'none', 1, 1, 0, 5, ''),
('2023-06-06', '16:30:00', 9, 'none', 1, 1, 2, 2, ''),
('2023-06-08', '16:30:00', 9, 'back9', 1, 1, 4, 6, ''),
('2023-06-13', '16:30:00', 9, 'none', 1, 1, 5, 1, ''),
('2023-06-15', '16:30:00', 9, 'none', 1, 1, 1, 3, ''),
('2023-06-22', '16:30:00', 9, 'none', 1, 1, -4, -2, ''),
('2023-07-06', '16:30:00', 9, 'none', 1, 1, 3, 2, ''),
('2023-07-11', '16:30:00', 9, 'none', 1, 1, 7, 2, ''),
('2023-07-13', '16:30:00', 9, 'none', 1, 1, -3, 3, ''),
('2023-07-18', '16:30:00', 9, 'none', 1, 1, 1, 6, ''),
('2023-07-20', '16:30:00', 9, 'none', 1, 1, 3, 1, ''),
('2023-07-25', '16:30:00', 9, 'none', 1, 1, 4, 2, ''),
('2023-07-27', '16:30:00', 9, 'none', 1, 1, 1, 0, ''),
('2023-08-01', '16:30:00', 9, 'none', 1, 1, 8, 4, ''),
('2023-08-10', '16:30:00', 9, 'none', 1, 1, -2, 2, ''),
('2023-08-15', '16:30:00', 9, 'none', 1, 1, 2, 4, ''),
('2023-08-17', '16:30:00', 9, 'none', 1, 1, -4, -1, ''),
('2023-08-22', '16:30:00', 9, 'none', 1, 1, 2, -3, ''),
('2023-08-24', '16:30:00', 9, 'none', 1, 1, 0, 0, ''),
('2023-08-29', '16:30:00', 9, 'none', 1, 1, 3, -3, ''),
('2023-08-31', '16:30:00', 9, 'none', 1, 1, 2, 2, ''),
('2023-09-05', '16:30:00', 9, 'none', 1, 1, -1, 0, ''),
('2023-09-07', '16:30:00', 9, 'none', 1, 1, -1, 3, ''),
('2023-09-12', '16:30:00', 9, 'none', 1, 1, 1, -2, ''),
('2023-09-14', '16:30:00', 9, 'none', 1, 1, 0, 6, ''),
('2023-09-19', '16:30:00', 9, 'none', 1, 1, 0, 0, ''),
('2024-03-12', '16:21:00', 9, 'none', 1, 1, 5, 2, ''),
('2024-03-14', '16:21:00', 9, 'none', 1, 1, 0, 8, ''),
('2024-03-19', '16:21:00', 9, 'none', 1, 1, 1, 7, ''),
('2024-03-21', '16:21:00', 9, 'none', 1, 1, 9, 5, ''),
('2024-03-26', '16:21:00', 9, 'none', 1, 1, 2, 0, ''),
('2024-03-28', '16:21:00', 9, 'none', 0, 1, 1, -2, ''),
('2024-04-02', '16:21:00', 9, 'back9', 1, 1, 7, 6, ''),
('2024-04-04', '16:21:00', 9, 'none', 1, 1, 0, 0, ''),
('2024-04-11', '16:21:00', 9, 'none', 1, 1, -3, -3, ''),
('2024-04-16', '16:21:00', 9, 'none', 1, 1, 4, 8, ''),
('2024-04-18', '16:21:00', 9, 'none', 1, 1, 4, 6, ''),
('2024-04-23', '16:21:00', 9, 'none', 1, 1, 6, 4, ''),
('2024-04-25', '16:21:00', 9, 'none', 1, 1, 8, 7, ''),
('2024-04-30', '16:21:00', 9, 'none', 1, 1, 8, 5, ''),
('2024-05-02', '16:21:00', 9, 'none', 1, 1, 9, -4, ''),
('2024-05-07', '16:21:00', 9, 'none', 1, 1, 5, 1, ''),
('2024-05-14', '16:21:00', 9, 'none', 1, 1, 4, -3, ''),
('2024-05-16', '16:21:00', 9, 'none', 1, 1, 1, -2, ''),
('2024-05-21', '16:21:00', 9, 'none', 1, 1, 2, 11, ''),
('2024-05-23', '16:21:00', 9, 'none', 1, 1, 7, 3, ''),
('2024-05-30', '16:21:00', 9, 'none', 1, 1, 3, 0, ''),
('2024-06-04', '16:21:00', 9, 'none', 1, 1, 5, 3, ''),
('2024-06-06', '16:21:00', 9, 'none', 1, 1, -1, 1, ''),
('2024-06-11', '16:21:00', 9, 'none', 1, 1, 2, 10, ''),
('2024-06-13', '16:21:00', 9, 'none', 1, 1, 4, 6, ''),
('2024-06-18', '16:21:00', 9, 'none', 1, 1, 5, 1, ''),
('2024-06-20', '16:21:00', 9, 'none', 1, 1, 4, 8, ''),
('2024-07-02', '16:21:00', 9, 'none', 1, 1, 6, 9, ''),
('2024-07-09', '16:21:00', 9, 'none', 1, 1, -2, 8, ''),
('2024-07-11', '16:21:00', 9, 'none', 1, 1, 2, 7, ''),
('2024-07-16', '16:21:00', 9, 'back9', 1, 1, 0, 1, ''),
('2024-07-18', '16:21:00', 9, 'none', 1, 1, -3, 4, ''),
('2024-07-23', '16:21:00', 9, 'none', 1, 1, 3, -2, ''),
('2024-07-25', '16:21:00', 9, 'none', 1, 1, 1, -1, ''),
('2024-07-30', '16:21:00', 9, 'none', 1, 1, 1, 6, ''),
('2024-08-06', '16:21:00', 9, 'none', 1, 1, 3, 3, ''),
('2024-08-13', '16:21:00', 9, 'none', 1, 1, 2, 5, ''),
('2024-08-15', '16:21:00', 9, 'none', 1, 1, 2, -2, ''),
('2024-08-20', '16:21:00', 9, 'none', 1, 1, -6, -1, ''),
('2024-08-22', '16:21:00', 9, 'back9', 1, 1, -1, 2, ''),
('2024-08-27', '16:21:00', 9, 'none', 1, 1, 3, 7, ''),
('2024-08-29', '16:21:00', 9, 'none', 1, 1, 0, 2, ''),
('2024-09-03', '16:21:00', 9, 'none', 1, 1, 0, 5, ''),
('2024-09-05', '16:21:00', 9, 'none', 1, 1, -1, -1, ''),
('2024-09-10', '16:21:00', 9, 'none', 1, 1, 0, 2, ''),
('2024-09-12', '16:21:00', 9, 'playoff', 1, 1, 4, 6, ''),
('2025-03-11', '16:21:00', 9, 'none', 1, 1, 2, 10, ''),
('2025-03-13', '16:21:00', 9, 'none', 1, 1, 1, 4, ''),
('2025-03-18', '16:21:00', 9, 'none', 1, 1, -4, 2, ''),
('2025-03-20', '16:21:00', 9, 'none', 1, 1, 1, -4, ''),
('2025-03-25', '16:21:00', 9, 'none', 1, 1, 6, -2, ''),
('2025-03-27', '16:21:00', 9, 'none', 1, 1, 5, 6, ''),
('2025-04-01', '16:21:00', 9, 'none', 1, 1, 1, 2, ''),
('2025-04-03', '16:21:00', 9, 'none', 1, 1, 3, 1, ''),
('2025-04-08', '16:21:00', 9, 'none', 1, 1, 1, 0, ''),
('2025-04-10', '16:21:00', 9, 'none', 0, 1, 3, 1, ''),
('2025-04-15', '16:21:00', 9, 'none', 1, 1, -1, 6, ''),
('2025-04-17', '16:21:00', 9, 'none', 1, 1, 4, 5, ''),
('2025-04-22', '16:21:00', 9, 'none', 1, 1, 4, 4, ''),
('2025-04-29', '16:21:00', 9, 'none', 1, 1, 3, 2, ''),
('2025-05-01', '16:21:00', 9, 'none', 1, 1, 4, 1, ''),
('2025-05-06', '16:21:00', 9, 'none', 1, 1, 3, 4, ''),
('2025-05-08', '16:21:00', 9, 'none', 1, 1, 3, 5, ''),
('2025-05-13', '16:21:00', 9, 'none', 1, 1, -2, 3, ''),
('2025-05-15', '16:21:00', 9, 'none', 1, 1, 2, -1, ''),
('2025-05-20', '16:21:00', 9, 'none', 1, 1, 9, 6, ''),
('2025-05-22', '16:21:00', 9, 'none', 1, 1, 3, -2, ''),
('2025-05-29', '16:21:00', 9, 'none', 1, 1, 5, 4, ''),
('2025-06-03', '16:21:00', 9, 'none', 1, 1, 7, 4, ''),
('2025-06-05', '16:21:00', 9, 'none', 1, 1, -4, -3, ''),
('2025-06-10', '16:21:00', 9, 'none', 0, 1, 3, 4, ''),
('2025-06-12', '16:21:00', 9, 'none', 1, 1, 0, 2, ''),
('2025-06-17', '16:21:00', 9, 'none', 0, 0, 0, 0, ''),
('2025-06-19', '16:21:00', 9, 'none', 0, 0, 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table GolfPlayers
--

CREATE TABLE IF NOT EXISTS GolfPlayers (
  playerId TEXT NOT NULL,
  fname TEXT NOT NULL,
  lname TEXT NOT NULL,
  affiliation TEXT NOT NULL,
  active INTEGER NOT NULL,
  paid INTEGER NOT NULL,
  role TEXT NOT NULL DEFAULT 'player',
  teamPurple INTEGER NOT NULL,
  target INTEGER NOT NULL DEFAULT '1',
  countingRounds INTEGER NOT NULL DEFAULT '0',
  teeBox TEXT NOT NULL,
  admin INTEGER NOT NULL DEFAULT '0',
  email TEXT NOT NULL,
  startYear year(4) NOT NULL,
  authpwd TEXT NOT NULL,
  hpwd TEXT NOT NULL,
  rec INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  carrier TEXT NOT NULL,
  phone TEXT NOT NULL,
  lateRequest INTEGER NOT NULL
);

--
-- Dumping data for table GolfPlayers
--

INSERT INTO GolfPlayers (playerId, fname, lname, affiliation, active, paid, role, teamPurple, target, countingRounds, teeBox, admin, email, startYear, authpwd, hpwd, rec, carrier, phone, lateRequest) VALUES
('ja76', 'Jason', 'Adkins', 'Theater', 1, 0, 'player', 1, 4, 0, 'W', 0, 'jason.adkins@furman.edu', 2021, '', 'NiXm7kX3kO.22', 1, '', '', 2),
('ja26', 'Jonathan', 'Allen', 'Golf shop', 1, 0, 'golfshop', 1, 14, 0, 'W', 0, 'Jonathan.allen2626@furman.edu', 2020, '', 'NijgjaejEgOG.', 3, '', '', 0),
('jb86', 'John', 'Barker', 'Ret. Malone Ctr', 1, 1, 'player', 1, 9, 0, 'G', 0, 'john.barker@retiree.furman.edu', 2020, '', 'NiSQ1jdiLHVx.', 4, '', '', 0),
('mb53', 'Mark', 'Britt', 'Music', 0, 0, 'player', 1, 5, 0, 'W', 0, 'mark.britt@furman.edu', 2020, '', 'NiLHufF8wURf2', 5, '', '', 0),
('jb90', 'John', 'Burns', 'Ret. Athletics', 1, 1, 'player', 1, 8, 6, 'G', 0, 'burns2648@gmail.com', 2000, '', 'Ni8l2NQ9m4Dvc', 6, '', '', 10),
('cc63', 'Connie', 'Carson', 'Student Affairs', 1, 1, 'player', 1, 8, 6, 'L', 0, 'connie.carson@furman.edu', 2000, '', 'Nidena34Gc1Q2', 7, '', '', 6),
('jc13', 'Jason', 'Cassidy', 'Student Affairs', 1, 1, 'player', 1, 6, 6, 'W', 0, 'Jason.Cassidy@furman.edu', 2010, '', 'Ni.ybG.N6C20w', 8, '', '', 2),
('bc25', 'Bryan', 'Catron', 'Ret. Computer Sci', 1, 1, 'player', 1, 12, 6, 'G', 1, 'bcatron2000@gmail.com', 2010, '', 'NiUgxQzRiyr8E', 9, '', '', 2),
('bc11', 'Bob', 'Chance', 'Ret. Art', 1, 1, 'player', 1, 13, 6, 'G', 0, 'bob.chance@furman.edu', 2010, '', 'NimG5QF7EQ.Dk', 10, '', '', 4),
('ed11', 'Elizabeth', 'Davis', 'President', 1, 0, 'player', 1, 1, 0, 'L', 0, 'elizabeth.davis@furman.edu', 2017, '', 'NiCDTGkdsnZgM', 11, '', '', 0),
('te15', 'Tim', 'Eckstein', 'Golf Shop', 1, 0, 'golfshop', 1, 13, 0, 'W', 0, 'tim.eckstein@furman.edu', 2017, '', 'Ni8WSwHj8jKn.', 12, '', '', 0),
('jf10', 'Jeremy', 'Fleming', 'Photographer', 0, 0, 'player', 1, 8, 0, 'W', 0, 'Jeremy.Fleming@furman.edu', 2010, '', 'Ni/8PkLGXr.qw', 13, '', '', 0),
('sh45', 'Shon', 'Herrick', 'Development', 1, 1, 'player', 1, 8, 5, 'W', 0, 'shon.herrick@furman.edu', 2010, '', 'Nio7KhXzggoNQ', 14, '', '', 4),
('jh11', 'Justin', 'Hughes', 'I.T.', 1, 1, 'player', 1, 5, 6, 'W', 0, 'justin.hughes@furman.edu', 2010, '', 'NiLhv6qV5uXGs', 15, '', '', 11),
('dk77', 'Donald', 'Kaade', 'Admin', 1, 0, 'player', 1, 2, 0, 'W', 0, 'don.kaade@furman.edu', 0000, '', 'NiQ5x/JJj4TYI', 16, '', '', 0),
('kk29', 'Kailash', 'Khandke', 'Economics', 1, 1, 'player', 1, 11, 5, 'G', 0, 'Kailash.Khandke@furman.edu', 2010, '', 'NiN9IwEeuUXzQ', 18, '', '', 3),
('jo88', 'James', 'Odom', '', 0, 0, 'player', 1, 6, 0, 'G', 0, 'jaspamodom@charter.net', 2000, '', 'NiTfII6k50GBc', 19, '', '', 0),
('pp34', 'Pat', 'Pecoy', 'Ret. Modern Lang', 1, 0, 'player', 1, 1, 0, 'L', 0, 'pat.pecoy@furman.edu', 2010, '', 'NibkkhX.teU02', 20, '', '', 0),
('kp15', 'Ken', 'Pettus', 'Ret. Athletics', 1, 1, 'player', 1, 15, 2, 'G', 0, 'Ken.Pettus@retiree.furman.edu', 2010, '', 'NisDRib34E7yE', 21, '', '', 0),
('ls50', 'Liz', 'Seman', 'Admin', 1, 1, 'player', 1, 2, 6, 'L', 0, 'liz.seman@furman.edu', 2010, '', 'Nincu1tX3h/cA', 22, '', '', 3),
('hs41', 'Harry', 'Shucker', 'Ret. Student Life', 1, 0, 'player', 1, 1, 0, 'G', 0, 'harry.shucker@furman.edu', 2010, '', 'NiDPc/zMx6//E', 23, '', '', 0),
('bs57', 'Ben', 'Snyder', 'H.E.S.', 1, 0, 'player', 1, 6, 0, 'W', 0, 'ben.snyder@furman.edu', 2015, '', 'NiFY4a6gC4//c', 24, '', '', 0),
('ts39', 'Tim', 'Sorrels', 'Ret. Athletics', 1, 0, 'player', 1, 12, 0, 'W', 0, 'tim.sorrells@furman.edu', 2015, '', 'NiSTASvHf2Evg', 25, '', '', 0),
('ms95', 'Mickie', 'Spencer', 'Theater', 1, 0, 'player', 1, 8, 0, 'L', 0, 'Mickie.Spencer@furman.edu', 2015, '', 'Nib.Avoc35rPM', 26, '', '', 0),
('es23', 'Emily', 'Sweezey', 'Music', 1, 1, 'player', 1, 3, 6, 'L', 0, 'emily.sweezey@furman.edu', 2015, '', 'NiTe8679KaIFU', 27, '', '', 6),
('bu48', 'Bob', 'Underwood', 'Business', 1, 1, 'player', 1, 10, 4, 'G', 0, 'robert.underwood@furman.edu', 2015, '', 'NivbiTFKyrlCM', 29, '', '', 2),
('jb14', 'Janis', 'Bandelin', 'Ret. Library', 0, 0, 'player', 0, 1, 0, 'L', 0, 'jbandelin@gmail.com ', 2015, '', 'NiQtoqzNjGvdM', 31, '', '', 0),
('de60', 'David', 'Enter', 'Ret. Police', 1, 0, 'player', 0, 5, 0, 'G', 0, 'denter60@gmail.com', 2015, '', 'NiZ9.WGrcpoIk', 32, '', '', 0),
('pg25', 'Paula', 'Gabbert', 'Ret. Computer Sci', 1, 1, 'player', 0, 6, 6, 'L', 1, 'paula.gabbert@furman.edu', 2015, '', 'Ni4v3ypVqhJrg', 33, '', '', 1),
('mg66', 'Mike', 'Gifford', 'I.T.', 1, 1, 'player', 0, 5, 0, 'W', 0, 'mike.gifford@furman.edu', 2015, '', 'NiBScqBNNghw.', 34, '', '', 2),
('bg16', 'Brian', 'Goess', 'Chemistry', 1, 1, 'player', 0, 4, 6, 'B', 1, 'brian.goess@furman.edu', 2015, '', 'NikNGlQHkZDRs', 35, '', '', 0),
('lh59', 'Les', 'Hicken', 'Ret. Music', 1, 1, 'player', 0, 9, 6, 'G', 0, 'les.hicken@furman.edu', 2015, '', 'Nincu1tX3h/cA', 37, '', '', 3),
('gl80', 'George', 'Lipscomb', 'Education', 1, 1, 'player', 0, 6, 6, 'W', 0, 'George.Lipscomb@furman.edu', 2015, '', 'Nizc/O0TaSJIc', 41, '', '', 0),
('sl90', 'Steve', 'Long', 'Facilities', 1, 1, 'player', 0, 6, 6, 'G', 1, 'steve.long@furman.edu', 2015, '', 'NitAFUS.PjbPM', 42, '', '', 0),
('mm85', 'Michael', 'May', 'Art', 1, 1, 'player', 0, 3, 3, 'W', 0, 'michael.may@furman.edu', 2015, '', 'NiDY4zytPHcSg', 44, '', '', 1),
('hm24', 'Heidi', 'McCrory', 'Development', 1, 1, 'player', 0, 5, 6, 'L', 0, 'hhmccrory@gmail.com', 2015, '', 'NiLIa4ZLfw69.', 45, '', '', 1),
('mm60', 'Marion', 'McHugh', '', 0, 0, 'player', 0, 1, 0, 'W', 0, 'marion.mchugh@furman.edu', 2015, '', 'Nic4gqc.eqCj6', 47, '', '', 0),
('jr44', 'Jason', 'Rawlings', 'Biology', 1, 1, 'player', 0, 6, 6, 'W', 1, 'jason.rawlings@furman.edu', 2015, '', 'NiMcCZJxcGQ0.', 49, '', '', 7),
('jr88', 'Jeff', 'Redderson', 'Facilities', 1, 1, 'player', 0, 10, 6, 'W', 0, 'Jeff.Redderson@furman.edu', 2015, '', 'NiGCEtw2Ky5u6', 50, '', '', 2),
('ds33', 'Debbie', 'Stegall', 'Ret. Bookstore', 1, 0, 'player', 0, 5, 0, 'L', 0, 'Debsnana@gmail.com', 2015, '', 'Nin1zNFWgz94U', 52, '', '', 0),
('rt66', 'Ron', 'Thompson', 'Housing', 1, 1, 'player', 0, 4, 6, 'W', 0, 'ron.thompson@furman.edu ', 2015, '', 'Nib8DhEt4TITU', 53, '', '', 6),
('bv66', 'Bing', 'Vick', 'Ret. Music', 1, 1, 'player', 0, 13, 6, 'G', 0, 'bing.vick@furman.edu', 2015, '', 'NilhtxlKz8EVQ', 55, '', '', 2),
('ww77', 'Wade', 'Worthen', 'Biology', 1, 1, 'player', 0, 7, 6, 'W', 0, 'Wade.Worthen@furman.edu', 2015, '', 'NiofwdftEi9zc', 56, '', '', 5),
('md20', 'Matt', 'Davidson', 'M Golf Coach', 0, 0, 'coach', 0, 19, 0, 'B', 0, 'matthew.davidson@furman.edu', 2010, '', 'NiNsVNwMyS8NA', 59, '', '', 0),
('tf55', 'Tim', 'Fehler', 'History', 1, 1, 'player', 1, 7, 4, 'W', 1, 'tim.fehler@furman.edu', 2010, '', 'NiHzAWSUeTjDs', 61, '', '', 4),
('gs39', 'Greg', 'Springsteen', 'Chemistry', 1, 1, 'player', 1, 1, 1, 'W', 0, 'greg.springsteen@furman.edu', 2015, '', 'NiQ1oxLuUQsC2', 64, '', '', 0),
('jd60', 'Jason', 'Donnelly', 'Athletics', 1, 0, 'player', 1, 0, 0, 'W', 0, 'Jason.donnelly@furman.edu', 2023, '', 'Nicr/f..uADpo', 65, '', '', 0),
('mr12', 'Mackenzie', 'Raim', '', 0, 0, 'coach', 1, 12, 0, 'W', 0, 'mackenzie.raim@furman.edu', 2010, '', 'NiN3D.J4jvrx6', 67, '', '', 0),
('jh15', 'Jeff', 'Hull', 'W. Golf Coach', 0, 0, 'coach', 0, 15, 0, 'W', 0, 'jeff.hull@furman.edu', 2010, '', '', 68, '', '', 0),
('cs87', 'Cherington', 'Shucker', 'Development', 1, 0, 'player', 0, 1, 0, 'L', 0, 'cherington.shucker@furman.edu', 2023, '', 'NiceNavl8ayb2', 69, '', '', 0),
('xx777', 'Roger', 'Baney', '', 0, 0, 'golfshop', 1, 0, 0, 'W', 0, 'roger.baney@furman.edu', 2022, '', 'NiDMBt0TZLLzc', 72, '', '', 0),
('at88', 'Andrea', 'Tartaro', 'Computer Sci', 1, 0, 'player', 1, 1, 0, 'L', 0, 'andrea.tartaro@furman.edu', 2022, '', 'NikhmyX/kK2GY', 73, '', '', 0),
('vc22', 'Vaughn', 'Crowetipton', 'Chaplain', 1, 1, 'player', 1, 2, 3, 'W', 0, 'vaughn.crowetipton@furman.edu', 2022, '', 'NiZY9MHupNEAE', 74, '', '', 3),
('zp23', 'Zach', 'Pace', 'Communications', 0, 0, 'player', 0, 0, 0, '', 0, 'zach.pace@furman.edu', 2023, '', 'NiW9HVe/FROBg', 75, '', '', 0),
('am44', 'Alex', 'Marinelli', 'Athletics', 0, 0, 'player', 0, 6, 0, 'W', 0, 'Alex.marinelli5@furman.edu', 2023, '', 'Nid/1ZgBKAa8M', 77, '', '', 0),
('mg23', 'Mac', 'Gilliland', 'Chemistry', 1, 1, 'player', 0, 9, 6, 'W', 0, 'mac.gilliland@furman.edu', 2023, '', 'NiyjnYKMloEHQ', 78, '', '', 4),
('ts67', 'Trent', 'Stubbs', 'Chemistry', 1, 1, 'player', 1, 1, 1, 'W', 0, 'trent.stubbs5@furman.edu', 2023, '', 'NiIuNzX8EhbPg', 79, '', '', 0),
('lh12', 'Lane', 'Harris', '', 0, 0, 'player', 1, 0, 0, 'W', 0, 'lane.harris@furman.edu', 2023, '', 'NivF1u.XhUS2U', 80, '', '', 0),
('xx89', 'Brandon', 'Mathis', '', 0, 0, 'golfshop', 1, 0, 0, 'W', 0, 'Brandon.mathis@furman.edu', 2020, '', 'NiDMBt0TZLLzc', 81, '', '', 0),
('jk15', 'Jordan', 'King', 'Student Life', 1, 1, 'player', 0, 3, 6, 'W', 0, 'jordan.king15@furman.edu', 2023, '', 'NiUm/TuBBOy2g', 84, '', '', 7),
('kh50', 'Kelsey', 'Hample', 'Economics', 1, 0, 'player', 1, 3, 0, 'L', 0, 'kelsey.hample@furman.edu', 2023, '', 'Ni8ntS3vQV532', 85, '', '', 0),
('se20', 'Sue', 'Eckstein', 'Athletics', 1, 1, 'player', 0, 8, 2, 'L', 0, 'sue.eckstein@furman.edu', 2023, '', 'Nio8ULiBN5qdo', 86, '', '', 1),
('ec80', 'Erik', 'Ching', 'History', 1, 1, 'player', 1, 6, 6, 'W', 0, 'erik.ching@furman.edu', 2024, '', 'NiFUqWP4Cn.To', 87, '', '', 5),
('tj80', 'Todd', 'Janssen', 'I.T.', 1, 1, 'player', 0, 4, 6, 'W', 0, 'todd.janssen@furman.edu', 2024, '', 'NiWgg/6KVdHIw', 88, '', '', 4),
('ru45', 'Randy', 'Umstead', 'Music', 1, 1, 'player', 1, 2, 6, 'W', 0, 'Randall.umstead@furman.edu', 2024, '', 'Niby3I1SAQreI', 89, '', '', 6),
('sl45', 'Scott', 'Legge', 'Anthropology', 1, 1, 'player', 1, 10, 6, 'W', 0, 'Scott.legge@furman.edu', 2024, '', 'NiGDzjFNBkKz2', 90, '', '', 1),
('tm45', 'Tafon', 'Mainsah', 'Athletics', 1, 1, 'player', 1, 9, 6, 'W', 0, 'tafon.mainsah@furman.edu', 2024, '', 'Nit5Aa0uxO3eI', 92, '', '', 4),
('sm45', 'Seth', 'Mcbrayer', 'Athletics', 1, 1, 'player', 0, 8, 6, 'W', 0, 'smcbrayer@furmanas.com', 2024, '', 'Niit2Aef5WVUU', 94, '', '', 1),
('aj45', 'Austin', 'Johnk', 'Development', 1, 0, 'player', 0, 8, 0, 'W', 0, 'Austin.johnk@furman.edu', 2024, '', 'NiUNxnd8.aUkw', 95, '', '', 4),
('rc45', 'Robert', 'Colas', 'Development', 1, 1, 'player', 0, 13, 6, 'W', 0, 'Robert.colas@furman.edu', 2024, '', 'NiVB89OPQbs8w', 96, '', '', 17),
('jp45', 'John', 'Pezdek', 'Development', 1, 1, 'player', 1, 16, 6, 'W', 0, 'John.pezdek@furman.edu', 2024, '', 'NiMXoPpvhg5/w', 97, '', '', 1),
('jc45', 'Jordan', 'Cox', 'Student Life', 1, 1, 'player', 1, 5, 6, 'W', 0, 'Jordan.cox12@furman.edu', 2024, '', 'NioYNDd6mURAs', 98, '', '', 2),
('mp45', 'Max', 'Potter', 'Athletics', 1, 1, 'player', 0, 8, 6, 'W', 0, 'max.potter7@furman.edu', 2024, '', 'Nir0pOkl3QNLI', 99, '', '', 13),
('af588', 'Alex', 'Fagan', 'OLLI', 1, 1, 'player', 0, 3, 6, 'W', 0, 'Alex.fagan@furman.edu', 2024, '', 'NiRP/xvt8bSHk', 106, '', '', 0),
('sm844', 'Stephen', 'Mandravelis', 'Art', 1, 1, 'player', 0, 5, 4, 'W', 0, 'stephen.mandravelis@furman.edu', 2024, '', 'NiDvQtYWYRowE', 108, '', '', 0),
('cw867', 'Claudia', 'Winkler', 'Riley Institute', 1, 1, 'player', 0, 8, 6, 'L', 0, 'claudia.winkler@furman.edu', 2024, '', 'NiW1mZ9VXLj8s', 109, '', '', 5),
('hf695', 'Houghton', 'Flanagan', 'Ticketing', 1, 1, 'player', 1, 9, 6, 'W', 0, 'houghton.flanagan@furman.edu', 2024, '', 'NiAlYZOtArzvQ', 110, '', '', 4),
('tr886', 'Tyler', 'Rosenberger', 'Athletics', 1, 1, 'player', 1, 5, 5, 'W', 0, 'tyler.rosenberger@furman.edu', 2025, '', 'Ni6s/eiy/BU4Q', 111, '', '', 1),
('dm15', 'David', 'Manning', 'Grounds', 1, 1, 'player', 1, 0, 0, 'W', 0, 'david.manning@furman.edu', 2025, '', 'NiBNyiJJpQHVM', 112, '', '', 0),
('dw445', 'David', 'Watt', '', 1, 1, 'player', 1, 0, 0, 'G', 0, 'David.watt@furman.edu', 2025, '', 'NirckLSdxFToA', 113, '', '', 0),
('te362', 'Tyler', 'Eckstein', 'Athletics', 1, 1, 'player', 1, 10, 4, 'W', 0, 'Tyler.eckstein4@furman.edu', 2025, '', 'NiyWYXxbLSR2s', 114, '', '', 3),
('em682', 'Erin', 'Mayes', '', 1, 1, 'player', 1, 0, 0, 'L', 0, 'Erin.mayes@furman.edu', 2025, '', 'Niofctzv50u5E', 115, '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table GolfRounds
--

CREATE TABLE IF NOT EXISTS GolfRounds (
  playerId TEXT NOT NULL,
  playDate TEXT NOT NULL,
  score INTEGER NOT NULL,
  points INTEGER NOT NULL,
  playToTarget INTEGER NOT NULL,
  specialDay INTEGER NOT NULL DEFAULT '0',
  rec INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

--
-- Dumping data for table GolfRounds
--

--
-- Table structure for table GolfSchedule
--

CREATE TABLE IF NOT EXISTS GolfSchedule (
  playerId TEXT NOT NULL,
  date date NOT NULL,
  preferredTime TEXT NOT NULL DEFAULT 'any',
  other TEXT NOT NULL,
  teeTime INTEGER NOT NULL DEFAULT '0',
  rec INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  signedUp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--
-- Dumping data for table GolfSchedule
--

INSERT INTO GolfSchedule (playerId, date, preferredTime, other, teeTime, rec, signedUp) VALUES
('bc25', '2025-06-17', 'C', '', 0, 625, '2025-06-13 21:05:19'),
('bc25', '2025-06-19', 'C', '', 0, 626, '2025-06-13 21:05:33'),
('bc11', '2025-06-19', 'B', '', 0, 628, '2025-06-13 21:44:42'),
('bg16', '2025-06-17', 'C', '', 0, 629, '2025-06-14 13:03:28'),
('bg16', '2025-06-19', 'C', '', 0, 630, '2025-06-14 13:03:37'),
('gl80', '2025-06-17', 'C', '', 0, 631, '2025-06-14 13:31:06'),
('ww77', '2025-06-17', 'C', '', 0, 632, '2025-06-15 16:31:49'),
('ww77', '2025-06-19', 'C', '', 0, 633, '2025-06-15 16:32:05'),
('rt66', '2025-06-17', 'E', '', 0, 634, '2025-06-15 21:48:02'),
('rt66', '2025-06-19', 'E', '', 0, 635, '2025-06-15 21:48:13'),
('jc13', '2025-06-17', 'E', '', 0, 636, '2025-06-16 01:36:57'),
('rc45', '2025-06-17', 'B', '', 0, 637, '2025-06-16 02:50:17'),
('bc11', '2025-06-17', 'C', '', 0, 638, '2025-06-16 09:04:03'),
('jr88', '2025-06-17', 'C', '', 0, 639, '2025-06-16 11:55:51'),
('jr88', '2025-06-19', 'D', '', 0, 640, '2025-06-16 11:56:17'),
('jp45', '2025-06-17', 'B', 'Anytime after 4:30 would work this week', 0, 641, '2025-06-16 12:21:26'),
('hf695', '2025-06-17', 'D', '', 0, 642, '2025-06-16 12:50:59'),
('jh11', '2025-06-17', 'D', '', 0, 643, '2025-06-16 13:08:40'),
('jh11', '2025-06-19', 'D', '', 0, 644, '2025-06-16 13:08:48'),
('sm45', '2025-06-17', 'D', '', 0, 645, '2025-06-16 13:46:48'),
('jk15', '2025-06-17', 'B', '', 0, 646, '2025-06-16 13:58:56');

-- --------------------------------------------------------

--
-- Table structure for table healthSafety
--

CREATE TABLE IF NOT EXISTS healthSafety (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  shortName TEXT DEFAULT NULL,
  content TEXT NOT NULL,
  type TEXT NOT NULL,
  icon TEXT NOT NULL,
  priority INTEGER NOT NULL DEFAULT '1'
);

--
-- Dumping data for table healthSafety
--

INSERT INTO healthSafety (id, name, shortName, content, type, icon, priority) VALUES
(1, 'Furman Police', NULL, '8642942111', 'phone', 'shield', 5),
(3, 'SafeRide', NULL, '8647720007', 'phone', 'car', 1),
(4, 'Health Verification Survey', NULL, 'https://furman.az1.qualtrics.com/jfe/form/SV_3mizqdKgD6QLujr', 'link', 'bandage.fill', 1),
(6, 'Parking Zone Maps', 'Park', 'https://www.furman.edu/university-police/wp-content/uploads/sites/25/2020/08/PUB20-21-Parking-Map-073120.pdf', 'link', 'car', 1),
(7, 'Earle Student Health Center', NULL, '8645222000', 'phone', 'bandage.fill', 3),
(8, 'Counseling Center', NULL, '8642943031', 'phone', 'person.circle', 3),
(9, 'The Greenville CrisisLine', NULL, '8642718888', 'phone', 'heart.circle', 3),
(10, 'Furman Focused Link', NULL, 'https://www.furman.edu/furman-focused/', 'link', 'staroflife', 1),
(14, 'South Carolina COVID-19 Testing Sites', NULL, 'https://scdhec.gov/covid19/find-covid-19-testing-location', 'link', 'heart.circle', 1),
(15, 'Sexual Misconduct Assistance', NULL, 'https://www.furman.edu/title-ix/sexual-misconduct-policy/', 'link', 'heart.circle', 3),
(16, 'Report a Bias Incident', NULL, 'https://cm.maxient.com/reportingform.php?FurmanUniv&layout_id=3', 'link', 'person.circle', 3),
(17, 'Parking Email', NULL, 'parking@furman.edu', 'email', '', 1),
(18, 'Parking Accessibility Map', NULL, 'https://www.furman.edu/american-disability-act/wp-content/uploads/sites/74/2019/05/ACCESSIBLE_PARKING-June-01-2017.pdf', 'link', '', 1),
(19, 'Furman Police Website', NULL, 'https://www.furman.edu/university-police/', 'link', '', 1),
(20, 'Student Handbook', NULL, 'https://www.furman.edu/student-life/student-handbook/', 'link', '', 1),
(21, 'Parking Citation Appeal', NULL, 'https://www.permitsales.net/FurmanUniv/violations', 'link', '', 1),
(22, 'Parking Regulations', NULL, 'https://www.furman.edu/university-police/wp-content/uploads/sites/25/2023/10/FU-Parking-Regs-updated-2023-3.pdf', 'link', '', 1),
(23, 'Suicide Prevention Hotline', NULL, '988', 'phone', '', 5);

--
-- Triggers healthSafety
--
-- BEFORE UPDATE: Update updateTimes
CREATE TRIGGER hs_on_update
BEFORE UPDATE ON healthSafety
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'healthSafety';
END;

-- AFTER DELETE: Update updateTimes
CREATE TRIGGER hs_ondelete
AFTER DELETE ON healthSafety
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'healthSafety';
END;

-- AFTER INSERT: Update updateTimes
CREATE TRIGGER hs_oninsert
AFTER INSERT ON healthSafety
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'healthSafety';
END;

-- --------------------------------------------------------

--
-- Table structure for table importantDates
--

CREATE TABLE IF NOT EXISTS importantDates (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT DEFAULT NULL,
  date date NOT NULL,
  startTime time NOT NULL,
  endTime time NOT NULL,
  category TEXT DEFAULT NULL,
  description TEXT,
  term TEXT,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Triggers importantDates
--
-- AFTER DELETE: Insert into updateTimes
CREATE TRIGGER importantDates_afterDelete
AFTER DELETE ON importantDates
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('importantDates');
END;

-- AFTER UPDATE: Insert into updateTimes
CREATE TRIGGER importantDates_afterUpdate
AFTER UPDATE ON importantDates
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('importantDates');
END;

-- BEFORE DELETE: Delete from updateTimes
CREATE TRIGGER importantDates_beforeDelete
BEFORE DELETE ON importantDates
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'importantDates';
END;

-- BEFORE UPDATE: Delete from updateTimes
CREATE TRIGGER importantDates_beforeUpdate
BEFORE UPDATE ON importantDates
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'importantDates';
END;

-- BEFORE INSERT: Delete from updateTimes
CREATE TRIGGER importantDates_deleteUpdateTimes
BEFORE INSERT ON importantDates
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'importantDates';
END;

-- AFTER INSERT: Insert into updateTimes
CREATE TRIGGER importantDates_inserted
AFTER INSERT ON importantDates
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('importantDates');
END;

-- --------------------------------------------------------

--
-- Table structure for table importantLinks
--

CREATE TABLE IF NOT EXISTS importantLinks (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  priority INTEGER NOT NULL DEFAULT '1',
  name TEXT NOT NULL,
  content TEXT NOT NULL,
  type TEXT CHECK('link' IN ('link','email','phone','')) NOT NULL
);

--
-- Dumping data for table importantLinks
--

INSERT INTO importantLinks (id, priority, name, content, type) VALUES
(65, 3, 'MyFurman', 'https://my.furman.edu', 'link'),
(66, 5, 'Moodle', 'https://courses.furman.edu/login/index.php', 'link'),
(67, 1, 'Academic Calendar', 'https://www.furman.edu/academics/university-calendar/', 'link'),
(68, 1, 'Box', 'http://furman.app.box.com/', 'link'),
(69, 1, 'Campus Map', 'https://campusmap.furman.edu/', 'link'),
(70, 1, 'CLP Calendar', 'https://www.furman.edu/academics/cultural-life-program/upcoming-clp-events/', 'link'),
(71, 1, 'FUPass / Password Station', 'https://fupass.furman.edu/AIMS/PS/Default.aspx', 'link'),
(72, 1, 'Libraries', 'https://libguides.furman.edu/library/home', 'link'),
(73, 1, 'Hours of Operations', 'https://blogs.furman.edu/myfurman/hours-of-operations/', 'link'),
(74, 1, '25Live Room Reservations', 'https://25live.collegenet.com/pro/furman', 'link'),
(75, 1, 'Instructor Evaluations', 'https://furman.smartevals.com/', 'link'),
(76, 1, 'syncDIN', 'https://furman.campuslabs.com/engage/', 'link'),
(77, 1, 'Starfish', 'https://furman.starfishsolutions.com/starfish-ops', 'link'),
(78, 3, 'Housing Portal', 'https://furman.datacenter.adirondacksolutions.com/furman_thdss_prod/index.html', 'link'),
(79, 1, 'IT Services', 'https://www.furman.edu/offices-services/information-technology-services/', 'link'),
(80, 5, 'Workday', 'https://wd5.myworkday.com/furman', 'link'),
(81, 1, 'SOAR Student Portal', 'https://shasta.accessiblelearning.com/Furman/', 'link'),
(82, 1, 'SOAR Resources', 'https://www.furman.edu/accessibility/current-student-resources/', 'link'),
(83, 1, 'Writing & Media Lab', 'https://www.timetap.com/appts/QdkKiAl27Tq', 'link'),
(84, 1, 'Furman Engaged Schedule', 'https://virtual.oxfordabstracts.com/#/e/fe2024/program', 'link');

-- --------------------------------------------------------

--
-- Table structure for table newsContent
--

CREATE TABLE IF NOT EXISTS newsContent (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  description TEXT NOT NULL,
  media TEXT CHECK('link' IN ('link','video')) NOT NULL,
  linktocontent TEXT NOT NULL,
  publisherID INTEGER NOT NULL,
  section TEXT DEFAULT NULL,
  publishdate TEXT NOT NULL,
  imagelink TEXT DEFAULT NULL
);

--
--
-- Table structure for table newsPublishers
--

CREATE TABLE IF NOT EXISTS newsPublishers (
  publisherID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  link TEXT NOT NULL,
  image TEXT NOT NULL,
  studentRun INTEGER NOT NULL
);

--
-- Dumping data for table newsPublishers
--

INSERT INTO newsPublishers (publisherID, name, link, image, studentRun) VALUES
(1, 'The Paladin', 'https://thepaladin.news/', '', 1),
(2, 'FUNC', 'https://www.youtube.com/@func928/videos', '', 1),
(3, 'The Echo', 'https://scholarexchange.furman.edu/echo/', '', 1),
(4, 'Knightly News', 'https://www.youtube.com/@knightlynewsfurmanuniversi9188/videos', '', 1),
(5, 'Christo et Doctrinae', 'https://christoetdoctrinae.com', '', 1),
(6, 'Furman Humanities Review', 'https://scholarexchange.furman.edu/fhr/', '', 1),
(7, 'Furman in the News', 'https://www.furman.edu/news/', '', 0),
(8, 'President''s Page', 'https://www.furman.edu/about/president/', '', 0),
(9, 'Furman Magazine', 'https://www.furman.edu/news/furman-magazine/', '', 0),
(10, 'The Tocqueville Center', 'https://www.furman.edu/academics/tocqueville-program/', '', 0),
(11, 'The Riley Institute', 'https://www.furman.edu/riley/', '', 0),
(12, 'The Hill Institute', 'https://www.furman.edu/innovation-entrepreneurship/', '', 0),
(13, 'The Shi Institue', 'https://www.furman.edu/shi-institute/', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table parkingResources
--

CREATE TABLE IF NOT EXISTS parkingResources (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  type TEXT CHECK('link' IN ('link','phone')) NOT NULL,
  resource TEXT NOT NULL
);

--
-- Dumping data for table parkingResources
--

INSERT INTO parkingResources (id, name, type, resource) VALUES
(1, 'Parking Website', 'link', 'https://www.furman.edu/university-police/parking-citations/'),
(2, 'Buy a Permit', 'link', 'https://portal.permitsales.net/driverportal/FurmanUniv'),
(3, 'Manage Citations', 'link', 'https://portal.permitsales.net/driverportal/FurmanUniv/paycitation'),
(4, 'Request a Guest Pass', 'link', 'https://portal.permitsales.net/driverportal/FurmanUniv'),
(5, 'Parking Regulations Document', 'link', 'https://www.furman.edu/university-police/wp-content/uploads/sites/25/2024/08/Traffic-and-Parking-Regs.pdf');

-- --------------------------------------------------------

--
-- Table structure for table parkingZones
--

CREATE TABLE IF NOT EXISTS parkingZones (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  zoneName TEXT NOT NULL,
  boundry TEXT NOT NULL,
  yellow INTEGER NOT NULL DEFAULT '0',
  green INTEGER NOT NULL DEFAULT '0',
  blue INTEGER NOT NULL DEFAULT '0',
  silver INTEGER NOT NULL DEFAULT '0',
  orange INTEGER NOT NULL DEFAULT '0',
  purple INTEGER NOT NULL DEFAULT '0',
  lightPurple INTEGER NOT NULL DEFAULT '0',
  public_col INTEGER NOT NULL DEFAULT '0'
);


--
-- Table structure for table restaurantMenu
--

CREATE TABLE IF NOT EXISTS restaurantMenu (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  restaurant TEXT NOT NULL,
  item TEXT NOT NULL
);

--
-- Dumping data for table restaurantMenu
--

INSERT INTO restaurantMenu (id, restaurant, item) VALUES
(1, 'Bread and Bowl', 'Sandwiches'),
(4, 'Bread and Bowl', 'Pizza'),
(5, 'Bread and Bowl', 'Drinks'),
(6, 'The Library Cafe', 'Snacks'),
(7, 'The Library Cafe', 'Smoothies'),
(8, 'The Library Cafe', 'Coffee Drinks'),
(9, 'The Library Cafe', 'Muffins'),
(10, 'The Library Cafe', 'Drinks'),
(20, 'Chick-Fil-A', 'Chicken Sandwiches'),
(21, 'Chick-Fil-A', 'Waffle Fries'),
(22, 'Chick-Fil-A', 'Nuggets'),
(23, 'Moe''s', 'Burritos'),
(24, 'Moe''s', 'Chips & Salsa'),
(25, 'Moe''s', 'Quesadillas'),
(26, 'Moe''s', 'Tacos'),
(27, 'Moe''s', 'Nachos'),
(28, 'Sushi with Gusto', 'Sushi'),
(29, 'The Paddock', 'Specialty Sandwiches'),
(30, 'The Paddock', 'Grilled Items'),
(31, 'The Paddock', 'Salads'),
(32, 'The Paddock', 'Drinks'),
(33, 'The Paddock', 'Beer and Wine'),
(34, 'Barnes & Noble Cafe', 'Starbucks Coffee'),
(35, 'Barnes & Noble Cafe', 'Snacks'),
(36, 'Barnes & Noble Cafe', 'Hot Chocolate'),
(37, 'Traditions Grille', 'Sandwiches'),
(38, 'Traditions Grille', 'Grilled Items'),
(39, 'Traditions Grille', 'Snack Food'),
(40, 'Traditions Grille', 'Drinks'),
(41, 'Traditions Grille', 'Beer and Wine'),
(42, 'Papa John''s Pizza', 'Pizza');

--
-- Triggers restaurantMenu
--
-- AFTER INSERT: Update updateTimes
CREATE TRIGGER rm_on_insert
AFTER INSERT ON restaurantMenu
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'restaurantMenu';
END;

-- BEFORE UPDATE: Update updateTimes
CREATE TRIGGER rm_on_update
BEFORE UPDATE ON restaurantMenu
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'restaurantMenu';
END;

-- AFTER DELETE: Update updateTimes
CREATE TRIGGER rm_ondelete
AFTER DELETE ON restaurantMenu
FOR EACH ROW
BEGIN
  UPDATE updateTimes
  SET newestUpdate = CURRENT_TIMESTAMP
  WHERE updatedTable = 'restaurantMenu';
END;

-- --------------------------------------------------------

--
-- Table structure for table shuttleLocations
--

CREATE TABLE IF NOT EXISTS shuttleLocations (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  vehicle TEXT NOT NULL,
  latitude REAL(10,8) DEFAULT NULL,
  longitude REAL(10,8) DEFAULT NULL,
  speed INTEGER DEFAULT NULL,
  direction INTEGER DEFAULT NULL,
  nextStopDistance REAL DEFAULT NULL,
  updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  nextStopID INTEGER DEFAULT NULL
);


CREATE TRIGGER update_shuttleLocations_updated
AFTER UPDATE ON shuttleLocations
FOR EACH ROW
BEGIN
  UPDATE shuttleLocations SET updated = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- --------------------------------------------------------

--
-- Table structure for table Standups
--

CREATE TABLE IF NOT EXISTS Standups (
  name TEXT NOT NULL,
  date date NOT NULL,
  priorDay TEXT NOT NULL,
  thisDay TEXT NOT NULL,
  blockers TEXT NOT NULL,
  recNum INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

--
-- Dumping data for table Standups
--

INSERT INTO Standups (name, date, priorDay, thisDay, blockers, recNum) VALUES
('Michael', '2022-10-25', 'Set up basic login page on server', 'Link login to SQL database', '', 15),
('Jack', '2022-10-25', 'Configured JavaFX to work.', 'Test it on all of my groups machines.', 'Nothing', 19),
('Jackson', '2022-10-25', 'Decided on, and got server and', 'Work on connecting database and php and ', 'None currently', 21),
('Phillip', '2022-10-25', 'I coded up a loose version of the front ', 'None', 'None', 22),
('Luke', '2022-10-25', 'Talked to Treu about the databases and m', 'share the db knowledge with my group', 'nothing', 23),
('John', '2022-10-25', 'Met with Dr. Treu to discuss databases a', 'Today I will use what I learned from PHP', 'Really busy week regarding other class c', 24),
('Reed', '2022-10-25', 'Studied HTML and JavaScript. Created a n', 'Make HTML page interactive w/ either Jav', 'Group decisions about database and prefe', 25),
('Tate', '2022-10-25', 'Learning PHP, get treu to make database,', 'work on understanding code and adding co', 'my limited knowledge/understanding of th', 26),
('Jake', '2022-10-25', 'Created sample input form in access', 'Create functional input form', '', 27),
('Michael', '2022-10-25', 'Familiarized myself with the PHPDatabase', 'Began to build one of the first data tab', 'PHP My Admin login: talk to True', 28),
('Ting', '2022-10-25', 'get familiar with js and react', 'create fields for the database', 'n/a', 29),
('George', '2022-10-25', 'Created Login Screen', 'Create tables in DB', '', 30),
('Brycen', '2022-10-25', 'Creating a skeleton for frontend and bac', 'Creating tables in the database', 'Not right now', 31),
('', '2022-10-26', '', '', '', 33),
('Phillip', '2022-10-27', 'I worked on looking up designs templates', 'Work with Jackson to link database to ou', 'Test tomorrow', 34),
('Michael', '2022-10-27', 'Studied PHP', 'Implement PHP login', 'Database setup', 35),
('Tate', '2022-10-27', 'started work on user table in database', 'finishing up user table, going to ask dr', 'unsure how to finish table! need more info', 36),
('Brycen Addison', '2022-10-27', 'Set up API backend, created new reposito', 'Explain how the app will work to the res', 'None', 37),
('Reed', '2022-10-27', 'Continued learning HTML and worked on ad', 'Finish add/remove account page', 'n/a', 38),
('Jackson', '2022-10-27', 'Organized Github files to ensure organiz', 'Figure out next sprint', '', 39),
('George', '2022-10-27', 'Created tables in database', 'making UI for admin page', '', 40),
('', '2022-10-27', '', '', '', 41),
('', '2022-10-28', '', '', '', 42),
('Phillip', '2022-11-01', 'Educated myself on front end development', 'None', 'none', 43),
('Brycen', '2022-11-01', 'Work on database/backend', '', 'Making database accessible outside Furman or creating a new database accessible ', 44),
('George', '2022-11-01', 'Worked on making admin UI', 'Finish admin UI', '', 45),
('Reed', '2022-11-01', 'Begin scheduling algorithm development', 'Get scheduling algorithm working, not ne', 'none', 46),
('Ting', '2022-11-01', 'Create UI for admin with general functio', 'Finalize the userEdit UI page for admin ', 'n/a', 47),
('John', '2022-11-01', 'Created a temporary database and tested ', 'Create a database to store information f', 'None', 48),
('Phillip', '2022-11-03', 'Worked on how to display student profile', 'Write and finish code to generate a stud', 'NONE', 49),
('Tate', '2022-11-03', 'worked on fixing the session variables i', 'ensure that login gets to dashboard as e', 'I do not have access to michaels server so it is hard to tell if what I am doing', 50),
('Jackson', '2022-11-03', 'Set up helper methods and php for admin ', 'finish completing admin panel and figure', 'setting up hosting on cs server', 51),
('Reed', '2022-11-03', 'Wrote sorting algorithm', 'Further optimize algorithm if needed. Fi', 'None', 52),
('', '2022-11-03', '', '', '', 53),
('', '2022-11-03', '', '', '', 54),
('Jack', '2022-11-03', 'added all of our work into one branch', 'added authentication to database', 'nothing', 55),
('Johnathan Dewey', '2022-11-04', 'Created SQL operations to add forms and ', 'Create Admin permissions', 'None', 56),
('Tate', '2022-11-10', 'worked on CSS files to improve the look ', 'continue work on these files and get the', 'I forgot my password for citrix... I will think of it', 57),
('', '2022-11-10', '', '', '', 58),
('Jackson', '2022-11-17', 'Set up base for student specefic module', 'Work on OOP classes and base and researc', 'N/A', 59),
('Phillip', '2022-11-17', 'Researched into filters and displaying r', 'Begin coding functional pieces of the we', 'None', 60);

-- --------------------------------------------------------

--
-- Table structure for table stopsDistanceTable
--

CREATE TABLE IF NOT EXISTS stopsDistanceTable (
  lineID INTEGER NOT NULL,
  stopOrderID INTEGER NOT NULL,
  distFromVehicle REAL DEFAULT NULL,
  updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  vehicleStopsUntil INTEGER DEFAULT NULL
);




CREATE TABLE IF NOT EXISTS stopsTable (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  lineID INTEGER NOT NULL,
  stopOrderID INTEGER NOT NULL,
  stopName TEXT NOT NULL,
  latitude REAL NOT NULL,
  longitude REAL NOT NULL,
  distFromStart REAL NOT NULL,
  updated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);


--
-- Table structure for table TestMenu
--

CREATE TABLE IF NOT EXISTS TestMenu (
  id INTEGER NOT NULL,
  meal TEXT NOT NULL,
  itemName TEXT NOT NULL,
  station TEXT NOT NULL
);

--
-- Dumping data for table TestMenu
--

INSERT INTO TestMenu (id, meal, itemName, station) VALUES
(0, 'Breakfast', 'Scrambled Eggs*', 'Breakfast Grill'),
(0, 'Breakfast', 'Hard-boiled Eggs', 'Breakfast Grill'),
(0, 'Breakfast', 'Applewood Smoked Bacon', 'Breakfast Grill'),
(0, 'Breakfast', 'Pork Sausage', 'Breakfast Grill'),
(0, 'Breakfast', 'Turkey Sausage', 'Breakfast Grill'),
(0, 'Breakfast', 'Creamy Pork Sausage Country Gravy', 'Breakfast Grill'),
(0, 'Breakfast', 'House Baked Biscuits', 'Breakfast Grill'),
(0, 'Breakfast', 'Breakfast Potatoes with Peppers and Onions', 'Breakfast Grill'),
(0, 'Breakfast', 'Bacon, Roasted Vegetable and Potato Tot Casserole', 'Breakfast Grill'),
(0, 'Breakfast', 'Tofu Scrambled Eggs', 'Vegan'),
(0, 'Breakfast', 'Grits', 'Kettles'),
(0, 'Breakfast', 'Oatmeal', 'Kettles'),
(0, 'Breakfast', 'Made to Order Omelets*', 'Mongolian'),
(0, 'Brunch', 'Scrambled Eggs', 'Breakfast Grill'),
(0, 'Brunch', 'Scrambled Eggs', 'Breakfast Grill'),
(0, 'Brunch', 'House-made Buttermilk Pancakes', 'Breakfast Grill'),
(0, 'Brunch', 'Malted Waffles', 'Breakfast Grill'),
(0, 'Brunch', 'Texas French Toast', 'Breakfast Grill'),
(0, 'Brunch', 'Texas French Toast', 'Breakfast Grill'),
(0, 'Brunch', 'Malted Waffles', 'Breakfast Grill'),
(0, 'Brunch', 'House-made Buttermilk Pancakes', 'Breakfast Grill'),
(0, 'Brunch', 'Bacon', 'Breakfast Grill'),
(0, 'Brunch', 'Grilled Ham', 'Breakfast Grill'),
(0, 'Brunch', 'Pork Breakfast Sausage Links', 'Breakfast Grill'),
(0, 'Brunch', 'Pork Breakfast Sausage Links', 'Breakfast Grill'),
(0, 'Brunch', 'Grilled Ham', 'Breakfast Grill'),
(0, 'Brunch', 'Bacon', 'Breakfast Grill'),
(0, 'Brunch', 'Hash Browns with Peppers and Onions', 'Breakfast Grill'),
(0, 'Brunch', 'Buttermilk Biscuit and Creamy Pork Sausage Gravy', 'Breakfast Grill'),
(0, 'Brunch', 'Buttermilk Biscuit and Creamy Pork Sausage Gravy', 'Breakfast Grill'),
(0, 'Brunch', 'Hash Browns with Peppers and Onions', 'Breakfast Grill'),
(0, 'Brunch', 'Whole Egg', 'Breakfast Grill'),
(0, 'Brunch', 'Liquid Egg', 'Breakfast Grill'),
(0, 'Brunch', 'Egg White', 'Breakfast Grill'),
(0, 'Brunch', 'Bell Pepper', 'Breakfast Grill'),
(0, 'Brunch', 'Broccoli', 'Breakfast Grill'),
(0, 'Brunch', 'Onion', 'Breakfast Grill'),
(0, 'Brunch', 'Mushroom', 'Breakfast Grill'),
(0, 'Brunch', 'Spinach', 'Breakfast Grill'),
(0, 'Brunch', 'Tomato', 'Breakfast Grill'),
(0, 'Brunch', 'Salsa', 'Breakfast Grill'),
(0, 'Brunch', 'Pico De Gallo', 'Breakfast Grill'),
(0, 'Brunch', 'Cheddar Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Mozzarella Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Feta Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Pork Breakfast Sausage', 'Breakfast Grill'),
(0, 'Brunch', 'Smoked Ham', 'Breakfast Grill'),
(0, 'Brunch', 'Bacon', 'Breakfast Grill'),
(0, 'Brunch', 'Peanut Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Cream Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Fruit Cream Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Unsalted Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Honey Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Jelly', 'Breakfast Grill'),
(0, 'Brunch', 'Preserves', 'Breakfast Grill'),
(0, 'Brunch', 'Cheerios', 'Breakfast Grill'),
(0, 'Brunch', 'Rice Chex', 'Breakfast Grill'),
(0, 'Brunch', 'Raisin Bran', 'Breakfast Grill'),
(0, 'Brunch', 'Low Fat Granola', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Toast Crunch', 'Breakfast Grill'),
(0, 'Brunch', 'Cocoa Puffs', 'Breakfast Grill'),
(0, 'Brunch', 'Apple Jacks', 'Breakfast Grill'),
(0, 'Brunch', 'Cap''n Crunch', 'Breakfast Grill'),
(0, 'Brunch', 'Lucky Charms', 'Breakfast Grill'),
(0, 'Brunch', 'Raisins', 'Breakfast Grill'),
(0, 'Brunch', 'Pecans', 'Breakfast Grill'),
(0, 'Brunch', 'Brown Sugar', 'Breakfast Grill'),
(0, 'Brunch', 'Maple Syrup', 'Breakfast Grill'),
(0, 'Brunch', 'Honey', 'Breakfast Grill'),
(0, 'Brunch', 'Chocolate Chips', 'Breakfast Grill'),
(0, 'Brunch', 'Whipped Topping', 'Breakfast Grill'),
(0, 'Brunch', 'Whole Grain Bread', 'Breakfast Grill'),
(0, 'Brunch', 'Multigrain Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Sourdough Bread', 'Breakfast Grill'),
(0, 'Brunch', 'White Bread', 'Breakfast Grill'),
(0, 'Brunch', 'Plain Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Raisin Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Whole Egg', 'Breakfast Grill'),
(0, 'Brunch', 'Liquid Egg', 'Breakfast Grill'),
(0, 'Brunch', 'Egg White', 'Breakfast Grill'),
(0, 'Brunch', 'Bell Pepper', 'Breakfast Grill'),
(0, 'Brunch', 'Broccoli', 'Breakfast Grill'),
(0, 'Brunch', 'Onion', 'Breakfast Grill'),
(0, 'Brunch', 'Mushroom', 'Breakfast Grill'),
(0, 'Brunch', 'Spinach', 'Breakfast Grill'),
(0, 'Brunch', 'Tomato', 'Breakfast Grill'),
(0, 'Brunch', 'Salsa', 'Breakfast Grill'),
(0, 'Brunch', 'Pico De Gallo', 'Breakfast Grill'),
(0, 'Brunch', 'Cheddar Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Mozzarella Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Feta Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Pork Breakfast Sausage', 'Breakfast Grill'),
(0, 'Brunch', 'Smoked Ham', 'Breakfast Grill'),
(0, 'Brunch', 'Bacon', 'Breakfast Grill'),
(0, 'Brunch', 'Peanut Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Cream Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Fruit Cream Cheese', 'Breakfast Grill'),
(0, 'Brunch', 'Unsalted Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Honey Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Butter', 'Breakfast Grill'),
(0, 'Brunch', 'Jelly', 'Breakfast Grill'),
(0, 'Brunch', 'Preserves', 'Breakfast Grill'),
(0, 'Brunch', 'Cheerios', 'Breakfast Grill'),
(0, 'Brunch', 'Rice Chex', 'Breakfast Grill'),
(0, 'Brunch', 'Raisin Bran', 'Breakfast Grill'),
(0, 'Brunch', 'Low Fat Granola', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Toast Crunch', 'Breakfast Grill'),
(0, 'Brunch', 'Cocoa Puffs', 'Breakfast Grill'),
(0, 'Brunch', 'Apple Jacks', 'Breakfast Grill'),
(0, 'Brunch', 'Cap''n Crunch', 'Breakfast Grill'),
(0, 'Brunch', 'Lucky Charms', 'Breakfast Grill'),
(0, 'Brunch', 'Raisins', 'Breakfast Grill'),
(0, 'Brunch', 'Pecans', 'Breakfast Grill'),
(0, 'Brunch', 'Brown Sugar', 'Breakfast Grill'),
(0, 'Brunch', 'Maple Syrup', 'Breakfast Grill'),
(0, 'Brunch', 'Honey', 'Breakfast Grill'),
(0, 'Brunch', 'Chocolate Chips', 'Breakfast Grill'),
(0, 'Brunch', 'Whipped Topping', 'Breakfast Grill'),
(0, 'Brunch', 'Whole Grain Bread', 'Breakfast Grill'),
(0, 'Brunch', 'Multigrain Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Sourdough Bread', 'Breakfast Grill'),
(0, 'Brunch', 'White Bread', 'Breakfast Grill'),
(0, 'Brunch', 'Plain Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Cinnamon Raisin Mini Bagel', 'Breakfast Grill'),
(0, 'Brunch', 'Grapes', 'Salad Bar'),
(0, 'Brunch', 'Cantaloupe', 'Salad Bar'),
(0, 'Brunch', 'Honeydew', 'Salad Bar'),
(0, 'Brunch', 'Pineapple', 'Salad Bar'),
(0, 'Brunch', 'Strawberries', 'Salad Bar'),
(0, 'Brunch', 'Watermelon', 'Salad Bar'),
(0, 'Brunch', 'Low Fat Plain Yogurt', 'Salad Bar'),
(0, 'Brunch', 'Low Fat Vanilla Yogurt', 'Salad Bar'),
(0, 'Brunch', 'Low Fat Fruit Yogurt', 'Salad Bar'),
(0, 'Brunch', '2% Cottage Cheese', 'Salad Bar'),
(0, 'Brunch', 'Mixed Greens', 'Deli'),
(0, 'Brunch', 'Soy Milk', 'Smoothie'),
(0, 'Brunch', 'Low Fat Vanilla Yogurt', 'Smoothie'),
(0, 'Brunch', 'Apple Juice', 'Smoothie'),
(0, 'Brunch', 'Juice Orange', 'Smoothie'),
(0, 'Brunch', 'Banana', 'Smoothie'),
(0, 'Brunch', 'Blueberry', 'Smoothie'),
(0, 'Brunch', 'Mango', 'Smoothie'),
(0, 'Brunch', 'Papaya', 'Smoothie'),
(0, 'Brunch', 'Peach', 'Smoothie'),
(0, 'Brunch', 'Strawberry', 'Smoothie'),
(0, 'Brunch', 'Kale', 'Smoothie'),
(0, 'Brunch', 'Flax', 'Smoothie'),
(0, 'Brunch', 'Chia Seed', 'Smoothie'),
(0, 'Brunch', 'Full Fat Plain Greek Yogurt', 'Smoothie'),
(0, 'Lunch', 'Roasted Buffalo Bone in Chicken', 'Daniel Dining Specials'),
(0, 'Lunch', 'Grilled Hamburger Patty', 'Daniel Dining Specials'),
(0, 'Lunch', 'Grilled Chicken Breast', 'Daniel Dining Specials'),
(0, 'Lunch', 'House Made Fries', 'Daniel Dining Specials'),
(0, 'Lunch', 'Impossible Meatless Shepard''s Pie', 'Pure In Balance'),
(0, 'Lunch', 'Grilled Chicken Breast', 'Pure In Balance'),
(0, 'Lunch', 'House Made Fries', 'Pure In Balance'),
(0, 'Lunch', 'Grilled Hamburger Patty', 'Pure In Balance'),
(0, 'Lunch', 'Stir Fry Tofu and Vegetables', 'Pure Vegan'),
(0, 'Lunch', 'Vegan Chili', 'Pure Vegan'),
(0, 'Lunch', 'Burger Condiments', 'Pure Vegan'),
(0, 'Lunch', 'Vegan Toppings', 'Pure Vegan'),
(0, 'Lunch', 'Seitan and Broccoli Stir Fry', 'Vegan'),
(0, 'Lunch', 'Pepperoni Pizza', 'Piazza'),
(0, 'Lunch', 'Cheese Pizza', 'Piazza'),
(0, 'Lunch', 'House Made Marinara Sauce', 'Cucina Rustica'),
(0, 'Lunch', 'Creamy Alfredo Sauce', 'Cucina Rustica'),
(0, 'Lunch', 'Steamed Pasta with Olive Oil', 'Cucina Rustica'),
(0, 'Lunch', 'House Made Focaccia Bread with Roasted Garlic and Fresh Herbs', 'Cucina Rustica'),
(0, 'Dinner', 'Beef Bourguignon', 'Daniel Dining Specials'),
(0, 'Dinner', 'Grilled Hamburger Patty', 'Daniel Dining Specials'),
(0, 'Dinner', 'Grilled Chicken Breast', 'Daniel Dining Specials'),
(0, 'Dinner', 'House Made Fries', 'Daniel Dining Specials'),
(0, 'Dinner', 'Turkey and Vegetable Stir Fry', 'Pure In Balance'),
(0, 'Dinner', 'Grilled Chicken Breast', 'Pure In Balance'),
(0, 'Dinner', 'House Made Fries', 'Pure In Balance'),
(0, 'Dinner', 'Grilled Hamburger Patty', 'Pure In Balance'),
(0, 'Dinner', 'Zucchini and Red Lentil Curry Stew', 'Pure Vegan'),
(0, 'Dinner', 'Vegan Chili', 'Pure Vegan'),
(0, 'Dinner', 'Burger Condiments', 'Pure Vegan'),
(0, 'Dinner', 'Vegan Toppings', 'Pure Vegan'),
(0, 'Dinner', 'Vegan Impossible Meatless Enchiladas', 'Vegan'),
(0, 'Dinner', 'Beef or Tofu Philly Steak Hoagie', 'Mongolian'),
(0, 'Dinner', 'Pepperoni Pizza', 'Piazza'),
(0, 'Dinner', 'Cheese Pizza', 'Piazza'),
(0, 'Dinner', 'House Made Marinara Sauce', 'Cucina Rustica'),
(0, 'Dinner', 'Creamy Alfredo Sauce', 'Cucina Rustica'),
(0, 'Dinner', 'Steamed Pasta with Olive Oil', 'Cucina Rustica'),
(0, 'Dinner', 'House Made Focaccia Bread with Roasted Garlic and Fresh Herbs', 'Cucina Rustica'),
(0, 'Breakfast', 'Grits', 'Kettles'),
(0, 'Breakfast', 'Grits', 'Kettles'),
(0, 'Breakfast', 'Grits', 'Kettles'),
(0, 'Breakfast', 'Grits', 'Kettles'),
(0, 'Breakfast', 'Grits', 'Kettles');

-- --------------------------------------------------------

--
-- Table structure for table TestNulls
--

CREATE TABLE IF NOT EXISTS TestNulls (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  location TEXT NOT NULL
);

--
-- Dumping data for table TestNulls
--

INSERT INTO TestNulls (id, title, description, location) VALUES
(1, 'Kappa Delta’s International Women’s Friendship Month - Writing Cards to Women', '', 'Testing location'),
(2, 'Second Title', 'Second full description. ''', 'and second location');

-- --------------------------------------------------------

--
-- Table structure for table TESTtimes
--

CREATE TABLE IF NOT EXISTS TESTtimes (
  hoursID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  ManuallyEntered INTEGER NOT NULL DEFAULT '0',
  id INTEGER NOT NULL,
  meal TEXT DEFAULT NULL,
  start time DEFAULT NULL,
  end time DEFAULT NULL,
  dayOfWeek TEXT DEFAULT NULL,
  dayOrder INTEGER NOT NULL
);

--
-- Dumping data for table TESTtimes
--

INSERT INTO TESTtimes (hoursID, ManuallyEntered, id, meal, start, end, dayOfWeek, dayOrder) VALUES
(14, 1, 23, NULL, '11:00:00', '21:00:00', 'Mon-Fri', 0),
(16, 1, 23, NULL, '14:00:00', '21:00:00', 'Sun', 6),
(18, 1, 28, NULL, '08:30:00', '18:00:00', 'Mon-Fri', 0),
(19, 1, 28, NULL, '10:00:00', '15:00:00', 'Sat-Sun', 5),
(1568, 1, 10, NULL, '11:00:01', '23:59:00', 'Mon-Thu', 0),
(1569, 1, 10, NULL, '11:00:00', '01:00:00', 'Fri-Sat', 4),
(1570, 1, 10, NULL, '11:00:00', '23:00:00', 'Sun', 6),
(2656, 0, 13, 'B''fast', '07:15:00', '10:30:00', 'Mon-Fri', 0),
(2657, 0, 13, 'B''fast', '09:00:00', '11:00:00', 'Sat-Sun', 0),
(2658, 0, 13, 'Brunch', '11:00:00', '14:00:00', 'Sat-Sun', 0),
(2659, 0, 13, 'Lunch', '11:00:00', '14:00:00', 'Mon-Sun', 0),
(2660, 0, 13, 'Dinner', '17:00:00', '20:30:00', 'Mon-Thu/Sun', 0),
(2661, 0, 13, 'Dinner', '17:00:00', '20:00:00', 'Fri-Sat', 0),
(2662, 0, 13, 'Grab & Go', '14:00:00', '17:00:00', 'Mon-Sun', 0),
(2663, 0, 13, 'Late Night', '20:30:00', '21:30:00', 'Mon-Thu/Sun', 0),
(2664, 0, 30, 'B''fast', '08:00:00', '21:00:00', 'Mon-Fri', 0),
(2665, 0, 30, 'Lunch', '11:00:00', '21:00:00', 'Mon-Fri', 0),
(2666, 0, 30, 'Lunch', '14:00:00', '21:00:00', 'Sun', 0),
(2667, 0, 25, 'Lunch', '11:00:00', '21:00:00', 'Tue-Thu', 0),
(2668, 0, 25, 'Lunch', '11:00:00', '21:00:00', 'Fri-Sat', 0),
(2669, 0, 29, 'Grill', '08:30:00', '18:30:00', 'Mon/Wed', 0),
(2670, 0, 29, 'Grill', '08:30:00', '20:00:00', 'Tue/Thu', 0),
(2671, 0, 29, 'Grill', '08:00:00', '18:30:00', 'Fri-Sat', 0),
(2672, 0, 29, 'Grill', '08:00:00', '18:00:00', 'Sun', 0),
(2673, 0, 18, 'All Day', '08:00:00', '17:00:00', 'Mon-Thu', 0),
(2674, 0, 18, 'B''fast & Lunch', '08:00:00', '16:00:00', 'Fri', 0),
(2675, 0, 17, 'Lunch', '11:00:00', '22:00:00', 'Mon-Sun', 0);

-- --------------------------------------------------------

--
-- Table structure for table times
--

CREATE TABLE IF NOT EXISTS times (
  hoursID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  id INTEGER NOT NULL,
  meal TEXT DEFAULT NULL,
  start time DEFAULT NULL,
  end time DEFAULT NULL,
  dayOfWeek TEXT DEFAULT NULL,
  dayOrder INTEGER NOT NULL,
  lastUpdated TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id) REFERENCES foodService(id) ON DELETE CASCADE ON UPDATE CASCADE
);

--
-- Dumping data for table times
--

INSERT INTO times (hoursID, id, meal, start, end, dayOfWeek, dayOrder, lastUpdated) VALUES
(6, 22, NULL, '11:00:00', '21:00:00', 'Mon-Fri', 0, '0000-00-00 00:00:00'),
(7, 22, NULL, '14:00:00', '21:00:00', 'Sun', 6, '0000-00-00 00:00:00'),
(13, 21, NULL, '08:00:00', '21:00:00', 'Mon-Fri', 0, '0000-00-00 00:00:00'),
(14, 23, NULL, '11:00:00', '21:00:00', 'Mon-Fri', 0, '0000-00-00 00:00:00'),
(16, 23, NULL, '14:00:00', '21:00:00', 'Sun', 6, '0000-00-00 00:00:00'),
(18, 28, NULL, '08:30:00', '18:00:00', 'Mon-Fri', 0, '0000-00-00 00:00:00'),
(19, 28, NULL, '10:00:00', '15:00:00', 'Sat-Sun', 5, '0000-00-00 00:00:00'),
(1568, 10, NULL, '11:00:00', '23:59:00', 'Mon-Thu', 0, '0000-00-00 00:00:00'),
(1569, 10, NULL, '11:00:00', '01:00:00', 'Fri-Sat', 4, '0000-00-00 00:00:00'),
(1570, 10, NULL, '11:00:00', '23:00:00', 'Sun', 6, '0000-00-00 00:00:00'),
(11376, 17, NULL, NULL, NULL, 'Mon-Sun', 0, '2024-08-19 04:01:02'),
(11377, 18, NULL, NULL, NULL, 'Mon-Sun', 0, '2024-08-19 04:01:02'),
(12456, 13, NULL, NULL, NULL, 'Mon-Sun', 0, '2025-01-11 05:01:01'),
(12457, 30, NULL, NULL, NULL, 'Mon-Sun', 0, '2025-01-11 05:01:01'),
(12458, 25, NULL, NULL, NULL, 'Mon-Sun', 0, '2025-01-11 05:01:01'),
(12459, 29, 'Open', '08:00:00', '18:00:00', 'Mon-Sun', 0, '2025-01-11 05:01:01');

--
-- Triggers times
--
-- AFTER DELETE: Insert into updateTimes
CREATE TRIGGER times_afterDelete
AFTER DELETE ON times
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('times');
END;

-- AFTER UPDATE: Insert into updateTimes
CREATE TRIGGER times_afterUpdate
AFTER UPDATE ON times
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('times');
END;

-- BEFORE DELETE: Delete from updateTimes
CREATE TRIGGER times_beforeDelete
BEFORE DELETE ON times
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'times';
END;

-- BEFORE UPDATE: Delete from updateTimes
CREATE TRIGGER times_beforeUpdate
BEFORE UPDATE ON times
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'times';
END;

-- BEFORE INSERT: Delete from updateTimes
CREATE TRIGGER times_deleteUpdateTimes
BEFORE INSERT ON times
FOR EACH ROW
BEGIN
  DELETE FROM updateTimes WHERE updatedTable = 'times';
END;

-- AFTER INSERT: Insert into updateTimes
CREATE TRIGGER times_inserted
AFTER INSERT ON times
FOR EACH ROW
BEGIN
  INSERT INTO updateTimes (updatedTable) VALUES ('times');
END;

-- --------------------------------------------------------

--
-- Table structure for table updateTimes
--

CREATE TABLE IF NOT EXISTS updateTimes (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  newestUpdate TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updatedTable TEXT NOT NULL
);

--
-- Dumping data for table updateTimes
--

INSERT INTO updateTimes (id, newestUpdate, updatedTable) VALUES
(135, '2024-06-13 00:34:29', 'healthSafety'),
(6766, '2025-06-16 04:00:02', 'clps'),
(7402, '2024-06-13 00:34:29', 'foodService'),
(7404, '2024-06-13 00:34:29', 'contacts'),
(7414, '2024-06-13 00:34:29', 'vehicleNames'),
(7416, '2025-06-16 04:01:04', 'DHmenu'),
(7417, '2024-06-13 00:34:29', 'restaurantMenu'),
(117242, '2024-06-13 00:34:29', 'buildingLocations'),
(492567, '2025-01-05 05:00:06', 'importantDates'),
(496764, '2025-01-11 05:01:01', 'times'),
(497072, '2025-01-11 16:00:01', 'buildingHours');

-- --------------------------------------------------------

--
-- Table structure for table vehicleNames
--

CREATE TABLE IF NOT EXISTS vehicleNames (
  vehicleIndex INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  shortName TEXT NOT NULL,
  serviceTimes TEXT NOT NULL,
  locations TEXT NOT NULL,
  colorRed REAL NOT NULL,
  colorGreen REAL NOT NULL,
  colorBlue REAL NOT NULL,
  iconName TEXT NOT NULL,
  routePolyline TEXT NOT NULL,
  website TEXT NOT NULL,
  color TEXT NOT NULL,
  averageSpeed REAL NOT NULL,
  averageStopSeconds INTEGER NOT NULL,
  message TEXT NOT NULL
);

--
-- Dumping data for table vehicleNames
--

INSERT INTO vehicleNames (vehicleIndex, name, shortName, serviceTimes, locations, colorRed, colorGreen, colorBlue, iconName, routePolyline, website, color, averageSpeed, averageStopSeconds, message) VALUES
(1, '503 Bus', '', 'M-Sat 5:55am-7:55pm', 'Front Gate/Cherrydale/Downtown', 0.71, 0.92, 0.64, 'location.circle', 'izvsEvg}uNc@hAw@j@SPSNOJONKFWPMJQLq@h@YTQLIFYLWJYL??]@o@\\a@RULe@OSK[Oe@EW@KAQAk@ASORNq@Dq@Ac@GW?O?S?Y?U@M?mA@JUYTQ?I?c@?k@?W@??]I[?{@B_@G[Aw@CI?{BC^OkCLQFI?w@@w@?G?UAg@AQ?o@?_@AcA?y@?U?M?m@?]AU@COCECICMEOQUEEOIQKcAm@e@WYQOIMIe@WqAu@aAk@WQq@c@{@i@g@]k@]k@_@q@c@GE_@UcAo@g@u@gAYg@[YSUQSUKQMUYo@Os@SaAi@sC_@uBESCOWqAG[UcABIOi@Ai@E]CSCQE_@AGK{@E]EQG[Wy@?UQ]]c@g@YIEKIUMSKOEcA[QGi@Qg@QYMq@]PQe@B[Se@[ECEE]]SSKKGIk@s@QUSYCEa@o@Yg@e@aAISMWgA_C}@iB??QPGFq@j@ONe@l@S\\ELCDEPCTGlA?VIbAk@v@[LDFQNmBrAMHSJg@X]Pw@\\k@RIBqAZ]FO?MAMGKIKOGQWm@M[M]GWAIAS@MBQBMFUBIBGRa@JQLUHOFa@MA[GyA[YGcCi@gAUeB_@QCWAS?Q?W@UDK@MDSGCNQFKDMH[NKFUP???TBt@@p@?l@?@?XAPCfAA^Af@IlAE@CZAJMhAObASdAUdAU~@M@GRUp@O@GRKTUh@iAfCq@xAq@tAc@|@GPQZgAjAAt@mAhCEHS@m@lACBEHSb@u@jBcApBk@V@v@IZGXI^AT?NAf@@b@?FF\\@HDPPl@Pb@DH@j@NX??@d@DPFZBT?HBnAJPe@Pu@ZID[PW^MHMFe@ZGBMJk@@i@b@m@f@qApAoBnB}A~AaDDSRs@t@q@n@UV[XkBlB_B~Ag@f@kCjC_Ad@JLyAzAy@x@EFgAdAeAfAiAhAMJ_A~@KL]ZKL[X[\\e@d@m@j@o@r@ONe@b@{@|@ED[ZWXgAjAWXSVMJqAhAe@d@e@b@o@p@o@n@u@t@aAAkBlBYVi@j@g@f@gAfAiAjAeFdFyDzDo@l@oApA}@~@QPqBnB[\\SPMJONg@d@qCdB??UL[NOH]JeDz@c@Pa@Ry@^u@d@w@j@o@j@o@n@_@b@]b@]f@e@x@U@Wh@eB|Dc@|@}@pAe@r@k@r@i@j@i@f@k@d@q@d@u@@s@\\u@Xw@Tw@R{@Le@Fk@Dk@Bk@@wB@uA?w@AcAAsACo@?K?i@W_Bu@mBy@[O]Ka@EW@WHYNWXQ\\K\\If@YjAaA|DMh@GVLFHDLFTJNOIGFQNi@BIZw@TYf@g@d@_@j@Y|@U|AInB?N?hA?fA?tJ?dAEhAG|@Mz@Qr@Qx@Yt@]x@a@t@e@r@g@bA}@p@s@l@w@t@iAt@s@j@k@r@sAT_@^g@@g@^e@FGTI^WTIZ?JKz@Jd@FXFhA\\LBJBj@LPDLBBEJYZkADODSL_@Lg@BGJ[Ja@Ni@H]JGB[H_@HUDKDMHMPSHGFGJGHCAMI]EMK]??pCeBf@e@NOLKRQZ]pBoBPQ|@_AnAqAn@m@xD{DdFeFhAkAfAgAf@g@h@k@XWjBmBAaAt@u@n@o@n@q@d@c@d@e@pAiALKRWVYfAkAd@@M[Z[DEz@}@d@c@NOn@s@l@k@d@e@Z]ZYJM\\[JM~@_ALKhAiAdAgAfAeADGx@y@xA{A|@SI_@jCkCf@g@~A_BjBmBZYTWp@o@r@u@RSDaD|A_BnBoBpAqAl@g@h@c@j@a@LKFCd@[LG\\QPAZMAa@XK?U?IN[CgAC]Ge@O_@T?i@M??OYa@k@EIQc@Qm@EQAIG]?GAc@@g@?O@UH_@FYH[h@oAbAqBt@kBRc@DIBCl@mARa@DIlAiChAaCP[FQb@}@p@uAp@yAhAgCTi@JUFSNa@Tq@FSLa@T_ATeAReANcALiA@KB[Da@HmA@g@@_@BgA@Q?Y?a@?m@Aq@Cu@?U??TQJGZOLIJEPGVGLEJA@RRYVAP?R?V@PBdB^fATbCh@XFxAZZFL@G@INMTKPS@CFCHGTCLCPAL@R@HFVL\\LZVl@FPJNJHLFL@N?\\GpA[HCj@Sv@]\\Qf@YRKLIlBsAZAIMTUj@w@HcA?WFmABUDQBEDMR]d@m@NOp@k@FGPQ??|@hBfA~BLVOHXHd@AXf@@n@BDRXPTj@r@FHJJRR\\\\DDDBDZ^?ZRRLp@\\XLf@Ph@PPFbAZNDRJTLJHHDf@X\\b@P\\EPGCGKKSYe@?Iz@vAVx@FZDPD\\Jz@@FD^BPBRD\\@h@Nh@CHTbAFZVpABNDR^tBh@rCRANr@Xn@LTJPRTTPXRf@ZnBnAw@AzBp@^TFDp@b@j@^j@\\f@\\z@h@p@b@VPAj@pAt@WD|@PLHNHXPd@VbAl@PJNHDDPTDNBLBHBDBNTA\\@l@?L?T?x@?bA?^@n@?P?f@@T@F?v@?Bf@r@i@H?PF\\?jAB~BBMTTUv@Bz@Bh@@R@X?\\I????VAj@?b@?H?P?L?lAAJNn@@SHb@GD?N?V??Ub@Fp@@p@E??j@@P@J@PR^HRBZLXNPD^C^SHEj@[G[\\A??XMVKXMHGPMXUp@i@PMLKVQJGNONKRORQv@k@Z?Xq@l@e@NMLIb@a@f@a@NKhAaAHE\\Yx@q@f@]\\WLKHGJGLKFGVQHGTQXUNMLQNWHQJUFULF@LPFHBNDJDDBJBPFjBn@^LFBf@N@NJD\\JHDJDF@JDPJLJDFFHJPBDRXTZ??FUBO@EDOBMDS@EDUDQ??BMM[OEOG{@PfAx@??RJ??AFADERCLENADCNGTGVe@tBCNOl@ALCHUK}Am@a@QOIe@QQKOGiCeAeBu@}CsAi@W}Aq@_@OKEaAm@OE??EJIZEP??K\\I^g@jBSt@CPETOh@U|@IJ', 'https://greenlink.cadavl.com:4437/SWIV/GTA', '#2c8358', 40, 50, 'The Greenlink 503 bus runs between campus and downtown Greenville Monday through Friday, 5:30 a.m. - 11:30 p.m., and 8:30 a.m. to 6:30 p.m. on Saturdays.'),
(2, 'Campus Shuttle', '', 'Morning & Afternoon', 'various campus', 0.34375, 0.171875, 0.511719, 'car', 'kretE~cvNA??CAAACEEIEA?A?A@CDOVEFm@l@GHQVO\\GVANCR??@?\\FLDDDFFBH??hAY^Ih@O\\MFCVMJC@UnBkApAu@^Sn@_@v@e@HE\\Wj@_@??l@A@DP\\p@tAV|@DLHZDRF\\Nf@P\\FHBB@BTV^\\h@Z^Jj@H@@??LA@?AO@NB?PEPM@AvD@BQHYN]LSRQRGXCVAPBb@R@GAFNHxAlAf@n@FJDJBJBP@d@@RAFABQ@Sd@INGFKFk@P??FVDHIDHE\\hANd@??IJCDQZSZADCFEP?N?@@D@NFN?BBBBHFN@BDF?@h@A\\b@v@j@B@\\LZND?b@@b@B@EJAt@]FGv@w@Z[JS?Q?ICKIQACS]CEe@}@AASa@Uc@GM[XZYMUUa@??AaAZ[Z[RSr@mA??P?PENGPMDMDDEEDKFc@?QEOGSKQOMOEWA??c@c@eCoCuB}Bq@k@?A?@s@k@}D}BgCyA??AO?MAKAGCGCGCIEGGGEGECEEECGCWGGAI?E?K@E@YJKFIJKNGP?DOENDCJCZ@X??aA[a@Ma@MKCy@SEAeBTOFIDUNGDWRKJ??EQDPYV]Xa@^WPKHk@^]VIDw@d@o@^_@RqAt@oBjAa@TKBWLGB]Li@N_@HiAX??CIGGEEME]GA???BS@OFWN]PJF@DAJEPOTSNUR]BI?C?A', 'https://furmansaferide.ridesystems.net/routes/3/stops', '#582c83', 15, 30, 'The Campus Shuttle operates on campus from  7:30 a.m. to 11:30 a.m. and 1 p.m. to 5 p.m. on weekdays.'),
(3, 'Walmart Shuttle', '', '', '', 0, 0, 0, '', '_sdtEladvN\\DBOJUGg@?QBa@HQF_@v@{CPBRPRNTB\\A@KVYNo@H{@Ms@SUCe@Ls@Fo@To@Jg@X_AJq@\\oAZcALMpAu@n@Jh@Nh@^ZXFZENKNMBoA?wAFoB?eB@i@?kC@wB?s@?y@@{@AcB?{BAyC?w@?qB?aA?}B?gA?}B@s@FmDP[DgDd@S@eDf@m@PeBX{@LcB@a@JwB@mGnAwH|AmDn@aFdAgEdAsD~A}E~BkBj@yARo@DaAHmCN{CZcAPu@Ps@Vk@PcAd@{@Zi@XaCz@cDv@qANiA@[?kCQiCe@kDu@}Bw@iCeAuBcA}AgAqAcA_Ay@_ByAc@_@qDyD_A_ABUFINWXYd@g@b@_@^]LQDQIQMGQ?y@e@QMg@We@OMGUS?WFSF_@LeAXsAHU?O[Aa@GKZShAKjAL^VNAZAb@RNXJRHXNJDRLPLLFPJHL@XGVIRKNWPYR_@Xa@h@SPKR?RHLPDPLFFPPfQfPvB~BtCjBlDv@hEb@dMO|Ky@xF_AD_BxEaCzOuHvDgAhAUt[oGlYaFr@MfAC|S_@~C?zHBnGFp@d@VZH@BZB~@ITK@E@ETIRGDQNYRW\\AX?V?\\CXCd@Mj@Ur@GRMh@IPKTK^MTIRETFNHH??', 'https://www.furman.edu/university-police/saferide-shuttle/', '#2c5883', 0, 0, 'The Walmart Shuttle takes students from Lakeside/Clark Murphy to the Travelers Rest Walmart on Sunday evenings.');

-- --------------------------------------------------------

--
-- Table structure for table weather
--

CREATE TABLE IF NOT EXISTS weather (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  day TEXT DEFAULT NULL,
  start TEXT DEFAULT NULL,
  end TEXT DEFAULT NULL,
  isDayTime TEXT NOT NULL DEFAULT 'True',
  tempCurrent INTEGER DEFAULT NULL,
  tempHi INTEGER NOT NULL,
  tempLo INTEGER NOT NULL,
  unit TEXT NOT NULL DEFAULT 'F',
  precipitationPercent TEXT NOT NULL,
  windSpeed TEXT DEFAULT NULL,
  windDirection TEXT DEFAULT NULL,
  shortForecast TEXT DEFAULT NULL,
  detailedForecast TEXT DEFAULT NULL,
  alert TEXT NOT NULL DEFAULT '',
  emoji TEXT DEFAULT NULL
);

--
-- Table structure for table ZToDo
--

CREATE TABLE IF NOT EXISTS ZToDo (
  recId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  taskName TEXT NOT NULL,
  duration time NOT NULL DEFAULT '00:01:00',
  indoor INTEGER NOT NULL DEFAULT '1',
  minTemp INTEGER NOT NULL DEFAULT '50',
  maxTemp INTEGER NOT NULL DEFAULT '90',
  minNoRain INTEGER NOT NULL,
  bestTOD TEXT NOT NULL DEFAULT 'AM',
  priority INTEGER NOT NULL,
  tools TEXT NOT NULL,
  material TEXT NOT NULL,
  instructions TEXT NOT NULL,
  media TEXT NOT NULL,
  notes TEXT NOT NULL,
  lastCompleted date NOT NULL,
  repeatDays INTEGER NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_foodService_fullname ON foodService(fullname);
CREATE UNIQUE INDEX IF NOT EXISTS idx_GolfPlayers_playerId ON GolfPlayers(playerId);
CREATE UNIQUE INDEX IF NOT EXISTS idx_GolfRounds_playerId_playDate ON GolfRounds(playerId, playDate);
CREATE UNIQUE INDEX IF NOT EXISTS idx_GolfSchedule_playerId_date ON GolfSchedule(playerId, date);
CREATE UNIQUE INDEX IF NOT EXISTS idx_vehicleNames_name ON vehicleNames(name);
CREATE UNIQUE INDEX IF NOT EXISTS idx_ZToDo_recId ON ZToDo(recId);

-- For Normal Indexes (MySQL: ADD KEY / ADD INDEX):
CREATE INDEX IF NOT EXISTS idx_buildingHours_buildingID ON buildingHours(buildingID);
CREATE INDEX IF NOT EXISTS idx_FU20_RestaurantHours_id ON FU20_RestaurantHours(id);
CREATE INDEX IF NOT EXISTS idx_GolfRounds_rec ON GolfRounds(rec);
CREATE INDEX IF NOT EXISTS idx_newsContent_publisherID ON newsContent(publisherID);
CREATE INDEX IF NOT EXISTS idx_TESTtimes_id ON TESTtimes(id);
CREATE INDEX IF NOT EXISTS idx_times_id ON times(id);

CREATE UNIQUE INDEX IF NOT EXISTS idx_unique_line_stop
ON stopsTable (lineID, stopOrderID);

CREATE VIEW stop_with_distance AS
SELECT 
    s.lineID,
    s.stopOrderID,
    s.distFromStart,
    s.latitude,
    s.longitude,
    s.stopName,
    s.updated,
    d.distFromVehicle,
    d.vehicleStopsUntil
FROM stopsTable s
JOIN stopsDistanceTable d
  ON s.lineID = d.lineID AND s.stopOrderID = d.stopOrderID;


--
-- Indexes for dumped tables
--

--
-- Indexes for table athletics
--

--
-- Indexes for table benches
--

--
-- Indexes for table buildingHours
--

--
-- Indexes for table buildingLocations
--

--
-- Indexes for table BusStops
-- --
-- ALTER TABLE BusStops
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table clps
-- --
-- ALTER TABLE clps
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table contacts
-- --
-- ALTER TABLE contacts
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table DHmenu
-- --
-- ALTER TABLE DHmenu
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table foodService
-- --
-- ALTER TABLE foodService
--   ADD PRIMARY KEY (id),
--   ADD UNIQUE KEY fullname (fullname);

-- --
-- -- Indexes for table FU20_RestaurantHours
-- --
-- ALTER TABLE FU20_RestaurantHours
--   ADD PRIMARY KEY (hoursID),
--   ADD KEY id (id);

-- --
-- -- Indexes for table GolfDay
-- --
-- ALTER TABLE GolfDay
--   ADD PRIMARY KEY (day);

-- --
-- -- Indexes for table GolfPlayers
-- --
-- ALTER TABLE GolfPlayers
--   ADD PRIMARY KEY (rec),
--   ADD UNIQUE KEY playerId (playerId);

-- --
-- -- Indexes for table GolfRounds
-- --
-- ALTER TABLE GolfRounds
--   ADD PRIMARY KEY (rec),
--   ADD UNIQUE KEY playerId (playerId,playDate),
--   ADD KEY REC (rec);

-- --
-- -- Indexes for table GolfSchedule
-- --
-- ALTER TABLE GolfSchedule
--   ADD PRIMARY KEY (rec),
--   ADD UNIQUE KEY playerId (playerId,date);

-- --
-- -- Indexes for table healthSafety
-- --
-- ALTER TABLE healthSafety
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table importantDates
-- --
-- ALTER TABLE importantDates
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table importantLinks
-- --
-- ALTER TABLE importantLinks
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table newsContent
-- --
-- ALTER TABLE newsContent
--   ADD PRIMARY KEY (id),
--   ADD UNIQUE KEY id (id),
--   ADD KEY publisherID (publisherID);

-- --
-- -- Indexes for table newsPublishers
-- --
-- ALTER TABLE newsPublishers
--   ADD PRIMARY KEY (publisherID);

-- --
-- -- Indexes for table parkingResources
-- --
-- ALTER TABLE parkingResources
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table parkingZones
-- --
-- ALTER TABLE parkingZones
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table restaurantMenu
-- --
-- ALTER TABLE restaurantMenu
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table shuttleLocations
-- --
-- ALTER TABLE shuttleLocations
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table Standups
-- --
-- ALTER TABLE Standups
--   ADD PRIMARY KEY (recNum);

-- --
-- -- Indexes for table stopsTable
-- --
-- ALTER TABLE stopsTable
--   ADD UNIQUE KEY id (id);

-- --
-- -- Indexes for table TestNulls
-- --
-- ALTER TABLE TestNulls
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table TESTtimes
-- --
-- ALTER TABLE TESTtimes
--   ADD PRIMARY KEY (hoursID),
--   ADD KEY id (id);

-- --
-- -- Indexes for table times
-- --
-- ALTER TABLE times
--   ADD PRIMARY KEY (hoursID),
--   ADD KEY id (id);

-- --
-- -- Indexes for table updateTimes
-- --
-- ALTER TABLE updateTimes
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table vehicleNames
-- --
-- ALTER TABLE vehicleNames
--   ADD PRIMARY KEY (vehicleIndex),
--   ADD UNIQUE KEY name (name);

-- --
-- -- Indexes for table weather
-- --
-- ALTER TABLE weather
--   ADD PRIMARY KEY (id);

-- --
-- -- Indexes for table ZToDo
-- --
-- ALTER TABLE ZToDo
--   ADD PRIMARY KEY (recId),
--   ADD UNIQUE KEY recId (recId);

-- --
-- -- AUTO_INCREMENT for dumped tables
-- --

-- --
-- -- AUTO_INCREMENT for table athletics
-- --
-- ALTER TABLE athletics
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table buildingHours
-- --
-- ALTER TABLE buildingHours
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table buildingLocations
-- --
-- ALTER TABLE buildingLocations
--   MODIFY buildingID INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table BusStops
-- --
-- ALTER TABLE BusStops
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table clps
-- --
-- ALTER TABLE clps
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table contacts
-- --
-- ALTER TABLE contacts
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table DHmenu
-- --
-- ALTER TABLE DHmenu
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table foodService
-- --
-- ALTER TABLE foodService
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table FU20_RestaurantHours
-- --
-- ALTER TABLE FU20_RestaurantHours
--   MODIFY hoursID INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table GolfPlayers
-- --
-- ALTER TABLE GolfPlayers
--   MODIFY rec INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table GolfRounds
-- --
-- ALTER TABLE GolfRounds
--   MODIFY rec INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table GolfSchedule
-- --
-- ALTER TABLE GolfSchedule
--   MODIFY rec INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table healthSafety
-- --
-- ALTER TABLE healthSafety
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table importantDates
-- --
-- ALTER TABLE importantDates
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table importantLinks
-- --
-- ALTER TABLE importantLinks
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table newsContent
-- --
-- ALTER TABLE newsContent
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table newsPublishers
-- --
-- ALTER TABLE newsPublishers
--   MODIFY publisherID INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table parkingResources
-- --
-- ALTER TABLE parkingResources
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table parkingZones
-- --
-- ALTER TABLE parkingZones
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table restaurantMenu
-- --
-- ALTER TABLE restaurantMenu
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table shuttleLocations
-- --
-- ALTER TABLE shuttleLocations
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table Standups
-- --
-- ALTER TABLE Standups
--   MODIFY recNum INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table stopsTable
-- --
-- ALTER TABLE stopsTable
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table TestNulls
-- --
-- ALTER TABLE TestNulls
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table TESTtimes
-- --
-- ALTER TABLE TESTtimes
--   MODIFY hoursID INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table times
-- --
-- ALTER TABLE times
--   MODIFY hoursID INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table updateTimes
-- --
-- ALTER TABLE updateTimes
--   MODIFY id INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- AUTO_INCREMENT for table vehicleNames
-- --
-- ALTER TABLE vehicleNames
--   MODIFY vehicleIndex INTEGER PRIMARY KEY AUTOINCREMENT,;
-- --
-- -- Constraints for dumped tables
-- --

