import hashlib
import json
import sys

data = json.load(sys.stdin)
hash_func = data["hash_func"]
message = data["message"]

h = hashlib.new(hash_func)
h.update(str.encode(message))

response_data = {
  "hash_value": h.hexdigest()
}

json.dump(response_data, sys.stdout)