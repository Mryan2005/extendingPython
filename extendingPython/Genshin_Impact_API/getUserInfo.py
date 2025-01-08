import os

from extendingPython.Genshin_Impact_API import GenshinImpactAPIExceptions

if (os.environ.get('Genshin_Impact_Cookie') == None):
    raise GenshinImpactAPIExceptions.CookieNotFound()
