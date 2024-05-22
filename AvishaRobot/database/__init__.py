

from async_pymongo import AsyncClient

from AvishaRobot import MONGO_DB_URI

DBNAME = "AvishaRobot"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
