import unittest
import numpy as np
from stats import Stat_istics


class Testmain(unittest.TestCase):

  def setUp(self):
    self.main = Stat_istics()

  def testingmean1(self):
    self.assertEqual(self.main.mean(np.zeros(5)), 0)

  def testingmean2(self):
    self.assertEqual(self.main.mean(np.ones(10)), 1)

  def testingmean3(self):
    self.assertEqual(self.main.mean(np.array([5, 6, 7, 8, 9])), 7)

  def testingmean4(self):
    self.assertEqual(self.main.mean(np.array([1])), 1)

  def testingmean5(self):
    self.assertEqual(self.main.mean(np.array([-1, -1, 1, 1])), 0)

  def testingvar1(self):
    self.assertEqual(self.main.disp(np.zeros(5)), 0)

  def testingvar2(self):
    self.assertEqual(self.main.disp(np.ones(10)), 0)

  def testingvar3(self):
    self.assertEqual(self.main.disp(np.array([2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5])), 1.3720238095238095)


if __name__ == "__main__":
  unittest.main()