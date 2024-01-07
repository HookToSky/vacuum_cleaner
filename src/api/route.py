from fastapi import APIRouter, HTTPException

from src.api.model import Result, Path
from src.api.service import generate_cleaning_report

developer_test = APIRouter(prefix="/tibber-developer-test")


@developer_test.post("/enter-path/")
def clean_given_path(path: Path) -> Result:
    """ Args:
            path: Path, gets the path from the request body, and transforms it into a Path Object.
        Returns:
          Inserted record into the database as a reference, and simplicity (no need to query the db).
    """
    try:
       response: Result = generate_cleaning_report(path)
       return response
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Something went wrong!"
        )
