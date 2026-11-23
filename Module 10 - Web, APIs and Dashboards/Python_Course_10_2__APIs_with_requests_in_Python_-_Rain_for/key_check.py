import os
key = os.environ.get("DESK_KEY")
if key is None:
    print("no DESK_KEY: set it first")
else:
    print("key found, starts", key[:4])
