from users import User
import random


if __name__ == "__main__":
    print('Enter your name:')
    
    name = input()
    user_id = random.randint(0, 10000)
    user = User(name, user_id)
    
    print('New user registered.')
    print()

    user.show_info()

    print('Pick a new name:')
    new_name = input()

    user.change_name(new_name)

    print('New user info:')
    user.show_info()
