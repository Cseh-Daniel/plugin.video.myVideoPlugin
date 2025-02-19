import xbmc

def notification(title, message, time):
    xbmc.executebuiltin('Notification(%s, %s, %d)' % (title, message, time))