GRANT ALL PRIVILEGES ON DATABASE tibber_app TO tibber;

CREATE TABLE IF NOT EXISTS cleaning_report (
    id serial NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    commands int NOT NULL,
    result int NOT NULL,
    duration decimal NOT NULL,
    PRIMARY KEY (id)
);