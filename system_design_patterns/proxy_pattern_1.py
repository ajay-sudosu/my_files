class Actor:
    def __init__(self):
        self.is_busy = False

    def is_occupied(self):
        self.is_busy = True
        print("Actor is busy at this time.")

    def available(self):
        self.is_busy = False
        print("Actor is free at this time.")

    def get_status(self):
        return self.is_busy


class Agent:
    def __init__(self):
        self.principle = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.is_occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    a = Agent()
    a.work()

