import sys
import os
import builtIns
import xbmcplugin
import xbmcgui


HANDLE = int(sys.argv[1])

builtIns.notification("korte", "banon", 1000)

li = xbmcgui.ListItem("korte", "korte1")
xbmcplugin.addDirectoryItem(HANDLE, "korte url", li, False)

li = xbmcgui.ListItem("banon", "banon1")
xbmcplugin.addDirectoryItem(HANDLE, "banon url", li, False)

li = xbmcgui.ListItem("alma", "alma1")
xbmcplugin.addDirectoryItem(HANDLE, "alma url", li, False)

xbmcplugin.endOfDirectory(HANDLE)
