CREATE ROLE tasktracker WITH ENCRYPTED PASSWORD 'password' LOGIN CREATEDB;
COMMENT ON ROLE tasktracker IS 'tasktracker database maintenance role';

CREATE DATABASE tasktracker OWNER tasktracker;
COMMENT ON DATABASE tasktracker IS 'tasktracker project database';
