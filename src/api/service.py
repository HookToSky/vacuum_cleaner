"""
    This file contains the core logic of how to move between vertices in the office,
        constructs the record to be inserted into the database.
"""
import time

from src.api.model import Path, Result, insert_into_db, Coordinates, Command, FurthestByDirection
from src.common.utils import get_duration, get_timestamp


def process_command(command: Command, visited: FurthestByDirection, last_visited_loc: Coordinates):
    """
        Robot executes the commands in the given direction by updating the visited furthest locations.
        Args:
            command: given command by the user in Path.
            visited: furthest visited location on the map in all directions up to now.
            last_visited_loc: last visited coordinate.
        Returns:
            last_visited_loc: Updated last visited coordinates.
            visited: Updated furthest visited locations in all directions.
    """
    x, y = last_visited_loc
    if command.direction == "east":
        last_visited_loc = (x+command.steps, y)
        visited.furthest_east = max(visited.furthest_east, x+command.steps)
    elif command.direction == "west":
        last_visited_loc = (x-command.steps, y)
        visited.furthest_west = min(visited.furthest_west, x-command.steps)
    elif command.direction == "north":
        last_visited_loc = (x, y+command.steps)
        visited.furthest_north = max(visited.furthest_north, y+command.steps)
    else: 
        last_visited_loc = (x, y-command.steps)
        visited.furthest_south = min(visited.furthest_south, y-command.steps)

    return last_visited_loc, visited


def generate_cleaning_report(path: Path) -> Result:
    """
        Robot cleans all the unique locations by series of commands in the given path.
        Args:
            path: Path, entered path by the user
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
        visited_so_far = FurthestByDirection(**{
            "furthest_east": path.start.x, 
            "furthest_west": path.start.x, 
            "furthest_south": path.start.y, 
            "furthest_north": path.start.y
            })
        last_visited_coord = (path.start.x, path.start.y)
        for command in path.commands:
          last_visited_coord, visited_so_far = process_command(command, visited_so_far, last_visited_coord)

        unique_cleaned_locs = abs(visited_so_far.furthest_east - visited_so_far.furthest_west) + abs(visited_so_far.furthest_north - visited_so_far.furthest_south)
        end_time = time.time()

        record = {
            "timestamp":get_timestamp(),
            "command":len(path.commands),
            # Adds the starting location as (+1).
            "result": unique_cleaned_locs + 1,
            "duration":get_duration(start_time, end_time)
        }

        insert_into_db(record)
        return Result(**record)
    
    except Exception as e:
        raise Exception(e)