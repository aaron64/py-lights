

class Color:

    def __init__(self, r, g, b):
    	self.r = min(r, 255)
    	self.g = min(g, 255)
    	self.b = min(b, 255)

    @classmethod
    def interpolate(cls, col1, col2, val):
    	r = int((col2.r - col1.r) * val + col1.r)
    	g = int((col2.g - col1.g) * val + col1.g)
    	b = int((col2.b - col1.b) * val + col1.b)
    	return cls(r, g, b)
    
    @classmethod
    def white(cls):
        return cls(255, 255, 255)

    @classmethod
    def red(cls):
        return cls(255, 0, 0)

    @classmethod
    def green(cls):
        return cls(0, 255, 0)

    @classmethod
    def blue(cls):
        return cls(0, 0, 255)

    @classmethod
    def cyan(cls):
        return cls(0, 255, 255)

    @classmethod
    def yellow(cls):
        return cls(255, 255, 0)

    @classmethod
    def magenta(cls):
        return cls(255, 0, 255)


	
