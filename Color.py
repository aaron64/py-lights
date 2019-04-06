

class Color:
    WHITE = None

    def __init__(self, r, g, b):
    	self.r = min(r, 255)
    	self.g = min(g, 255)
    	self.b = min(b, 255)
    
    @classmethod
    def white(cls):
        return cls(255, 255, 255)


	
