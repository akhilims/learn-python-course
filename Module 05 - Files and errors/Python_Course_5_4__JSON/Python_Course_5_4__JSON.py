# Python Course 5.4: JSON
# Every cell of the notebook, in order, as one script (run: python Python_Course_5_4__JSON.py)

# Packing Python data into JSON text with json.dumps

import json
data = {"name": "Asha", "age": 21}
print(json.dumps(data))

# Saving JSON to a file with json.dump

with open("user.json", "w") as f:
    json.dump(data, f)

# Reading JSON from a file with json.load

with open("user.json") as f:
    loaded = json.load(f)
print(loaded["name"])

# Reading JSON text with json.loads

text = '{"ok": true, "items": [1, 2]}'
parsed = json.loads(text)
print(parsed["items"], parsed["ok"])

# Common error: JSONDecodeError and single quotes

json.loads("{'a': 1}")
