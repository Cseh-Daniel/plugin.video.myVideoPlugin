import xbmc

import os
import sys

import xbmcgui
import xbmcplugin

# xbmc.executebuiltin('Notification(Hello World!, Hello World!,10000)')

URL = sys.argv[0]
HANDLE = int(sys.argv[1])

xbmc.executebuiltin(f'Notification(URL-{URL}, HANDLE-{HANDLE},10000)')

xbmcplugin.addDirectoryItem(HANDLE, "url", "listitem", False)

