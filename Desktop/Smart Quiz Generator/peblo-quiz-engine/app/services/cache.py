cache = {}

def get_cached(key):
    return cache.get(key)

def set_cache(key, value):
    cache[key] = value