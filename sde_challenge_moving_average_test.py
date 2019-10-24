import unittest
from sde_challenge_moving_average import MovingAverageImpl


class TestMovingAverage(unittest.TestCase):
    def test_get_moving_average(self):
        moving_avg = MovingAverageImpl(3)
        moving_avg.add(1)
        assert moving_avg.average == 1

        moving_avg.add(2)
        moving_avg.add(3)
        assert moving_avg.average == 2

        moving_avg.add(4)
        assert moving_avg.average == 3

        moving_avg.add(5)
        assert moving_avg.average == 4

        assert moving_avg.get(0) == 1
        assert moving_avg.get(1) == 2
        assert moving_avg.get(2) == 3
        assert moving_avg.get(3) == 4
        assert moving_avg.get(4) == 5

        with self.assertRaises(Exception):
            assert moving_avg.get(5) == 5

    def test_get_average_with_n_changed(self):
        moving_avg = MovingAverageImpl(3)
        moving_avg.add(1)
        moving_avg.add(2)
        moving_avg.add(3)
        moving_avg.add(4)
        assert moving_avg.average == 3

        # change n: now we want to get average of last 4 elements
        moving_avg.n = 4
        moving_avg.add(7)
        assert moving_avg.average == 4


unittest.main(exit=False)