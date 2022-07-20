# Copyright (C) 2020-2021 by KashDaYash@Github, < https://github.com/KashDaYash >.
#
# This file is part of < https://github.com/XeroOP/YaaraBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/XeroOP/YaaraBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import idle, Client, filters
from config import PREFIX
from Yaara import app, LOGGER
import logging
from Yaara.modules import *

app.start()
me = app.get_me()
print(f"Yaara UserBot started for user {me.id}. Type {PREFIX}help in any telegram chat.")
idle()
