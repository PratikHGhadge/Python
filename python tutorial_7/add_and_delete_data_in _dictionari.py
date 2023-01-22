# # add and delete data in dictionari
user_info = {'name':'pratik','age':'21','fav_movies':['avanger','avtar','race'],
              'fav_animals':['dog','cat']}
#
# #how to add data
# user_info['fav_songs'] = ['zingat','man udhan varyache']
# print(user_info)
#
# # pop method
# pooped_items = user_info.pop('fav_animals')
# print(f"pooped item is {pooped_items}")

#popitem method
pooped_item = user_info.popitem()
print(user_info)
print(pooped_item)
