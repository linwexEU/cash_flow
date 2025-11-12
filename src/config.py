import os
from typing import Literal

from dotenv import find_dotenv, load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_dir)

load_dotenv(find_dotenv(".env"))


class Settings: 
    MODE: Literal["DEV", "TEST"] = os.environ.get("MODE")

    DB_NAME: str = os.environ.get("DB_NAME") 
    TEST_DB_NAME: str = os.environ.get("TEST_DB_NAME")

    DB_URL: str = f"sqlite+aiosqlite:///{DB_NAME}.sqlite"
    TEST_DB_URL: str = f"sqlite+aiosqlite:///{TEST_DB_NAME}.sqlite"


settings = Settings() 
