

# user = {
#     'name': 'Raf',
#     'age': 26,
#     'car': [4234,234234,234],
# };

# with open('example.txt', 'a') as file:
#     file.write('\n\t\thello')

def checkAge(age) :
    y = int(age);
    if y < 10:
        print('Ты пездюк');
    elif y > 100:
        print('Ты древний');


name = '';

while len(name) == 0:
    name = input('Введи свое имя:');

age = '';
while len(age) == 0:
    age = input('Склько тебе лет?:');
    y = int(age);
    result = checkAge(age);


checkAge(age);

user = {
    'name': name,
    'age': age,
};

print('Твои данные:', user);
