from common.db_conn import conn
from datetime import datetime
from pydantic import BaseModel


class Start(BaseModel):
    x: int
    y: int


class Command(BaseModel):
    direction: str
    steps: int


class Path(BaseModel):
    start: Start
    commands: list[Command]


class Result(BaseModel):
    timestamp: datetime
    command: int
    result: int
    duration: float


def insert_into_db(result: dict):
    """
        Args:
            result: Dict, record to be inserted into the database table.
    """
     
    with conn:
        cur = conn.cursor()
        cur.execute("""INSERT INTO cleaning_report 
                        (timestamp, commands, result, duration) VALUES (%s, %s, %s, %s)""", 
                    (result['timestamp'], result['command'], result['result'], result['duration']))
        conn.commit()
        cur.close()