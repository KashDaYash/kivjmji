# Copyright (C) 2020-2021 by KashDaYash@Github, < https://github.com/KashDaYash >.
#
# This file is part of < https://github.com/KashDaYash/YaaraBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/KashDaYash/YaaraBot/blob/master/LICENSE >
#
# All rights reserved.

import motor.motor_asyncio
from config import MONGO_URI


cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
