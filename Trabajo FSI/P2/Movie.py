from Show import Show

class Movie (Show):

    __type = ""

    def __init__ (self, show_id, title, director, cast, country, date_added, release_year,rating,duration,listed_in,description):
        super().__init__(show_id, title, director, cast, country, date_added, release_year,rating,duration,listed_in,description)
        self.__type = "Movie"

    def __str__(self) -> str:
        return self.__type + super().__str__()

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def show_id(self):
        return self.__show_id

    @property
    def tipo(self):
        return self.__tipo

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director

    @property
    def cast(self):
        return self.__cast

    @property
    def country(self):
        return self.__country

    @property
    def date_added(self):
        return self.__date_added

    @property
    def release_year(self):
        return self.__release_year

    @property
    def rating(self):
        return self.__rating

    @property
    def duration(self):
        return self.__duration

    @property
    def listed_in(self):
        return self.__listed_in

    @property
    def description(self):
        return self.__description




