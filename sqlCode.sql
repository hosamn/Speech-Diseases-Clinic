CREATE TABLE `patient` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`name`	TEXT NOT NULL UNIQUE,
	`dobDay`	INTEGER,
	`dobMonth`	INTEGER,
	`dobYear`	INTEGER,
	`sex`	TEXT,
	`nationality`	TEXT,
	`marital`	TEXT,
	`job`	TEXT,
	`address`	TEXT,
	`phoneMobile`	TEXT,
	`phoneHome`	TEXT,
	`phoneWork`	TEXT,
	`referrer`	TEXT
);



CREATE TABLE `test` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`patientID`	INTEGER NOT NULL,
	`dateDay`	INTEGER,
	`dateMonth`	INTEGER,
	`dateYear`	INTEGER,
	`hospital`	TEXT,
	`endoscope`	TEXT,
	`diag`	TEXT,
	`hist`	TEXT,
	`pasTG`	TEXT,
	`pasTB`	TEXT,
	`pasNG`	TEXT,
	`pasNB`	TEXT,
	`pasHG`	TEXT,
	`pasHB`	TEXT,
	`pasPG`	TEXT,
	`pasPB`	TEXT,
	`pasMG`	TEXT,
	`pasMB`	TEXT,
	`pasSG`	TEXT,
	`pasSB`	TEXT,
	`residue`	TEXT,
	`others`	TEXT,
	`recomm`	TEXT

);



