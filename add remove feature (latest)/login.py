from firebase import firebase

# Initialize Firebase
firebase = firebase.FirebaseApplication('https://test-a1fc4-default-rtdb.firebaseio.com/', None)

# #importing data
# data = {
#     'Email': 'colsdes@gmail.com',
#     'Password': '123456789'
# }
#
# #post data
# #data base name/table name
# firebase.post('https://test-a1fc4-default-rtdb.firebaseio.com/', data)

# get data
result = firebase.get('https://test-a1fc4-default-rtdb.firebaseio.com/', '')

# GET specific column like email or password

for i in result.keys():
    print(result[i])