```python
import random

class Health:
    def __init__(self):
        self.air_quality_index = 100  # in percentage
        self.allergen_level = 0  # in percentage
        self.lighting_for_circadian_rhythm = 50  # in percentage

    def monitor(self):
        # Simulate monitoring health and wellness
        self.air_quality_index = random.randint(80, 100)
        self.allergen_level = random.randint(0, 20)
        self.lighting_for_circadian_rhythm = random.randint(40, 60)

        # Simulate adjusting for health and wellness
        self.adjust_air_quality_index()
        self.adjust_allergen_level()
        self.adjust_lighting_for_circadian_rhythm()

    def adjust_air_quality_index(self):
        if self.air_quality_index < 90:
            print("Air quality index is poor, purifying air.")
            self.air_quality_index += 10

    def adjust_allergen_level(self):
        if self.allergen_level > 10:
            print("Allergen level is high, purifying air.")
            self.allergen_level -= 10

    def adjust_lighting_for_circadian_rhythm(self):
        if self.lighting_for_circadian_rhythm < 40:
            print("Lighting is too dim for circadian rhythm, increasing lighting.")
            self.lighting_for_circadian_rhythm += 10
        elif self.lighting_for_circadian_rhythm > 60:
            print("Lighting is too bright for circadian rhythm, decreasing lighting.")
            self.lighting_for_circadian_rhythm -= 10
```
