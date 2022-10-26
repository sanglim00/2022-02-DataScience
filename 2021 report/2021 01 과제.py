class Matrix:
  def __init__(self, data):
    self.data = data
    
  def __str__(self):
    return f"Matrix({self.data})"
    
  def __add__(self, another):
    if len(self.data) == 0 or len(another.data) == 0:
      raise Exception("Assertion Error")
      
    elif len(self.data) != len(another.data):
      raise Exception("Assertion Error")
      
    elif len(self.data[0]) != len(another.data[0]):
      raise Exception("Assertion Error")

    ret = [[0 for x in self.data[0]] for y in self.data]

    for i in range(0, len(self.data)):
      for j in range(0, len(self.data[0])):
        ret[i][j] = self.data[i][j] + another.data[i][j]

    return Matrix(ret)

  def __sub__(self, another):
    if len(self.data) == 0 or len(another.data) == 0:
      raise Exception("Assertion Error")
      
    elif len(self.data) != len(another.data):
      raise Exception("Assertion Error")
      
    elif len(self.data[0]) != len(another.data[0]):
      raise Exception("Assertion Error")
    
    ret = [[0 for x in self.data[0]] for y in self.data]

    for i in range(0, len(self.data)):
      for j in range(0, len(self.data[0])):
        ret[i][j] = self.data[i][j] - another.data[i][j]

    return Matrix(ret)

  def __mul__(self, another):
    ret = [[0 for x in self.data[0]] for y in self.data]

    if(type(another) == int):
      for i in range(0, len(self.data)):
        for j in range(0, len(self.data[0])):
          ret[i][j] = self.data[i][j] * another
    else:
      if len(self.data) == 0 or len(another.data) == 0:
        raise Exception("Assertion Error")
        
      elif len(self.data) != len(another.data):
        raise Exception("Assertion Error")
        
      elif len(self.data[0]) != len(another.data[0]):
        raise Exception("Assertion Error")
      
      for i in range(0, len(self.data)):
        for j in range(0, len(self.data[0])):
          ret[i][j] = self.data[i][j] * another.data[i][j]

    return Matrix(ret)

  def __rmul__(self, another):
    ret = [[0 for x in self.data[0]] for y in self.data]
    
    if(type(another) == int):
      for i in range(0, len(self.data)):
        for j in range(0, len(self.data[0])):
          ret[i][j] = self.data[i][j] * another
          
    else:
      if len(self.data) == 0 or len(another.data) == 0:
        raise Exception("Assertion Error")
        
      elif len(self.data) != len(another.data):
        raise Exception("Assertion Error")
        
      elif len(self.data[0]) != len(another.data[0]):
        raise Exception("Assertion Error")

      for i in range(0, len(self.data)):
        for j in range(0, len(self.data[0])):
          ret[i][j] = self.data[i][j] * another.data[i][j]

    return Matrix(ret)

a = Matrix([[1,2,3], [4,5,6]])
b = Matrix([[1,2,3], [4,5,6]])
print(a + b)
print(a - b)
print(a * 2)
print(2 * a)
print(a * b)
