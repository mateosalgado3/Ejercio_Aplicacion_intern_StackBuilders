from datetime import datetime
from rules import PicoPlacaRules

class PicoPlacaPredictor:
    def __init__(self, rules=None):
        self.rules = rules if rules else PicoPlacaRules()

    def can_drive(self, plate: str, date_str: str, time_str: str) -> bool:
        last_digit = self._get_last_digit(plate)
        if last_digit is None:
            raise ValueError("La placa debe terminar en un numero válido")

        date = datetime.strptime(date_str, "%Y-%m-%d")
        time = datetime.strptime(time_str, "%H:%M").time()

        if self.rules.is_restricted(last_digit, date.weekday(), time):
            return False
        return True

    def _get_last_digit(self, plate: str) -> int:
        try:
            return int(plate[-1])
        except ValueError:
            return None
