INSERT INTO specialization (id, name) VALUES 
(1, 'General'), 
(2, 'Electrical'), 
(3, 'Computer'), 
(4, 'Archtecture'), 
(5, 'Communication'), 
(6, 'Mechanical'), 
(7, 'Civil');

INSERT INTO section (id, name) VALUES 
(1,'1SC1'),
(2,'1SC2'),
(3,'1SC3'),
(4,'1SC4'),
(5,'1SC5'),
(6,'2M1'), 
(7,'2M2'),
(8,'2M3'),
(9,'2M4'), 
(10,'2M5'),
(11,'2V1'), 
(12,'2V2'),
(13,'2V3'),
(14,'2V4'), 
(15,'2V5'),
(16,'2A1'), 
(17,'2A2'),
(18,'2A3'),
(19,'2A4'), 
(20,'2A5'),
(21,'2L1'), 
(22,'2L2'),
(23,'2L3'),
(24,'2L4'), 
(25,'2L5'),
(26,'3C1'), 
(27,'3C2'), 
(28,'3C3'), 
(29,'3C4'), 
(30,'3C5'),
(31,'3M1'),
(32,'3M2'),
(33,'3M3'),
(34,'3M4'),
(35,'3M5'),
(36,'3V1'),
(37,'3V2'),
(38,'3V3'),
(39,'3V4'),
(40,'3V5'),
(41,'3A1'),
(42,'3A2'),
(43,'3A3'),
(44,'3A4'),
(45,'3A5'),
(46,'3L1'), 
(47,'3L2'),
(48,'3L3'),
(49,'3L4'), 
(50,'3L5'),
(51,'4C1'), 
(52,'4C2'), 
(53,'4C3'), 
(54,'4C4'), 
(55,'4C5'),
(56,'4M1'),
(57,'4M2'),
(58,'4M3'),
(59,'4M4'),
(60,'4M5'),
(61,'4V1'),
(62,'4V2'),
(63,'4V3'),
(64,'4V4'),
(65,'4V5'),
(66,'4A1'),
(67,'4A2'),
(68,'4A3'),
(69,'4A4'),
(70,'4A5'),
(71,'4L1'), 
(72,'4L2'),
(73,'4L3'),
(74,'4L4'), 
(75,'4L5'),
(76,'5C1'), 
(77,'5C2'), 
(78,'5C3'), 
(79,'5C4'), 
(80,'5C5'),
(81,'5M1'),
(82,'5M2'),
(83,'5M3'),
(84,'5M4'),
(85,'5M5'),
(86,'5V1'),
(87,'5V2'),
(88,'5V3'),
(89,'5V4'),
(90,'5V5'),
(91,'5A1'),


INSERT INTO courses (id, name, code) VALUES
(1, 'Information Systems', 'CMPN345' ),
;

INSERT INTO student (id, name, email, address, phone, gender, date_of_birth, logincode, specialization_id, section_id) VALUES 
(1, 'John Isaac', 'johnisaac@gmail.com', 'Beni Suef', '+20 120 531 0694','Male', '2000-10-07', 'S0001', 3, 28),

;


INSERT INTO staff (id, name, email, address, phone, gender,job, date_of_birth, logincode) VALUES 
(1, 'Khaled Morsy', 'kahledmorsy@gmail.com', 'Menia', '+20 112 654 8495','Male', 'Doctor', '1960-11-08','D0001'),
;


INSERT INTO student_courses(student_id, course_id) VALUES
(1,1),
(1,2),
;


INSERT INTO staff_courses(courses_id, staff_id) VALUES
(1,1),
(2,3),
;


INSERT INTO data (id, name, short_description, , description, link, type, course_id, staff_id) VALUES 
(1, 'Chapter 1', 'This is a short introduction to Information Systems', 'Information Systems is responsible for a lot of things around us', '','document', 1, 1),
;
