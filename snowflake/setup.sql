CREATE DATABASE IF NOT EXISTS HERO_DB;
USE DATABASE HERO_DB;
USE SCHEMA PUBLIC;

-- Table for tourism stats
CREATE OR REPLACE TABLE tourism_stats (
    state_name STRING,
    visitors INT,
    month STRING,
    category STRING, -- 'Domestic' or 'Foreign'
    year INT
);

-- Create table for cultural sites
CREATE OR REPLACE TABLE cultural_sites (
    SITE_ID VARCHAR(10),
    NAME VARCHAR(100),
    REGION VARCHAR(50),
    ART_TYPE VARCHAR(50),
    DESCRIPTION TEXT,
    LATITUDE FLOAT,
    LONGITUDE FLOAT
);

-- Create table for yearly tourism trends
CREATE TABLE yearly_tourism (
    STATE_NAME VARCHAR(50),
    YEARLY_VISITORS INT,
    YEAR INT,
    CATEGORY VARCHAR(20)
);

-- Sample insert (you can add more from actual data)
INSERT INTO cultural_sites (site_id, name, region, art_type, description) VALUES
('S001', 'Kathakali Dance', 'Kerala', 'Performing Arts', 'A traditional dance-drama from Kerala with elaborate costumes.'),
('S002', 'Ajanta Caves', 'Maharashtra', 'Architecture', 'Rock-cut Buddhist cave monuments dating back to the 2nd century BCE.');

INSERT INTO tourism_stats (state_name, visitors, month, category, year) VALUES
-- Kerala
('Kerala', 120000, 'January', 'Domestic', 2024),
('Kerala', 30000, 'January', 'Foreign', 2024),
('Kerala', 100000, 'February', 'Domestic', 2024),
('Kerala', 28000, 'February', 'Foreign', 2024),

-- Rajasthan
('Rajasthan', 150000, 'January', 'Domestic', 2024),
('Rajasthan', 50000, 'January', 'Foreign', 2024),
('Rajasthan', 130000, 'February', 'Domestic', 2024),
('Rajasthan', 47000, 'February', 'Foreign', 2024),

-- Assam
('Assam', 80000, 'January', 'Domestic', 2024),
('Assam', 10000, 'January', 'Foreign', 2024),
('Assam', 75000, 'February', 'Domestic', 2024),
('Assam', 9000, 'February', 'Foreign', 2024),

-- Additional March Data
('Kerala', 95000, 'March', 'Domestic', 2024),
('Kerala', 25000, 'March', 'Foreign', 2024),
('Rajasthan', 110000, 'March', 'Domestic', 2024),
('Rajasthan', 40000, 'March', 'Foreign', 2024),
('Assam', 72000, 'March', 'Domestic', 2024),
('Assam', 8000, 'March', 'Foreign', 2024);

-- Insert data into yearly_tourism
INSERT INTO yearly_tourism (STATE_NAME, YEARLY_VISITORS, YEAR, CATEGORY) VALUES
('Kerala', 800000, 2020, 'Domestic'),
('Kerala', 200000, 2020, 'Foreign'),
('Kerala', 400000, 2021, 'Domestic'),
('Kerala', 40000, 2021, 'Foreign'),
('Kerala', 520000, 2022, 'Domestic'),
('Kerala', 44000, 2022, 'Foreign'),
('Rajasthan', 1000000, 2020, 'Domestic'),
('Rajasthan', 400000, 2020, 'Foreign'),
('Rajasthan', 500000, 2021, 'Domestic'),
('Rajasthan', 80000, 2021, 'Foreign'),
('Rajasthan', 650000, 2022, 'Domestic'),
('Rajasthan', 88000, 2022, 'Foreign'),
('Assam', 500000, 2020, 'Domestic'),
('Assam', 80000, 2020, 'Foreign'),
('Assam', 250000, 2021, 'Domestic'),
('Assam', 16000, 2021, 'Foreign'),
('Assam', 325000, 2022, 'Domestic'),
('Assam', 17600, 2022, 'Foreign');