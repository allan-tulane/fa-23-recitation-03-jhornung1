from main import *



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
  assert quadratic_multiply(BinaryNumber(5), BinaryNumber(4)) == 5*4
  assert quadratic_multiply(BinaryNumber(100), BinaryNumber(100)) == 100*100
