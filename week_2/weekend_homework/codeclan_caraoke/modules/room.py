class Room:

    def __init__(self, room_name, capacity, admission_fee):
        self.name = room_name
        self.guests = []
        self.admission_fee = admission_fee
        self.capacity = capacity
        self.guests = []
        self.song_list = []

    def get_guest_list(self):
        return len(self.guests)

    def check_capacity(self):
        if len(self.guests) < self.capacity:
            return True
        else: 
            return False

    def add_guest_to_room(self, guests):
        self.guests.append(guests)

    def remove_guest_from_room(self, guests):
        self.guests.remove(guests)

    def song_count(self):
        return len(self.song_list)

    def add_song(self, song):
        self.song_list.append(song)