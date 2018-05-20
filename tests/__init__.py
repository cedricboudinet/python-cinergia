from unittest import TestCase
from cinergia import IQ21toFloat, IQ10toFloat, FloatToIQ21, FloatToIQ10


class IQ_Tests(TestCase):

    def setUp(self):
        pass

    def test_IQ21toFloat(self):
        self.assertEqual(IQ21toFloat(0), 0.0)
        self.assertEqual(IQ21toFloat(0x1 << 21),  1.0)
        self.assertEqual(IQ21toFloat((0x1 << 32)-(0x1 << 21)),  -1.0)

    def test_IQ10toFloat(self):
        self.assertEqual(IQ10toFloat(0), 0.0)
        self.assertEqual(IQ10toFloat(0x1 << 9), 0.5)
        self.assertEqual(IQ10toFloat(0x1 << 10), 1.0)
        self.assertEqual(IQ10toFloat((0x1 << 32)-(0x1 << 10)),  -1.0)

    def test_FloatToIQ21(self):
        self.assertEqual(FloatToIQ21(0.0), 0.0)
        self.assertEqual(FloatToIQ21(1.0), 0x1 << 21)
        self.assertEqual(FloatToIQ21(-1.0), (0x1 << 32)-(0x1 << 21))

    def test_FloatToIQ10(self):
        self.assertEqual(FloatToIQ10(0.0), 0.0)
        self.assertEqual(FloatToIQ10(1.0), 0x1 << 10)
        self.assertEqual(FloatToIQ10(-1.0), (0x1 << 32)-(0x1 << 10))
