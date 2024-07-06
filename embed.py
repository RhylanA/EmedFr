import urllib.parse

class Embed:
    def __init__(self, title, description="", colour="", url=""):
        self.title = title
        self.description = description
        self.colour = colour
        self.url = url
        self.author = {}
        self.thumbnail = ""

    def set_author(self, name, icon_url=""):
        self.author = {"name": name, "icon_url": icon_url}

    def set_thumbnail(self, url):
        self.thumbnail = url

    def generate_url(self, hide_url=False):
        base_url = "https://embed.benny.fun"
        query = {
            "title": self.title,
            "description": self.description,
            "colour": self.colour,
            "url": self.url,
            "author[name]": self.author.get("name"),
            "author[icon_url]": self.author.get("icon_url"),
            "thumbnail": self.thumbnail,
        }
        if hide_url:
            query["hide_url"] = "true"
        query_string = urllib.parse.urlencode(query)
        return f"{base_url}/generate?{query_string}"
