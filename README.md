# Overview

The created service will simulate a robot moving in an office space
and will be cleaning the places this robot visits. The path of the robot's movement is
described by the starting coordinates and move commands. After the cleaning has
been done, the robot reports the number of unique places cleaned. The service will
store the results into the database and return the created record in JSON format. The
service listens to HTTP protocol on port 5000.

## Requirements
- docker/podman compose should already be installed. 
Both can be used interchangebly.

## Usage
Database is initialized when the project is run for the first time. 

example .env variable
```
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB
```

```
docker compose up
```
or 
```
podman compose up
```

Then, you should call the endpoint with post request.
```
Example:
   curl -X POST -H "Content-Type: application/json" -d ' {
   "start":{
      "x":10,
      "y":22
   },
   "commands":[
      {
         "direction":"east",
         "steps":2
      },
      {
         "direction":"north",
         "steps":1
      }
   ]
}' <endpoint-url>

After issuing the command, this service calculates the total number of unique places that are cleaned, and gives the result back. It also saves the result into the "cleaning_report" table in Postgres.

```
In order to run the tests:
´´´pytest --v ´´´

## Future Work
If I had more time, I would work on:
- The exceptions. Because they are too general, I should make them more specific.
- The certificates, authentication, and rate limiting to secure the endpoint...
- Integration tests...
