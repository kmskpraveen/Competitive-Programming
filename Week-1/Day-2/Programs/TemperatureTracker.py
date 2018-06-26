import unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    Listtemp = {}
    total = 0
    maximum = -1
    minimum = 500
    length = 0
    mode = -1

    def insert(self, temperature):
        if temperature in self.Listtemp:
            self.Listtemp[temperature] += 1
        else:
            self.Listtemp[temperature] = 1
        self.total += temperature
        if(self.maximum<=temperature):
            self.maximum = temperature
        if(self.minimum>=temperature):
            self.minimum = temperature
        self.length += 1

        for i in self.Listtemp.keys():
            if self.Listtemp[i] == max(self.Listtemp.values()):
                self.mode = i
                break

    def get_max(self):
        return self.maximum

    def get_min(self):
        return self.minimum

    def get_mean(self):
        return self.total/self.length

    def get_mode(self):
        return self.mode


















# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)