class Athlete:
    """A class to represent an athlete. """
    def __init__(self, name, age, sport):
        self.name = name
        self.age = age
        self.sport = sport
    def __str__(self):
        return f"Athlete(name={self.name}, age={self.age})"
    def __repr__(self):
        return f"Athlete(name={self.name}, age={self.age}, sport={self.sport})"
    def display(self):
        print(f"{self.name}|{self.age}|{self.sport}|")

def main():
    """TEST THE CLASS"""
    a = Athlete("Ana G", 25, "200m")
    b = Athlete("J", 30, "100m")
    c = Athlete("", 28, "400m")

    a.display()
    b.display()
    c = eval(repr(b))
    print(c)