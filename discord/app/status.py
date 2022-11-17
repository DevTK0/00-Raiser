from datetime import datetime, timedelta


class GAMES:
    V_RISING = "V Rising"
    MINECRAFT = "Minecraft"
    CORE_KEEPER = "Core Keeper"


class Game:
    def __init__(self, name):
        self.start = datetime.now()
        self.end = datetime.now()
        self.name = name

    def extend(self):
        if self.end + timedelta(hours=1) - self.start > timedelta(hours=4):
            print("Exceeded maximum time allowed")
        else:
            self.end = self.end + timedelta(hours=1)

    def launch(self):
        self.start = datetime.now()
        self.end = datetime.now() + timedelta(hours=2)

    def expired(self):
        return datetime.now() >= self.end

    def running(self):
        return datetime.now() <= self.end

    def terminate(self):
        self.end = datetime.now()

    def __str__(self):
        return f"{self.name}({self.start})({self.end})"
