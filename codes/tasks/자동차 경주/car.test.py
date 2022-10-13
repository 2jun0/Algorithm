import io
import unittest
from unittest import mock
from car import Car

class CarTestCase(unittest.TestCase):

  def test_contructor(self):
    '''test contructor
    - 자동차는 0부터 시작해야 함
    '''
    car = Car()
    self.assertEqual(car.pos, 0)

  def test_move(self):
    '''test move'''
    car = Car()
    car.move()
    self.assertEqual(car.pos, 1)

  @mock.patch('random.randint')
  def test_can_move_randomly(self, mock_randint):
    '''test can_move_randomly'''
    car = Car()

    mock_randint.return_value = 0
    self.assertTrue(car.can_move_randomly())

    mock_randint.return_value = 9
    self.assertFalse(car.can_move_randomly())

  @mock.patch('sys.stdout', new_callable=io.StringIO)
  def test_show_result(self, mock_stdout):
    '''test show_result'''
    car = Car()
    car.pos = 4
    car.show_result()
    self.assertEqual(mock_stdout.getvalue(), '----\n')

if __name__ == '__main__':
  unittest.main()