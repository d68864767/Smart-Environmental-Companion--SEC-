```python
import random

class Learning:
    def __init__(self):
        self.user_preferences = {
            'temperature': 20,  # in Celsius
            'humidity': 50,  # in percentage
            'air_quality': 100,  # in percentage
            'lighting': 50,  # in percentage
            'heating': False,  # Heating system status
            'cooling': False,  # Cooling system status
            'lighting_system': False,  # Lighting system status
            'appliances': {},  # Dictionary to store the status of various appliances
            'air_quality_index': 100,  # in percentage
            'allergen_level': 0,  # in percentage
            'lighting_for_circadian_rhythm': 50,  # in percentage
            'voice_control': False,  # Voice control status
            'gesture_control': False  # Gesture control status
        }

    def learn_and_adapt(self):
        # Simulate learning from user behavior
        self.user_preferences = {
            'temperature': random.randint(15, 25),
            'humidity': random.randint(30, 60),
            'air_quality': random.randint(80, 100),
            'lighting': random.randint(40, 60),
            'heating': random.choice([True, False]),
            'cooling': random.choice([True, False]),
            'lighting_system': random.choice([True, False]),
            'appliances': {
                'fridge': random.choice([True, False]),
                'oven': random.choice([True, False]),
                'tv': random.choice([True, False]),
                'washing_machine': random.choice([True, False])
            },
            'air_quality_index': random.randint(80, 100),
            'allergen_level': random.randint(0, 20),
            'lighting_for_circadian_rhythm': random.randint(40, 60),
            'voice_control': random.choice([True, False]),
            'gesture_control': random.choice([True, False])
        }

        # Simulate adapting to user preferences
        print("Adapting to user preferences...")
        print(f"Setting temperature to {self.user_preferences['temperature']} degrees Celsius.")
        print(f"Setting humidity to {self.user_preferences['humidity']}%.")
        print(f"Setting air quality to {self.user_preferences['air_quality']}%.")
        print(f"Setting lighting to {self.user_preferences['lighting']}%.")
        print(f"Setting heating system to {'on' if self.user_preferences['heating'] else 'off'}.")
        print(f"Setting cooling system to {'on' if self.user_preferences['cooling'] else 'off'}.")
        print(f"Setting lighting system to {'on' if self.user_preferences['lighting_system'] else 'off'}.")
        for appliance, status in self.user_preferences['appliances'].items():
            print(f"Setting {appliance} to {'on' if status else 'off'}.")
        print(f"Setting air quality index to {self.user_preferences['air_quality_index']}%.")
        print(f"Setting allergen level to {self.user_preferences['allergen_level']}%.")
        print(f"Setting lighting for circadian rhythm to {self.user_preferences['lighting_for_circadian_rhythm']}%.")
        print(f"Setting voice control to {'on' if self.user_preferences['voice_control'] else 'off'}.")
        print(f"Setting gesture control to {'on' if self.user_preferences['gesture_control'] else 'off'}.")
```
