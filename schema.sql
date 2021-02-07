drop table if exists forum;
	create table forum (
		id integer primary key autoincrement,
		fname text not null,
		lname text not null,
		phonenum text not null,
		email text not null,
		dd date not null
);
