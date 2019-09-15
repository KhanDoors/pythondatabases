from user import User

my_user = User.load_from_db_by_email('cowboys@cowboys.com')

my_user.save_to_db()

