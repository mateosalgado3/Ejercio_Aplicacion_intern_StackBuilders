import unittest
from predictor import PicoPlacaPredictor

class TestPicoPlaca(unittest.TestCase):
    def setUp(self):
        self.predictor = PicoPlacaPredictor()

    def test_allowed_time(self):
        # En miércoles 5 de marzo de 2025 la placa termina en 4 y debería estar restringida
        self.assertTrue(self.predictor.can_drive("PBC-1234", "2025-03-05", "10:00"))

    def test_restricted_time(self):
        # En el lunes 3 de marzo de 2025 la placa termina en 1 y  si debería estar restringida
        self.assertFalse(self.predictor.can_drive("PBC-1231", "2025-03-03", "07:30"))

    def test_weekend(self):
        # El sábado 8 de marzo de 2025 no hay pico y placa
        self.assertTrue(self.predictor.can_drive("PBC-1232", "2025-03-08", "08:00"))

if __name__ == '__main__':
    unittest.main()
