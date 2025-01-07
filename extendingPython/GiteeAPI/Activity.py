import pyhttpx

from . import Exceptions


def getTheUserWhoStarTheRepo(owner: str, repo: str, page: int = -1, access_token: str = '', per_page: int = 100):
    """
    :param owner: str, the owner of the repo
    :param repo: str, the repo name
    :param page: int, the page number
    :param access_token: str, the access token
    :param per_page: int, the number of users per page
    :return: list of users
    """
    session = pyhttpx.HttpSession()
    url = f"https://gitee.com/api/v5/repos/{owner}/{repo}/stargazers"
    if access_token == '':
        if page == -1:
            params = {
                "owner": owner,
                "repo": repo,
                "per_page": per_page
            }
        else:
            params = {
                "owner": owner,
                "repo": repo,
                "page": page,
                "per_page": per_page
            }
    else:
        if page == -1:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "per_page": per_page
            }
        else:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "page": page,
                "per_page": per_page
            }
    res = session.get(url, params=params)
    res = res.json()
    if len(res) != 0 and res.get("message") == "Not Found Project":
        raise Exceptions.NotFoundProject("The project is not found or your project is private")
    elif len(res) != 0 and res.get("message") == "401 Unauthorized: Access token does not exist":
        raise Exceptions.AccessTokenNotExist("Access token does not exist")
    return res


def getTheUserWhoWatchTheRepo(owner: str, repo: str, page: int = -1, access_token: str = '', per_page: int = 100):
    """
    :param owner: str, the owner of the repo
    :param repo: str, the repo name
    :param page: int, the page number
    :param access_token: str, the access token
    :param per_page: int, the number of users per page
    :return: list of users
    """
    session = pyhttpx.HttpSession()
    url = f"https://gitee.com/api/v5/repos/{owner}/{repo}/subscribers"
    if access_token == '':
        if page == -1:
            params = {
                "owner": owner,
                "repo": repo,
                "per_page": per_page
            }
        else:
            params = {
                "owner": owner,
                "repo": repo,
                "page": page,
                "per_page": per_page
            }
    else:
        if page == -1:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "per_page": per_page
            }
        else:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "page": page,
                "per_page": per_page
            }
    res = session.get(url, params=params)
    res = res.json()
    try:
        if res.get("message") == "Not Found Project":
            raise Exceptions.NotFoundProject("The project is not found or your project is private")
        elif res.get("message") == "401 Unauthorized: Access token does not exist":
            raise Exceptions.AccessTokenNotExist("Access token does not exist")
    except AttributeError:
        pass
    return res


def getTheMassageFromTheRepo(owner: str, repo: str, access_token: str = '', limit: int = 100, prev_id: int = -1):
    """
    :param owner: str, the owner of the repo
    :param repo: str, the repo name
    :param access_token: str, the access token
    :param limit: int, the number of messages
    :param prev_id: int, the previous message id
    :return: list of messages
    """
    session = pyhttpx.HttpSession()
    url = f"https://gitee.com/api/v5/repos/{owner}/{repo}/events"
    if access_token == '':
        if prev_id == -1:
            params = {
                "owner": owner,
                "repo": repo,
                "limit": limit
            }
        else:
            params = {
                "owner": owner,
                "repo": repo,
                "limit": limit,
                "prev_id": prev_id
            }
    else:
        if prev_id == -1:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "limit": limit
            }
        else:
            params = {
                "access_token": access_token,
                "owner": owner,
                "repo": repo,
                "limit": limit,
                "prev_id": prev_id
            }
    res = session.get(url, params=params)
    res = res.json()
    try:
        if res.get("message") == "Not Found Project":
            raise Exceptions.NotFoundProject("The project is not found or your project is private")
        elif res.get("message") == "401 Unauthorized: Access token does not exist":
            raise Exceptions.AccessTokenNotExist("Access token does not exist")
    except AttributeError:
        pass
    return res
