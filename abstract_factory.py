from abc import ABC, abstractmethod

class TarjetaCredito(ABC):

    @abstractmethod
    def crear(self) -> str: pass

class LibreInversion(ABC):

    @abstractmethod
    def crear(self) -> str: pass

class BancolombiaTarjetaCredito(TarjetaCredito):

    def crear(self) -> str:
        print ('Se ha creado tarjeta de credito para bancolombia')
        return 'Completado'
class DaviviendaTarjetaCredito(TarjetaCredito):

    def crear(self) -> str:
        print ('Se ha creado tarjeta de credito para bancolombia')
        return 'Completado'

class BancolombiaLibreInversion(LibreInversion):

    def crear(self) -> str:
        print ('Se ha creado  inversión para bamcolombia')
        return 'Completado'

class DaviviendaLibreInversion(LibreInversion):

    def crear(self) -> str:
        print ('Se ha creado libre inversión para davivienda')
        return 'Completado'


class AbstractFactory(ABC):

    @abstractmethod
    def crear_libre_inversion(self) -> LibreInversion: pass

    @abstractmethod
    def crear_tarjeta_credito(self) -> TarjetaCredito: pass

class BancolombiaFactory(AbstractFactory):

    def crear_libre_inversion(self) -> LibreInversion:
        return BancolombiaLibreInversion()

    def crear_tarjeta_credito(self) -> TarjetaCredito:
        return BancolombiaTarjetaCredito()

class DaviviendaFactory(AbstractFactory):

    def crear_libre_inversion(self) -> LibreInversion:
        return DaviviendaLibreInversion()

    def crear_tarjeta_credito(self) -> TarjetaCredito:
        return BancolombiaTarjetaCredito()








# Client
class CrearProductos:
    
    def __init__(self,factory):
        self.factory = factory
    
    def crear_libre_inversion(self):
        obj = self.factory.crear_libre_inversion()
        obj.crear()

    def crear_tarjeta_credito(self):
        obj = self.factory.crear_tarjeta_credito()
        obj.crear()




############################# Usuario final ######################################################
if __name__ == "__main__":

  option = str(input("""
      [1]Para crear libre inversión bancolombia
      [2]Para crear tarjeta de credito bancolombia
      [3]Para crear libre inversion davivienda
      [4]Para crear tarjeta de credito davivienda
      >>>: """))

  if option == '1':
    factory = BancolombiaFactory()
    producto = CrearProductos(factory)
    producto.crear_libre_inversion()

  elif option == '2':
    factory = BancolombiaFactory()
    producto = CrearProductos(factory)
    producto.crear_tarjeta_credito()
  elif option == '3':
    factory = DaviviendaFactory()
    producto = CrearProductos(factory)
    producto.crear_libre_inversion()
  elif option == '4':
    factory = DaviviendaFactory()
    producto = CrearProductos(factory)
    producto.crear_tarjeta_credito()
  else:
        print("Opcion no valida")











