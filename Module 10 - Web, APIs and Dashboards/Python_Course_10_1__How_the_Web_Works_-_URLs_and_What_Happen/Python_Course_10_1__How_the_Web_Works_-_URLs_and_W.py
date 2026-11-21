# Python Course 10.1: How the Web Works - URLs and What Happens When You Press Enter (Part 1 of 4)
# Every cell of the notebook, in order, as one script (run: python Python_Course_10_1__How_the_Web_Works_-_URLs_and_W.py)

# ## Build a URL in Python: scheme, host, path and query

site = "archive-api.open-meteo.com"
url = "https://" + site + "/v1/archive"
q = "?latitude=19.07&longitude=72.88"
url = url + q
print(url)

# ## Take a URL apart with urllib.parse and urlparse

from urllib.parse import urlparse
parts = urlparse(url)
print(parts.scheme)
print(parts.netloc)
print(parts.path)
print(parts.query)

# ## Read the query string with parse_qs

from urllib.parse import parse_qs
asks = parse_qs(parts.query)
print(asks)
print(asks["latitude"][0])
