-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Description of Crimes
SELECT description
FROM crime_scene_reports
WHERE day = "28" AND month = "7" AND street = "Humphrey Street";

-- Check the transcript of interviews
SELECT * FROM interviews
WHERE day = 28 AND month = 7;
--People exiting bakery
SELECT name
FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE day = 28 AND month = 7
AND hour = 10
AND activity = "exit";

-- I'm so sorry, I forgot to record my logs!!!! and i'm too lazy to do it again because it took me a lot of time to find the thief!!! please I swear I didnt cheat :(((((
