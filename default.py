#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2013 escoand
#
#  This file is part of the radiogong.de xbmc plugin.
#
#  This plugin is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This plugin is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this plugin.  If not, see <http://www.gnu.org/licenses/>.

from os.path import join
from sys import argv
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xbmc import translatePath
import xbmcaddon
from xbmcgui import Dialog, ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setContent
from urllib2 import urlopen

Addon = xbmcaddon.Addon("plugin.audio.radiogong")
addon_handle = int(sys.argv[1])
setContent(addon_handle, 'songs')

icon = join(Addon.getAddonInfo('path'), 'resources/icon.png')
data = {
	'live': {'pl': 'https://www.radiogong.de/app/live.m3u', 'txtid': 30001},
	'top50': {'pl': 'https://www.radiogong.de/app/top50.m3u', 'txtid': 30002},
	'party': {'pl': 'https://www.radiogong.de/app/partygong.m3u', 'txtid': 30003},
	'kult': {'pl': 'https://www.radiogong.de/app/kulthits.m3u', 'txtid': 30004},
	'relaxed': {'pl': 'https://www.radiogong.de/app/relaxed.m3u', 'txtid': 30005},
	'christmas': {'pl': 'https://www.radiogong.de/app/xmas.m3u', 'txtid': 30006},
	'wiesn': {'pl': 'https://www.radiogong.de/app/wiesn.m3u', 'txtid': 30007}
}

for dataItem in data:
	item = ListItem(Addon.getLocalizedString(data [dataItem] ['txtid']), iconImage=icon)
	item.setMimeType('audio/mp3')
	item.setContentLookup(False)
	addDirectoryItem(handle=addon_handle, url=data [dataItem] ['pl'], listitem=item)

endOfDirectory(addon_handle)
