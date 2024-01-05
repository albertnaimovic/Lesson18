# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self._name = name
#         self.__surname = surname

#     def __get_name(self) -> str:
#         return self._name


# person = Person(name="Albert", surname="Naimovic")

# print(person.name, person.surname)

# person.surname = "Kleckas"

# print(person.surname)

# print(person._name)
# print(person.__surname)

# print(person.__get_name())


# class Vehicle:
#     def mean_of_transport(self) -> str:
#         return "This is vehicle"


# class Car(Vehicle):
#     def __init__(self, brand: str) -> None:
#         self.brand = brand

#     def get_brand(self) -> str:
#         return self.brand


# class Plane(Vehicle):
#     def __init__(self, price: int) -> None:
#         self.price = price

#     def get_price(self) -> int:
#         return self.price


# car = Car(brand="Mercedes")

# print(car.get_brand())
# print(car.mean_of_transport())

# plane = Plane(price=4654651)
# print(plane.mean_of_transport())


class Employee:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def get_employee_info(self) -> str:
        return f"{self.name} {self.surname} is {self.age} years old"


class Engineers(Employee):
    def __init__(self, position: str, name: str, surname: str, age: int) -> None:
        super().__init__(
            name=name, surname=surname, age=age
        )  # pasiemam is Employee klases visus instance atributus
        self.position = position

    def get_engineer_position(self) -> str:
        return self.position


engineer = Engineers(
    position="Senior developer", name="Albert", surname="Naimovic", age=26
)
print(engineer.get_employee_info())


# class Car:
#     def __init__(self, brand: str, price: int) -> None:
#         self.brand = brand
#         self.price = price

#     def get_car_price(self) -> str:
#         return f"The price of {self.brand} is {self.price}"


# class Mercedes(Car):
#     def __init__(self, engine_type: str, brand: str, price: int) -> None:
#         super().__init__(brand=brand, price=price)
#         self.engine_type = engine_type

#     def get_engine_type(self) -> str:
#         return f"Engine type is {self.engine_type}"


# class Lexus(Car):
#     def __init__(self, production_date: int, brand: str, price: int) -> None:
#         super().__init__(brand=brand, price=price)
#         self.production_date = production_date

#     def get_production_date(self) -> str:
#         return f"Production date is {self.production_date}"


# mercedes = Mercedes(engine_type="electric", brand="MB", price=60000)
# lexus = Lexus(production_date=2020, brand="Lexus", price=50000)

# print(mercedes.get_car_price())
# print(lexus.get_car_price())


# Create a base class called Book with attributes like title, author, and publication_year. This class should have a method called display_info that prints basic information about the book. Create two subclasses of Book called Fiction and NonFiction. Add an additional attribute to each subclass, such as genre for Fiction and subject for NonFiction. Create two more subclasses, Mystery and History, that inherit from Fiction and NonFiction, respectively. Add specific attributes to each of these subclasses (e.g., detective for Mystery and time_period for History).

# Add in each sub class methods to retrieve provided data.


# class Book:
#     def __init__(self, title: str, author: str, publication_year: int) -> None:
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year

#     def display_info(self) -> str:
#         return f"Title: {self.title}\nAuthor: {self.author}\nPublication year: {self.publication_year}"


# class Fiction(Book):
#     def __init__(
#         self, genre: str, title: str, author: str, publication_year: int
#     ) -> None:
#         super().__init__(title=title, author=author, publication_year=publication_year)
#         self.genre = genre

#     def display_genre(self) -> str:
#         return f"Genre: {self.genre}"


# class NonFiction(Book):
#     def __init__(
#         self, subject: str, title: str, author: str, publication_year: int
#     ) -> None:
#         super().__init__(title=title, author=author, publication_year=publication_year)
#         self.subject = subject

#     def display_subject(self) -> str:
#         return f"Subject: {self.subject}"


# class Mystery(Fiction):
#     def __init__(
#         self, detective: str, genre: str, title: str, author: str, publication_year: int
#     ) -> None:
#         super().__init__(
#             title=title, author=author, publication_year=publication_year, genre=genre
#         )
#         self.detective = detective

#     def display_detective(self) -> bool:
#         return self.detective


# class History(NonFiction):
#     def __init__(
#         self,
#         time_period: str,
#         genre: str,
#         title: str,
#         author: str,
#         publication_year: int,
#     ) -> None:
#         super().__init__(
#             title=title, author=author, publication_year=publication_year, genre=genre
#         )
#         self.time_period = time_period

#     def display_time_period(self) -> str:
#         return f"Time period: {self.time_period}"


# fiction = Fiction(
#     genre="Crime",
#     title="Pulp Fiction",
#     author="Quentin Tarantino",
#     publication_year="1994",
# )

# mystery = Mystery(
#     detective=True,
#     genre="Thriller",
#     title="Altoriu Sesely",
#     author="V.M.P",
#     publication_year="1854",
# )

# print(fiction.display_info())
# print()
# print(mystery.display_info())
