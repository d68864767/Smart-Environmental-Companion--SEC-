```python
import random

class Energy:
    def __init__(self):
        self.heating = False  # Heating system status
        self.cooling = False  # Cooling system status
        self.lighting = False  # Lighting system status
        self.appliances = {}  # Dictionary to store the status of various appliances

    def optimize(self):
        # Simulate monitoring energy usage
        self.heating = random.choice([True, False])
        self.cooling = random.choice([True, False])
        self.lighting = random.choice([True, False])
        self.appliances = {
            'fridge': random.choice([True, False]),
            'oven': random.choice([True, False]),
            'tv': random.choice([True, False]),
            'washing_machine': random.choice([True, False])
        }

        # Simulate optimizing energy usage
        self.adjust_heating()
        self.adjust_cooling()
        self.adjust_lighting()
        self.adjust_appliances()

    def adjust_heating(self):
        if self.heating:
            print("Heating system is on, checking if it's necessary.")
            # If the temperature is above 22, turn off the heating system
            if self.temperature > 22:
                print("It's warm enough, turning off the heating system.")
                self.heating = False

    def adjust_cooling(self):
        if self.cooling:
            print("Cooling system is on, checking if it's necessary.")
            # If the temperature is below 18, turn off the cooling system
            if self.temperature < 18:
                print("It's cool enough, turning off the cooling system.")
                self.cooling = False

    def adjust_lighting(self):
        if self.lighting:
            print("Lighting system is on, checking if it's necessary.")
            # If the lighting is above 60, turn off some lights
            if self.lighting > 60:
                print("It's bright enough, turning off some lights.")
                self.lighting = False

    def adjust_appliances(self):
        for appliance, status in self.appliances.items():
            if status:
                print(f"{appliance} is on, checking if it's necessary.")
                # Simulate checking if the appliance is necessary
                necessary = random.choice([True, False])
                if not necessary:
                    print(f"{appliance} is not necessary at the moment, turning it off.")
                    self.appliances[appliance] = False
```
