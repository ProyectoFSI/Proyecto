class Show:
    __show_id = ""
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

    def __init__ (self, show_id, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description):
        self._show_id = show_id
        self._title = title
        self._director = director
        self._cast = cast
        self._country = country
        self._date_added = date_added
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._listed_in = listed_in
        self._description = description

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
    # toString

    # Equals

    def __str__(self):
        return  "ID: " + self._show_id + "\t\nTitle " + self._title + "\t\n" +  self._director + "\n\t" + self._cast + "\t\n" + self._country + "\n\t" + self._date_added + \
            "\n\t" + self._release_year + "\t\n" + self._rating + "\n\t" + self._duration + "\n\t" + self._listed_in + "\n\t" + self._description

    def __eq__(self, other):
        if isinstance(other, Show):
            return self._show_id == other._show_id
        return False
