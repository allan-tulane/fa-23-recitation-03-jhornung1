"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))

    def __add__(self, other):
      max_len = max(len(self.binary_vec), len(other.binary_vec))
      self_vec = ['0'] * (max_len - len(self.binary_vec)) + self.binary_vec
      other_vec = ['0'] * (max_len - len(other.binary_vec)) + other.binary_vec

      carry = 0
      result_vec = []

      for i in range(max_len - 1, -1, -1):
        bit_sum = int(self_vec[i]) + int(other_vec[i]) + carry
        result_vec.insert(0, str(bit_sum % 2))
        carry = bit_sum // 2

      if carry:
        result_vec.insert(0, '1')

      return BinaryNumber(int(''.join(result_vec), 2))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec

  # Pad xvec and yvec with leading 0s to make them the same length
  max_len = max(len(xvec), len(yvec))
  xvec = ['0'] * (max_len - len(xvec)) + xvec
  yvec = ['0'] * (max_len - len(yvec)) + yvec

  # Base case: If both x and y are <= 1, return their product
  if x.decimal_val <= 1 or y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

  # Split xvec and yvec into two halves
  n = len(xvec)
  n_half = n // 2

  x_left = binary2int(xvec[:n_half])
  x_right = binary2int(xvec[n_half:])
  y_left = binary2int(yvec[:n_half])
  y_right = binary2int(yvec[n_half:])

  # Recursive calls to compute the sub-products
  xy_left = _quadratic_multiply(x_left, y_left)
  xy_right = _quadratic_multiply(x_right, y_right)
  xy_cross = (_quadratic_multiply(x_left, y_right) + _quadratic_multiply(x_right, y_left))

  # Perform the necessary bit shifts
  result = (bit_shift(xy_left, 2 * (n - n_half)) +
            bit_shift(xy_cross, (n - n_half)) +
            xy_right)

  return result


def test_quadratic_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  result = f(x, y)
  
  return (time.time() - start)*1000


## Testing the test function
x = BinaryNumber(100)
y = BinaryNumber(100)

print(test_quadratic_multiply(x, y, quadratic_multiply))
      