GRANT ALL PRIVILEGES ON DATABASE app TO postgres;

CREATE TABLE IF NOT EXISTS cleaning_report (
    id serial NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    commands int NOT NULL,
    result int NOT NULL,
    duration decimal NOT NULL,
    PRIMARY KEY (id)
);