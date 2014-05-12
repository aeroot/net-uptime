CREATE TABLE uptimelog (
	time DATETIME NOT NULL PRIMARY KEY,
	router BOOL,
	carrier_router BOOL,
	internet BOOL
);