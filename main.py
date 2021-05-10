from models.school import School


def main():
    school = School(100, True)
    for _ in range(5):
        school.finish_school_year()
        print(school)


if __name__ == '__main__':
    main()