from urlparse import urljoin, urlsplit

class Parser:
  
  def __init__(self, url):
    self.url = urlsplit(url)

  def removeQuery(self):
    o = self.url
    return o.scheme + '://' + o.netloc + o.path

