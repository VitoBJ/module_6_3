class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)  

    def voice(self):
        print(self.sound)



pegasus = Pegasus()


print("Начальная позиция:", pegasus.get_pos())
pegasus.run(10)
print("После бега на 10:", pegasus.get_pos())
pegasus.fly(15)
print("После полета на 15:", pegasus.get_pos())
pegasus.move(5, 10)
print("После движения (5, 10):", pegasus.get_pos())
pegasus.voice()