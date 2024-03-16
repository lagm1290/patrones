from abc import ABC, abstractmethod
import copy




class Prototype(ABC):
    @abstractmethod
    def clonar():
        pass



class ClonarConfiguracionAplicante(Prototype):
    """docstring for ClonarConfiguracion"""
    def __init__(self, configuracion):
        self.configuracion = configuracion

    def clonar(self):
        return copy.deepcopy(self)



 # Cliente   
def main():    
    configuracion = {
        "nombre":"Lenin Andres",
        "estado":"rechazado"
     }

    configuracion_inicial = ClonarConfiguracionAplicante(configuracion)
    clonar_configuracion= configuracion_inicial.clonar()

    print(f'inicial, {configuracion_inicial.configuracion}' )
    print(f'clonada, {clonar_configuracion.configuracion}' )




if __name__ == "__main__":
    main()