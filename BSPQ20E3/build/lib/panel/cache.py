
class Cache(object):
    class __Cache:
        def __init__(self):
            self.COUNTRIES = ()
            self.DATE_CHOICES = []
            self.COUNTRY_CHOICES = []

    instance = None

    def __new__(cls):
        if not Cache.instance:
            Cache.instance = Cache.__Cache()
        return Cache.instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)