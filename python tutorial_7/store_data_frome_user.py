
user_info = {}

user_info['name'] = input("enter your name :")
user_info['age'] = input("enter your age :")
user_info['fav_movies'] = input("Enter your fav movies seprated by , ").split(",")
user_info['fav_songs'] = input("enter your fav songs seprated by ,").split(",")

for key, valu in user_info.items():
    print(f"{key}:{valu}")