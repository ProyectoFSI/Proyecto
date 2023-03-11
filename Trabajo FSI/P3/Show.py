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
    def show_id (self):
        return self.__show_id
    @property
    def tipo (self):
        return self.__tipo
    @property
    def title (self):
        return self.__title
    @property
    def director (self):
        return self.__director
    @property
    def cast (self):
        return self.__cast
    @property
    def country (self):
        return self.__country
    @property
    def date_added (self):
        return self.__date_added
    @property
    def release_year (self):
        return self.__release_year
    @property
    def rating (self):
        return self.__rating
    @property
    def duration (self):
        return self.__duration
    @property
    def listed_in (self):
        return self.__listed_in
    @property
    def description (self):
        return self.__description