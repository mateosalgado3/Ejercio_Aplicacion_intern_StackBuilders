from datetime import time

class PicoPlacaRules:
    def __init__(self):
        self.restricted_hours = [
            (time(7, 0), time(9, 30)),
            (time(16, 0), time(19, 30))
        ]
        self.restriction_map = {
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [7, 8],
            4: [9, 0],
        }

    def is_restricted(self, last_digit: int, weekday: int, current_time: time) -> bool:
        if weekday > 4:  # sabado y domingo no tiene restricciones
            return False

        restricted_digits = self.restriction_map.get(weekday, [])
        if last_digit not in restricted_digits:
            return False

        for start, end in self.restricted_hours:
            if start <= current_time <= end:
                return True
        return False
