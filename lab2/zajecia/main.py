#!/usr/bin/python3
import sys

def add_course(name, courses, LIMIT_OF_COURSES):
    if len(courses) + 1 > LIMIT_OF_COURSES:
        print("Wyczerpano maksymalna liczbę kursów!")
    elif name not in courses:
        courses[name] = []
    else:
        raise Exception("Kurs o takiej nazwie juz istnieje!")

def remove_course(name, courses):
    if name in courses:
        courses.pop(name)
    else:
        print("Kurs o podanej nazwie nie istnieje!")

def add_pearson_to_course(perason_name, course_name, courses, LIMIT_OF_PEOPLE_IN_COURSE):
    if course_name in courses:
        if len(courses[course_name]) + 1 <= LIMIT_OF_PEOPLE_IN_COURSE:
            courses[course_name].append(perason_name)
        else:
            print("Limit osób w grupie został wyczerpany!")
    else:
        print("Kurs o podanej nazwie nie istnieje!")
    pass

def remove_pearson_from_course(perason_name, course_name, courses):
    if course_name in courses:
        if perason_name in courses[course_name]:
            courses[course_name].remove(perason_name)
        else:
            print("Takiej osoby nie ma w podanym kursie!")
    else:
        print("Taki kurs nie istnieje!")


def modify_course(old_name, new_name, courses):
    if old_name in courses:
        if new_name not in courses:
            courses[new_name] = courses[old_name]
            courses.pop(old_name)
        else:
            print("Kurs o podanej nowej nazwie juz istnieje!")
    else:
        print("Kurs o podanej nazwie nie istnieje!")
        


if __name__ == '__main__':
    LIMIT_OF_COURSES = int(sys.argv[1])
    LIMIT_OF_PEOPLE_IN_COURSE = int(sys.argv[2])

    courses = {}

    while True:
        try:
            todo = input("Co planuejsz zrobic? \n DK - dodaj kurs \n RK - usuń kurs \n MK - zmien nazwe kursu \n DU - dodaj uczestnika kursu \n RU - usun uczestnika kursu --> \n")
            if todo == "DK":
                name = input("Podaj nazwe kursu ktory chcesz utworzyc: ")
                add_course(name, courses, LIMIT_OF_COURSES)

            elif todo == "RK":
                name = input("Podaj nazwe kursu ktory chcesz usunac: ")
                remove_course(name,courses)


            elif todo == "MK":
                old_name = input("Podaj stara nazwe kursu: ")
                new_name = input("Podaj nowa nazwe kursu: ")
                modify_course(old_name, new_name, courses)

            elif todo == "DU":
                pearson_name = input("Podaj dane osoby: ")
                course_name = input("Podaj do jakiego kursu chcesz dodac osobe: ")
                add_pearson_to_course(pearson_name, course_name, courses, LIMIT_OF_PEOPLE_IN_COURSE)

            elif todo == "RU":
                pearson_name = input("Podaj dane uzytkownika do usuniecia: ")
                course_name = input("Podaj nazwę kursu w którym się znajduje: ")
                remove_pearson_from_course(pearson_name, course_name, courses)
                     
        except EOFError:
            for key, val in courses.items():
                print(key)
                for each in val:
                    print(each, end=" ")
                print()
            exit()

