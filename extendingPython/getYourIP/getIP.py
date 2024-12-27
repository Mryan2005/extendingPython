import pyhttpx


def getYourPublicIPv4():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    session = pyhttpx.HttpSession()
    res = session.get(url='https://ipv4.icanhazip.com', headers=headers)
    return res.text
