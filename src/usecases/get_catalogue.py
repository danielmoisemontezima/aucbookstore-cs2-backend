# src/usecases/get_catalogue.py
from src.entities.furnitures import Furniture
from src.entities.services import Service
from src.usecases.interfaces.catalog_repository import CatalogRepository

class GetCatalogue:
  

    def __init__(self, catalogRepo:CatalogRepository):
        
       self.catalogRepo = catalogRepo 
 #self{attributs ki nan objet a }

    def executeFurnitures(self) -> dict[Furniture]:
        listFurnitures = self.catalogRepo.getFurniture()
        return listFurnitures
    
    def executeServices(self) -> dict[Services]:
        listServices = self.catalogRepo.getServices()
        return listServices

       