from __future__ import annotations

import time

from pymongo import MongoClient


class Logger:
    def __init__(self, db: MongoClient):
        self.db = db

    def log(self, msg: str, type: str = "info") -> None:
        """
        Log simply logs a message to the console


        :param msg:
        :type msg:
        :param type:
        :type type:
        :return:
        :rtype:
        """
        print(f"[{time.time()}] [{type.upper()}] {msg}")

    def event(self, msg_or_data: str | dict, event: str, type: str = "info", meta: dict = {}) -> None:
        """
        Events are saved to the database

        database : Events
        collection: event param

        :param msg:
        :type msg:
        :param event:
        :type event:
        :param type:
        :type type:
        :return:
        :rtype:
        """

        print(f"[{time.time()}] [{type.upper()}] [{event.upper()}] {str(msg_or_data)}")
        self.db["events"][event].insert_one({
            "data": msg_or_data,
            "meta": {},
            "createdAt": int(time.time())
        })
