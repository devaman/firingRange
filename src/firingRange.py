import asyncio
from src.server.server import server
import src.config as config

class firingRange:
    def __init__(self):
        pass

    def run(self):
        asyncio.run(server())
