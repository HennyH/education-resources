import unittest

def bitrate_convert(value: float, from_units: str, to_units: str) -> float:
    """
    Converts a bitrate amount `value` given in `from_units` into `to_units`.

    The function should support converting between the following units:
    - b/s (bits per second)
    - Kb/s (kilobits per second)
    - Mb/s (megabits per second)
    - Gb/s (gigabits per second)
    - B/s (bytes per second)
    - KB/s (kilobytes per second)
    - MB/s (megabytes per second)
    - GB/s (gigabytes per second)
    
    For the purposes of this exercise use the metric prefix values e.g.
    K = 10^3, M = 10^6, ...

    Remember that a byte contains 8 bits!
    """
    pass

try:
    from answer import bitrate_convert
except ImportError as error:
    pass

class BitrateConversionTests(unittest.TestCase):
    """Test the bitrate_convert function"""

    def test_bps_to_kbps(self):
        self.assertEqual(1, bitrate_convert(1000, "b/s", "Kb/s"), "1000 b/s should equal 1Kb/s")
        self.assertEqual(1, bitrate_convert(1000, "b/s", "Kb/s"), "1000 b/s should equal 1Kb/s")

    def test_kbps_to_bs(self):
        self.assertEqual(1000, bitrate_convert(1, "Kb/s", "b/s"), "1 Kb/s should equal 1000 b/s")
        self.assertEqual(1000, bitrate_convert(1, "Kb/s", "b/s"), "1 Kb/s should equal 1000 b/s")
    
    def test_bps_to_mbps(self):
        self.assertEqual(5 * 10 ** 6, bitrate_convert(5, "MB/s", "B/s"), "5 MB/s should equal 5,000,000 B/s")
        self.assertEqual(8 * 5 * 10 ** 6, bitrate_convert(5, "MB/s", "b/s"), "5 MB/s should equal 40,000,000 b/s")

    def test_gbps_to_mbps(self):
        self.assertAlmostEqual(8.2 * 10 ** 3, bitrate_convert(8.2, "Gb/s", "Mb/s"), msg="8.2 Gb/s should equal 8,200 Mb/s")
        self.assertAlmostEqual(8.2 * 10 ** 3, bitrate_convert(8.2, "Gb/s", "Mb/s"), msg="8.2 Gb/s should equal 8,200 Mb/s")

if __name__ == "__main__":
    unittest.main()
