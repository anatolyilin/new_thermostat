class Room:
    def __init__(self, name, temperature = -1, humidity = -1, ):
        self.name = name
        self.temperature = temperature
        self.humditiy = humidity


bedroom = Room("bedroom", 20, 10)

print(bedroom.name)
