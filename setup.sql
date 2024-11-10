PRAGMA foreign_keys = ON;

-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    usr INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    pwd TEXT NOT NULL
);

-- Create Follows table
CREATE TABLE IF NOT EXISTS follows (
    flwer INTEGER,
    flwee INTEGER,
    start_date TEXT,
    FOREIGN KEY(flwer) REFERENCES users(usr),
    FOREIGN KEY(flwee) REFERENCES users(usr)
);

-- Create Lists table
CREATE TABLE IF NOT EXISTS lists (
    owner_id INTEGER,
    lname TEXT,
    PRIMARY KEY (owner_id, lname),
    FOREIGN KEY(owner_id) REFERENCES users(usr)
);

-- Create Include table
CREATE TABLE IF NOT EXISTS include (
    owner_id INTEGER,
    lname TEXT,
    tid INTEGER,
    FOREIGN KEY(owner_id) REFERENCES users(usr),
    FOREIGN KEY(tid) REFERENCES tweets(tid)
);

-- Create Tweets table
CREATE TABLE IF NOT EXISTS tweets (
    tid INTEGER PRIMARY KEY AUTOINCREMENT,
    writer_id INTEGER,
    text TEXT,
    tdate TEXT,
    ttime TEXT,
    replyto_tid INTEGER,
    FOREIGN KEY(writer_id) REFERENCES users(usr),
    FOREIGN KEY(replyto_tid) REFERENCES tweets(tid)
);

-- Create Retweets table
CREATE TABLE IF NOT EXISTS retweets (
    tid INTEGER,
    retweeter_id INTEGER,
    writer_id INTEGER,
    spam INTEGER,
    rdate TEXT,
    PRIMARY KEY(tid, retweeter_id),
    FOREIGN KEY(tid) REFERENCES tweets(tid),
    FOREIGN KEY(retweeter_id) REFERENCES users(usr),
    FOREIGN KEY(writer_id) REFERENCES users(usr)
);

-- Create Hashtag Mentions table
CREATE TABLE IF NOT EXISTS hashtag_mentions (
    tid INTEGER,
    term TEXT,
    FOREIGN KEY(tid) REFERENCES tweets(tid)
);
