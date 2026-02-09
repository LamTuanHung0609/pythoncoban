# Variables 

first_name = 'Hung'
last_name = 'Lam'
country = 'Viet Nam'
city = 'Quy Nhon'
age = 19
skills = ['Python','Java', 'SQL']
person_info = {
    'firstname': 'Hung',
    'lastname': 'Lam',
    'country': 'Viet Nam',
    'city': 'Quy Nhon'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Hung', 'Lam', 'Viet Nam', 19

print(first_name, last_name, country, age)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)

