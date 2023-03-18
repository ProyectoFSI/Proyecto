from Show import Show
class TV_Show (Show):
    __type = ""

    def __init__(self, show_id, title, director, cast, country, date_added, release_year,rating,duration,listed_in,description):
        super().__init__(show_id, title, director, cast, country, date_added, release_year,rating,duration,listed_in,description)
        self.__type = "TV Show"

    def __str__(self) -> str:
        return self.__type + super().__str__()

    def __eq__(self, other):
        return super().__eq__(other)

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type = type

