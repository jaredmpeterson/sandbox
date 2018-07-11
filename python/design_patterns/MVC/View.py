from Model import Person


def show_all_view(people: list):
    print(f'There are {len(people)} people in our database:')
    for person in people:
        print(person.name())


def start_view():
    print('MVC - simplest example')
    print('Do you want to see everyone in the db? [y/n]')


def end_view():
    print('Goodbye!')
