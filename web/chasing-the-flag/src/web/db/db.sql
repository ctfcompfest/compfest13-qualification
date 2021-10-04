CREATE TABLE teamdata (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(25) NOT NULL,
    points INT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE teamcreds (
    id INT NOT NULL,
    username VARCHAR(25) NOT NULL,
    password VARCHAR(25) NOT NULL,
    winner BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES teamdata(id)
);

INSERT INTO teamdata (name, points)
    VALUES ('aebeceh', 10000),
    ('Divide et Conquer', 9000),
    ('Receh abesssss', 8000),
    ('UwU', 7000),
    ('The triad', 6000),
    ('Alpha', 7500),
    ('Charlie', 9500),
    ('YEET', 12500),
    ('Wait, whut', 20000);

INSERT INTO teamcreds VALUES
    (1, 'aebeceh', 'abcabcabc', 0),
    (2, 'DivideetConquer', 'hahahihihehe', 0),
    (3, 'Recehabesssss', '4p4l0l14tl14t', 0),
    (4, 'UwU', 'UwawUwu890', 0),
    (5, 'Thetriad', 'OneTwoDreiForFive', 0),
    (6, 'Alpha', 'YEEAAHHBOOII111', 0),
    (7, 'Charlie', 'HOWlittleratstolethe3333', 0),
    (8, 'YEET', 'Taaaan9999', 0),
    (9, 'Waitwhut', 'Th1sIsN0tPl41nT3xtRight?', 1);
