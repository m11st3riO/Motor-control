

def create_dictionary(first_name, last_name,age, helght, birth_place,birthday, blood_type):
    user_info = {
    'firstname': first_name,
    'lastname' : last_name,
    'age': age,
    'helght': helght,
    'birth_place': birth_place,
    'birthday': birthday,
    'blood_type': blood_type}
    return user_info

dictionario_sergio = create_dictionary('segio','Garcia','20','1.95','San fernando, tamaulpas','15 noviembre','A+')
print(dictionario_sergio)
