CREATE DATABASE IF NOT EXISTS lab5ece140a;

USE lab5ece140a;

CREATE TABLE IF NOT EXISTS Commands (
  id         int AUTO_INCREMENT PRIMARY KEY,
  message    VARCHAR(32) NOT NULL,
  completed  boolean DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS Telemetry;

-- CREATE TABLE Telemetry to store Telemetry data here
-- Call it "Telemetry"!!!

CREATE TABLE IF NOT EXISTS Telemetry (
  id         int AUTO_INCREMENT PRIMARY KEY,
  pitch      int,
  roll       int,
  yaw        int,
  vgx        int,
  vgy        int,
  vgz        int,
  templ      int,
  temph      int,
  tof        int,
  h          int,
  bat        int,
  baro       double,
  time       int,
  agx        double,
  agy        double,
  agz        double, 
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);