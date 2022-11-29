import hashlib

s = "test"
result = int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
print(s)
print(result)
