# Copyright (C) 2020-2021 by KashDaYash@Github, < https://github.com/KashDaYash >.
#
# This file is part of < https://github.com/XeroOP/YaaraBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/XeroOP/YaaraBot/blob/master/LICENSE >
#
# All rights reserved.

from . import cli
import asyncio

collection = cli["Yaara"]["afk"]


async def set_afk(afk_status, afk_since, reason):
    doc = {"_id": 1, "afk_status": afk_status}
    r = await collection.find_one({"_id": 1})
    if r:
        await collection.update_one(
            {"_id": 1},
            {
                "$set": {
                    "afk_status": afk_status,
                    "afk_since": afk_since,
                    "reason": reason,
                }
            },
        )
    else:
        await collection.insert_one(doc)


async def set_unafk():
    await collection.update_one(
        {"_id": 1}, {"$set": {"afk_status": False, "afk_since": None, "reason": None}}
    )


async def get_afk_status():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    else:
        status = result["afk_status"]
        return status


async def afk_stuff():
    result = await collection.find_one({"_id": 1})
    afk_since = result["afk_since"]
    reason = result["reason"]
    return afk_since, reason
