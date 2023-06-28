class Hostel:
    def __init__(self):
        print("Arranging the hotel for the marriage.")

    def _isavailable(self):
        print("Is the hotel free?")
        return True

    def book_hotel(self):
        if self._isavailable():
            print("Booking hotel for the event.")


class Florist:
    def __init__(self):
        print("Setting the flower decorations.")

    def set_flower_requirements(self):
        print("Roses and lily will be used for decorations.")


class Caterer:
    def __init__(self):
        print("Setting the food.")

    def set_cuisine(self):
        print("Indian food will be served.")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


class EventManager:
    def __init__(self):
        print("Event manager: Let me talk to other service providers.")

    def arrange(self):
        self.hotel = Hostel()
        self.hotel.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")

    def ask_event_manager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done!")


you = You()
you.ask_event_manager()
