from user import User
from database import Database

Database.initialise(database="learning", user="postgres", password="syyad", host="localhost")

user = User('syyad@syyad.com', 'syyad', 'khan')

user.save_to_db()

user_from_db = User.load_from_db_by_email('syyad@syyad.com')

print(user_from_db)
