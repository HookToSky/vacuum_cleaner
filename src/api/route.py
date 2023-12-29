from fastapi import APIRouter, HTTPException

from api.model import Result, Path
from api.service import move_accross_the_path

developer_test = APIRouter(prefix="/tibber-developer-test")


@developer_test.post("/enter-path/")
def clean_given_path(path: Path) -> Result:
    """ Args:
            path: Path, gets the path from the request body, and transforms it into a Path Object.
        Returns:
          Inserted record into the database as a reference, and simplicity (no need to query the db).
    """
    try:
       response: Result = move_accross_the_path(path)
       return response
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Something went wrong!"
        )
