# Copyright (C) 2020-2021 by KashDaYash@Github, < https://github.com/KashDaYash >.
#
# This file is part of < https://github.com/XeroOP/YaaraBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/XeroOP/YaaraBot/blob/master/LICENSE >
#
# All rights reserved.

from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]
