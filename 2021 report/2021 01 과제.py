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

  def __mul__(self, other):
    if type(other) == Matrix:
        assert len(self.data[0]) == len(other.data)

        tmp = [[0] * len(other.data[0]) for i in range(len(self.data))]
        for i in range(len(self.data)):
            for k in range(len(other.data[0])):
                total = 0
                for j in range(len(other.data)):
                    total += self.data[i][j] * other.data[j][k]
                tmp[i][k] = total
        return Matrix(tmp)

    else:
        tmp = [[0] * len(self.data[0]) for i in range(len(self.data))]
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                tmp[i][j] = self.data[i][j]*other
        return Matrix(tmp)

  def __rmul__(self, other):
    tmp = [[0] * len(self.data[0]) for i in range(len(self.data))]
    for i in range(len(self.data)):
        for j in range(len(self.data[0])):
            tmp[i][j] = self.data[i][j] * other
    return Matrix(tmp)

a = Matrix([[1,2,3], [4,5,6]])
b = Matrix([[1,2], [4,5], [6,7]])
# print(a + b)
# print(a - b)
# print(a * 2)
# print(2 * a)
print(a * b)
