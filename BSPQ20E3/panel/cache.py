
class Cache(object):
    """
    -----------
    Description
    ----------- 
    Singleton patterned object that stores data that is used repeatedly, in order to avoid the time penalty for accessing the database 

    Attributes
    ----------
    DATA: queryset
        Data objects queryset, updated every time data capture is done from githubcsv.py
    DATE_CHOICES: str list
        Stores the different dates of all data objects to enable filtering
    COUNTRY_CHOICES: str list
        Stores the different countries of all data objects to enable filtering

    """
    class __Cache:
        def __init__(self):
            self.DATA = ["test"]
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