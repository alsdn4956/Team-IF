# 객체 간의 산술 연산
class Element:
    def __init__(self, value=0):
        self.value = value
    
    def __str__(self) :
        return f"Element: {self.value}"
    
    def __repr__(self) :
        return str(self)

    def  __add__(self, other):
        if not isinstance(other, Element):
            raise Exception("Should not be differnt type.")
        
        ret = self.value + other.value
        return Element(ret)
    
    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception("Should not be differnt type.")
        
        ret = self.value - other.value
        return Element(ret)
    

res = Element(10) + Element(30)
print(res)

#객체 Elements 를 list 처럼.
class Element:
    def __init__(self, value=0):
        self.value = value
    
    def __str__(self) :
        return f"Element: {self.value}"
    
    def __repr__(self) :
        return str(self)

    def  __add__(self, other):
        if not isinstance(other, Element):
            raise Exception("Should not be differnt type.")
        
        ret = self.value + other.value
        return Element(ret)
    
    def __sub__(self, other):
        if not isinstance(other, Element):
            raise Exception("Should not be differnt type.")
        
        ret = self.value - other.value
        return Element(ret)
class Elements:
    def __init__(self, cap=10):
        self.cap = cap
        self.elems = [None] * cap

    def __setitem__(self,id, elem):
        self.elems[id] = elem

    def __getitem__(self, id):
        return self.elems[id]

elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)

print(elems.elems[0])
print(elems.elems[1])
print(elems[0])
print(elems[1])
