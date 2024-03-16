class Cache:
    _instance = None
    _cache_data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_data(self, key):
        return self._cache_data.get(key)

    def set_data(self, key, value):
        self._cache_data[key] = value

# Ejemplo de uso
cache = Cache()
cache.set_data("usuario", {"nombre": "lenin", "años": 30})
cached_user = cache.get_data("usuario")
print(cached_user)  

## nueva instancias
print("nueva instancia")
cache2 = Cache()
cached_user = cache.get_data("usuario")
print(cached_user)  

