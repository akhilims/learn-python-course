# Python Course 10.1: How the Web Works - Build a URL in Python and Read the Server Headers (Part 2 of 4)
# Every cell of the notebook, in order, as one script (run: python Python_Course_10_1__How_the_Web_Works_-_Build_a_UR.py)

# ## Build the rain URL with urlencode in rain_url.py

# ## Run rain_url.py in the terminal: the safe URL

# ## Read the HTTP response headers with pathlib

from pathlib import Path
head = Path("mumbai_headers.txt")
lines = head.read_text().splitlines()
print(lines[0])
print(lines[2])
