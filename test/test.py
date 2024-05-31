import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):
    
    def setUp(self) -> None:
        
        self.zoo_1: Zoo = Zoo()
        self.zookeeper_1: ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id=1)
        self.fence_1: Fence = Fence(area=100, temperatura=25.0, habitat="Savana")
        self.animal_1: Animal = Animal(name="Pluto", species="Canide", age=5, height=300.0, width=1.0, preferred_habitat="Savana")
        
    def test_animal_dimensioni(self):
            """
            
            Questo Test controlla che animali troppon grandi non vengano aggiunti alla fence
            
            """
            
            self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
            result: int = len(self.fence_1.list_of_animals)
            message: str = f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
            
if __name__ == "__main__":
            
        unittest.main()
            
        
    
        