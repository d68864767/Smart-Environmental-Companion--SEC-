```python
import random

class Environment:
    def __init__(self):
        self.temperature = 20  # in Celsius
        self.humidity = 50  # in percentage
        self.air_quality = 100  # in percentage
        self.lighting = 50  # in percentage

    def monitor_and_adjust(self):
        # Simulate monitoring environment
        self.temperature = random.randint(15, 25)
        self.humidity = random.randint(30, 60)
        self.air_quality = random.randint(80, 100)
        self.lighting = random.randint(40, 60)

        # Simulate adjusting environment
        self.adjust_temperature()
        self.adjust_humidity()
        self.adjust_air_quality()
        self.adjust_lighting()

    def adjust_temperature(self):
        if self.temperature < 18:
            print("It's too cold, increasing temperature.")
            self.temperature += 2
        elif self.temperature > 22:
            print("It's too hot, decreasing temperature.")
            self.temperature -= 2

    def adjust_humidity(self):
        if self.humidity < 40:
            print("Humidity is too low, increasing humidity.")
            self.humidity += 10
        elif self.humidity > 60:
            print("Humidity is too high, decreasing humidity.")
            self.humidity -= 10

    def adjust_air_quality(self):
        if self.air_quality < 90:
            print("Air quality is poor, purifying air.")
            self.air_quality += 10

    def adjust_lighting(self):
        if self.lighting < 40:
            print("Lighting is too dim, increasing lighting.")
            self.lighting += 10
        elif self.lighting > 60:
            print("Lighting is too bright, decreasing lighting.")
            self.lighting -= 10
```
