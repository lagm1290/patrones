from abc import ABC, abstractmethod

# Interfaz para el Reporte
class IReport(ABC):
    @abstractmethod
    def generate(self):
        pass

# Implementaciones de los diferentes tipos de formato del reporte
class PDFReport(IReport):
    def generate(self):
        print("Generando reporte en formato PDF")

class ExcelReport(IReport):
    def generate(self):
        print("Generando reporte en formato Excel")

class CsvReport(IReport):
    def generate(self):
        print("Generando reporte en formato Csv")

# Clase base abstracta para el creador
class GenerateReport(ABC):
    @abstractmethod
    def get_report(self):
        pass

   
# Implementación concreta del creator
class GetReportExcell(GenerateReport):
    def get_report(self):
      return ExcelReport()


class GetReportCsv(GenerateReport):
    def get_report(self):
      return CsvReport()



class GetReportPdf(GenerateReport):
    def get_report(self):
      return PDFReport()


# Cliente
if __name__ == "__main__":

  type_report = str(input("""
      [c]Para formato csv
      [e]Para formato excell
      [p]Para formato pdf
      >>>: """))

  if type_report == 'c':
    factory_report = GetReportCsv()
  elif type_report == 'e':
    factory_report = GetReportExcell()
  elif type_report == 'p':
    factory_report = GetReportPdf()
  
  try:
    report_generator = factory_report.get_report()
    report_generator.generate()
  except Exception as e:
    print("Opcion no valida")
  




