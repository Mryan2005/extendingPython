import json

import pyhttpx
import requests


def getCloudflareDomainNameContent(Token, DomainID, RecordID):
    """
    :param Token:
    :param DomainID:
    :param RecordID:
    :return: result from Cloudflare dns_records
    """
    headers = {
        "Authorization": "Bearer " + Token,
        "Content-Type": "application/json"
    }
    session = pyhttpx.HttpSession()
    res = session.get(
        url='https://api.cloudflare.com/client/v4/zones/' + DomainID + '/dns_records/' + RecordID,
        headers=headers)
    res = json.loads(res.text)
    return res


def verifyCloudflareToken(Token: str):
    """
    :param Token:
    :return: True or False
    """
    headers = {
        "Authorization": "Bearer " + Token,
        "Content-Type": "application/json"
    }
    session = pyhttpx.HttpSession()
    res = session.get(url='https://api.cloudflare.com/client/v4/user/tokens/verify', headers=headers)
    res = json.loads(res.text)
    if res["result"]["status"] == "active":
        return True
    else:
        return False


def updateCloudflareContent(Token: str, DDNSType: str, DDNSHostName: str, DDNSContent: str, DDNS_TTL: int,
                            isProxied: bool, DomainID: str,
                            RecordID: str):
    """
    :param Token: str
    :param DDNSType: str
    :param DDNSHostName: str
    :param DDNSContent: str
    :param DDNS_TTL: int
    :param isProxied: bool
    :param DomainID: str
    :param RecordID: str
    :return: status_code
    """
    headers = {
        "Authorization": "Bearer " + Token,
        "Content-Type": "application/json"
    }
    data = {
        "type": DDNSType,
        "name": DDNSHostName,
        "content": DDNSContent,
        "ttl": DDNS_TTL,
        "proxied": isProxied
    }
    res = requests.put(
        url='https://api.cloudflare.com/client/v4/zones/' + DomainID + '/dns_records/' + RecordID,
        headers=headers, json=data)
    return res.status_code


def compareDDNSContent(NowContent: str, LastContent: str):
    """
    :param NowContent: you can use getData()
    :param LastContent: you can use getCloudflareDomainNameContent()["result"]["content"]
    :return: True or False
    """
    if NowContent == LastContent:
        return True
    else:
        return False
