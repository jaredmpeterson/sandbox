from Model import Person
import View


def show_all():
    people_in_db = Person.get_all()
    return View.show_all_view(people_in_db)


def start():
    View.start_view()
    answer = input()
    if answer == 'y':
        return show_all()
    else:
        return View.end_view()


if __name__ == "__main__":
    start()
