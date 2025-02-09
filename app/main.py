import logging
import pathlib
from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config_manager import ConfigManager
from app.core.log_manager import LogManager

from app.core.db.db_manager import DBManager

logger = logging.getLogger(__name__)


confFilePath = pathlib.Path.cwd() / "app" / "conf" / "config.ini"

configManager = ConfigManager()

LogManager(configManager)
logger.info("Starting app")

logger.info(f"Config manager init successful with config file {confFilePath}")
logger.info("Logger manager init successful")


class Hello(BaseModel):
    message: str


app = FastAPI()

# This is for when we will need to store information the database
dbManager = DBManager(configManager)
logger.info("DB manager init succesful")


@app.get("/")
async def show_welcome_page():
    message = {
        "Message": "Welcome to your own API ! It is kind of empty don't you think ? Why don't you try adding an /health !"
    }
    return message


# add your /health here, reload and make the /health return ok !


@app.get("/getAllStudents")
async def get_all_students():
    all_students = dbManager.getAllStudents()
    return all_students
