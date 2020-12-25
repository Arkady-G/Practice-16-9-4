class Volunteers:
    def __init__(self, first_name, second_name, address):
        self.first_name = first_name
        self.second_name = second_name
        self.address = address


class Guest(Volunteers):
    def __init__(self, first_name, second_name, address, status):
        super().__init__(first_name, second_name, address)
        self.status = status

    def print_list(self):
        return print('"{} {}, г.{}, статус "{}"'.format(self.first_name, self.second_name, self.address, self.status))

