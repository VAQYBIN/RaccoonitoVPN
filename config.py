from dataclasses import dataclass
from typing import List
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str
    admins: List[int]


def load_config() -> Config:
    return Config(
        bot_token=os.getenv("BOT_TOKEN", ""),
        admins=[int(x) for x in os.getenv("ADMINS_IDS", "").split(",") if x]
    )
