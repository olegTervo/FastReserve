
CREATE TABLE IF NOT EXISTS Users (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(128) NOT NULL,
	secondName VARCHAR(128) NOT NULL,
	email VARCHAR(128) NOT NULL,
	phoneNumber BIGINT,
	password TEXT NOT NULL,
	isModerator BIT
);


CREATE TABLE IF NOT EXISTS Item (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(128) NOT NULL,
	type INT,
	isPublic BIT,
	info TEXT,
	author SERIAL,
	FOREIGN KEY (author) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS ItemType (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(128) NOT NULL
);

INSERT INTO ItemType (id, name)
values (0, 'Undefined'),
(1, 'Väline'),
(2, 'Ajoneuvo'),
(3, 'Pinta ala'),
(4, 'Palvelu'),
(5, 'Muu tyyppi');

ALTER TABLE Item
ADD FOREIGN KEY (type) 
REFERENCES ItemType(id);

CREATE TABLE IF NOT EXISTS Channel (
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(128) NOT NULL,
	author SERIAL NOT NULL
);

CREATE TABLE IF NOT EXISTS ChannelItem (
	item_id SERIAL,
	channel_id SERIAL,
	CONSTRAINT PK PRIMARY KEY (item_id,channel_id),
	FOREIGN KEY (item_id) REFERENCES Item(id),
	FOREIGN KEY (channel_id) REFERENCES Channel(id)
);

CREATE TABLE IF NOT EXISTS ChannelUser (
	user_id SERIAL,
	channel_id SERIAL,
	isAdmin BIT,
	isBanned BIT
);
  
