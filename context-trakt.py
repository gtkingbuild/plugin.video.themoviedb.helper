# -*- coding: utf-8 -*-
# Module: default
# Author: jurialmunkey
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import sys
from resources.lib.script.router import sync_item
from json import loads

if __name__ == '__main__':
    sync_item(**loads(sys.listitem.getProperty('tmdbhelper.context.trakt')))