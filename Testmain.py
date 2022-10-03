import unittest
import numpy as np
from main import Seryi_tsvet


class Testmain(unittest.TestCase):

  def setUp(self):
    self.main = Seryi_tsvet()

  def test_yarkost(self):
    (self.main.izm_yarkost(np.array([[1, 0], [0, 1]]), 255) - np.array([[255, 255],
                                                                        [255, 255]])).all()

  def test_contrast(self):
    (self.main.izm_contrast(np.ones((2, 2)), 4) - np.array([[0, 4],
                                                            [4, 0]])).all()

  def test_yarkost_and_contrast(self):
    (self.main.izm_contrast_and_yarkost(np.eye(4, 4), 3, 5) - np.array([[8, 5, 5, 5],
                                                                        [5, 8, 5, 5],
                                                                        [5, 5, 8, 5],
                                                                        [5, 5, 5, 8]])).all()

  def test_ifshape_less1(self):
    (self.main.izm_contrast_and_yarkost(np.ones(3), 0, 8) - np.array([8, 8, 8])).all()

  def test_ifshape_less2(self):
    (self.main.izm_contrast_and_yarkost(np.ones(1), 8, 0) - np.array([8, 8, 8])).all()

if __name__ == "__main__":
  unittest.main()
