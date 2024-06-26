#Defines the mesh class 
from matplotlib import tri  

class Mesh(tri.Triangulation):
    def __init__(self):
        pass

    def method_in_superclass(self):
        pass
    # Add more methods as needed


class SubMesh(Mesh):
    def __init__(self):
        super().__init__()

    def method_in_subclass(self):
        pass
    # Add more methods as needed
