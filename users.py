class User:

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def show_info(self):
        print('User information:')
        print('\tName:', self.name)
        print('\tID:', self.user_id)


    def change_name(self, new_name):
        self.name = new_name
