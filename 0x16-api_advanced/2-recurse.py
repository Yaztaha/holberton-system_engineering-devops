#!/usr/bin/python3
""" Reddit API """


def top_ten(subreddit):
    """ Reddit API hot posts """
    import requests

    subs = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 400:
        return None

    hot_p = hotlist + [child.get("data").get("title")
                       for child in sub_info.json()
                       .get("data")
                       .get("children")]

    infos = subs.json()
    if not infos.get("data").get("after"):
        return hot_p

    return recurse(subreddit, hot_p, infos.get("data").get("count"),
                   infos.get("data").get("after"))
