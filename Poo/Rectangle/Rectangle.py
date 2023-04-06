"""
Écrivez une classe « Rectangle » ayant deux variables « a » et « b » et une fonction membre 
« surface() » qui retournera la surface du rectangle.

"""

class Rectangle:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def surface(self):
        return self.a*self.b