"""
    This file contains the core logic of how to move between vertices in the office,
        constructs the record to be inserted into the database.
"""
import time

from api.model import Path, Result, insert_into_db
from common.utils import get_duration, get_timestamp


def move_accross_the_path(path: Path) -> Result:
    """
        Robot executes the commands in the given direction.
        Args:
            path: Path, entered path to the endpoint
        Returns:
            {
                "timestamp": date of the execution,
                "command": number of commands sent to the robot,
                "result": number of unique places which are cleaned by the robot,
                "duration": total duration of the execution.
            }
    """
    try:
        start_time = time.time()
        furthest_west, furthest_east, furthest_south, furthest_north = path.start.x, path.start.x, path.start.y, path.start.y
        last_visited_coord = (path.start.x, path.start.y)
        for command in path.commands:
            x, y = last_visited_coord
            if command.direction == "east":
                last_visited_coord = (x+command.steps, y)
                furthest_east = max(furthest_east, x+command.steps)
            if command.direction =="west":
                last_visited_coord = (x-command.steps, y)
                furthest_west = min(furthest_west, x-command.steps)
            if command.direction == "north":
                last_visited_coord = (x, y+command.steps)
                furthest_north = max(furthest_north, y+command.steps)
            if command.direction == "south": 
                last_visited_coord = (x, y-command.steps)
                furthest_south = min(furthest_south, y-command.steps)
            
        cleaned_locs = abs(furthest_east - furthest_west) + abs(furthest_north - furthest_south)
        end_time = time.time()

        record = {
            "timestamp":get_timestamp(),
            "command":len(path.commands),
            # Adds the starting location as (+1).
            "result": cleaned_locs + 1,
            "duration":get_duration(start_time, end_time)
        }

        insert_into_db(record)
        return Result(**record)
    
    except Exception as e:
        raise Exception(e)