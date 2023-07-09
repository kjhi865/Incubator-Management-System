
DROP DATABASE IF EXISTS incub;

CREATE DATABASE incub;
USE incub;

DROP TABLE IF EXISTS `EMPLOYEE`;
CREATE TABLE `EMPLOYEE` (
  `EmployeeID` int(11) NOT NULL,
  `EmployeeName` varchar(100) NOT NULL,
  `EmployeeDept` varchar(50) NOT NULL,
  `EmployeeSalary` int(11) NOT NULL,
  `EmployeeSex` varchar(15) NOT NULL,
  `ResourceID` int(11) DEFAULT NULL,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `EMPLOYEE` VALUES (57,'Rajesh','HR',50000,'Male',101),(91,'Ramesh','Sales',20000,'Male',102),
(123,'Rita','Finance',100000,'Female',103);
/******************************************************************************************************************/
/******************************************************************************************************************/

DROP TABLE IF EXISTS `INDUSTRY`;
CREATE TABLE `INDUSTRY` (
  `IndustryID` int(11) NOT NULL,
  `IndustryName` varchar(100) NOT NULL,
  `IndustryType` varchar(100) NOT NULL,
  PRIMARY KEY (`IndustryID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `INDUSTRY` VALUES (1,'Transportation','Tertiary'),(2,'Textile','Secondary'),(3,'Agriculture','Primary'),(4,'Horticulture','Primary'),(5,'IT','Tertiary');

/******************************************************************************************************************/
/******************************************************************************************************************/

DROP TABLE IF EXISTS `LOCATION`;
CREATE TABLE `LOCATION` (
  `Pincode` int(11) NOT NULL,
  `City` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  PRIMARY KEY (`Pincode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `LOCATION` VALUES (250001,'Meerut','India'),(400094,'Mumbai','India'),(500032,'Hyderabad','India')
,(710094,'Hyderabad','Pakistan');

/******************************************************************************************************************/
/******************************************************************************************************************/

DROP TABLE IF EXISTS `RESOURCE`;
CREATE TABLE `RESOURCE` (
  `ResourceID` int(11) NOT NULL,
  `ResourceValue` int(11) NOT NULL,
  `ResourceType` varchar(100) NOT NULL,
  PRIMARY KEY (`ResourceID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/******************************************************************************************************************/
/******************************************************************************************************************/


INSERT INTO `RESOURCE` VALUES (101,1000000,'Capital'),(102,50000,'Workspaces'),(103,50000,'Computers'),(104,10000,'Manufacturing Space');
DROP TABLE IF EXISTS `STARTUP`;
CREATE TABLE `STARTUP` (
  `StartupID` int(11) NOT NULL,
  `StartupName` varchar(50) NOT NULL,
  `NoofEmployees` int(11) NOT NULL,
  `Networth` int(11) NOT NULL,
  `ResourceID` int(11) ,
  PRIMARY KEY (`StartupID`),
 /*added */ FOREIGN KEY (`ResourceID`) REFERENCES RESOURCE(`ResourceID`) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/******************************************************************************************************************/
/******************************************************************************************************************/


INSERT INTO `STARTUP` VALUES (1,'Dream View',100,1000000,  101),(2,'Ober Cab Services',200,200000,102);

DROP TABLE IF EXISTS `STARTUP_FOUNDERS`;
CREATE TABLE `STARTUP_FOUNDERS` (
  `StartupID` int(11) NOT NULL,
  `Founder` varchar(50) NOT NULL,
  PRIMARY KEY (`StartupID`,`Founder`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `STARTUP_FOUNDERS` VALUES (1,'Ahish Deshpande'),(1,'Utkarsh Mishra'),(2,'Trunapushpa'),(2,'Yoogottam');

DROP TABLE IF EXISTS `BASED_IN`;

CREATE TABLE `BASED_IN` (
  `StartupID` int(11) NOT NULL,
  `LocationID` int(11) NOT NULL,
  PRIMARY KEY (`StartupID`,`LocationID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`LocationID`) REFERENCES LOCATION(`Pincode`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `BASED_IN` VALUES (1,400094),(1,500032),(2,250001);

DROP TABLE IF EXISTS `DIRECTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DIRECTOR` (
  `Name` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `Sex` varchar(20) NOT NULL,
  `Experience` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`StartupID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


LOCK TABLES `DIRECTOR` WRITE;
INSERT INTO `DIRECTOR` VALUES ('Kamal',1,'Male',10),('Nonidh',2,'Male',2);
DROP TABLE IF EXISTS `DIRECTOR_EDUCATION`;
CREATE TABLE `DIRECTOR_EDUCATION` (
  `Name` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `Degree` varchar(50) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `Year` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`StartupID`,`Degree`,`Branch`,`Year`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
 /*added */ FOREIGN KEY (`Name`) REFERENCES DIRECTOR(`Name`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `DIRECTOR_EDUCATION` VALUES ('Kamal',1,'B.Tech','Computer Science',1990),('Kamal',1,'PhD','Computer Science',2000),('Nonidh',2,'B.Tech','Computer Science',2010),('Nonidh',2,'M.Sc','Natural Sciences',2015);



DROP TABLE IF EXISTS `INVESTOR`;
CREATE TABLE `INVESTOR` (
  `InvestorID` int(11) NOT NULL,
  `DOB` date NOT NULL,
  `Sex` varchar(50) NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `LocationID` int(11) ,
  PRIMARY KEY (`InvestorID`),
 /*added */ FOREIGN KEY (`LocationID`) REFERENCES LOCATION(`Pincode`) ON UPDATE CASCADE ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `INVESTOR` VALUES (1,'1990-07-10','Male','Shyam','Gopal',250001),(2,'1991-05-02','Female','Rama','Dewam',400094),(3,'1992-03-29','Male','Anubhav','Trump',710094);

DROP TABLE IF EXISTS `INVESTOR_EDUCATION`;
CREATE TABLE `INVESTOR_EDUCATION` (
  `InvestorID` int(11) NOT NULL,
  `Degree` varchar(50) NOT NULL,
  `Branch` varchar(50) NOT NULL,
  `Year` int(11) NOT NULL,
  PRIMARY KEY (`InvestorID`,`Degree`,`Branch`,`Year`),
 /*added*/ FOREIGN KEY (`InvestorID`) REFERENCES INVESTOR(`InvestorID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `INVESTOR_EDUCATION` VALUES (1,'B.Tech','Computer Science',1990),(1,'PhD','Computer Science',2000),(2,'B.Tech','Computer Science',2010),(3,'B.Sc','Aeronautical Science',2015);

DROP TABLE IF EXISTS `INVESTS`;
CREATE TABLE `INVESTS` (
  `IndustryID` int(11) NOT NULL ,
  `InvestorID` int(11) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `ResourceID` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  PRIMARY KEY (`IndustryID`,`InvestorID`,`StartupID`,`ResourceID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`IndustryID`) REFERENCES INDUSTRY(`IndustryID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`InvestorID`) REFERENCES INVESTOR(`InvestorID`) ON UPDATE CASCADE ON DELETE CASCADE,
 /*added */ FOREIGN KEY (`ResourceID`) REFERENCES RESOURCE(`ResourceID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `INVESTS` VALUES (1,2,1,101,'2008-01-09'),(2,1,1,101,'2008-01-09'),(2,3,2,102,'2010-10-10');

DROP TABLE IF EXISTS `PROJECT`;
CREATE TABLE `PROJECT` (
  `ProjectName` varchar(50) NOT NULL,
  `StartupID` int(11) NOT NULL,
  `TimeFrame` int(11) NOT NULL,
  `StartDate` date NOT NULL,
  `NoofEmployees` int(11) NOT NULL,
  PRIMARY KEY (`ProjectName`,`StartupID`),
 /*added */ FOREIGN KEY (`StartupID`) REFERENCES STARTUP(`StartupID`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `PROJECT` VALUES ('AlphaQ',1,200,'2010-10-10',32),('BetaG',2,100,'2000-10-20',25);

