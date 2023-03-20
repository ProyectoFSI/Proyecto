class Show:
    __show_id = ""
    __tipo = ""
    __title = ""
    __director = ""
    __cast = ""
    __country = ""
    __date_added = ""
    __release_year = ""
    __rating = ""
    __duration = ""
    __listed_in = ""
    __description = ""

    def __init__ (self, show_id, tipo, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description):
        self.__show_id = show_id
        self.__tipo = tipo
        self.__title = title
        self.__director = director
        self.__cast = cast
        self.__country = country
        self.__date_added = date_added
        self.__release_year = release_year
        self.__rating = rating
        self.__duration = duration
        self.__listed_in = listed_in
        self.__description = description

    # Getter, Setter
    @property
    def show_id(self):
        return self.__show_id

    @show_id.setter
    def show_id(self, show_id):
        self.__show_id = show_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        self.__director = director

    @property
    def cast(self):
        return self.__cast

    @cast.setter
    def cast(self, cast):
        self.__cast = cast

    @property
    def country(self):
        return self.__country

    @country.setter
    def cauntry(self, country):
        self.__country = country

    @property
    def date_added(self):
        return self.__date_added

    @date_added.setter
    def date_added(self, date_added):
        self.__date_added = date_added

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year):
        self.__releaser_year = release_year

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def listed_in(self):
        return self.__listed_in

    @listed_in.setter
    def listed_in(self, listed_in):
        self.__listed_in = listed_in

    @property
    def description(self):
        return self.__description

    @description.setter
    def decription(self, description):
        self.__description = description

    # toString

    def __str__(self) -> str:
        return "ID: " + self.__show_id + "\t\nTitle " + self.__title + "\t\n" + self.__director + "\n\t" + self.__cast + "\t\n" + self.__country + "\n\t" + self.__date_added + \
            "\n\t" + str(
                self.__release_year) + "\t\n" + self.__rating + "\n\t" + self.__duration + "\n\t" + self.__listed_in + "\n\t" + self.__description

    # Equals
    def __eq__(self, other):
        if isinstance(other, Show):
            return self.__show_id == other.__show_id
        return False
