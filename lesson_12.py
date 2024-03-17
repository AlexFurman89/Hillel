# Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону,
# назву країни, кількість жителів міста, поштовий індекс міста, телефонний код міста.
# Реалізуйте доступ до окремих полів (Інкапсуляція).
# class City:
#     __name:str="no name"
#     __region:str="no region"
#     __country:str="no country"
#     __population:int=0
#     __index_code:int=0
#     __phone_code:int=0
#
#     def get_name(self):
#         return self.__name
#
#     def get_region(self):
#         return self.__region
#
#     def get_country(self):
#         return self.__country
#
#     def get_population(self):
#         return self.__population
#
#     def get_index_code(self):
#         return self.__index_code
#
#     def get_phone_code(self):
#         return self.__phone_code
#
#     def set_name(self, name):
#         self.__name=name
#
#
# new:City=City()
# print(new.get_name())
# new.set_name("New York")
# print(new.get_name())

# Завдання 2:
#
# Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту,
# кількість жителів країни, телефонний код країни, назву столиці, назву міст країни.
# Реалізуйте доступ до окремих полів (Інкапсуляція).

class Country:
    __name:str="no name"
    __continent:str="no continent"
    __population:int=0
    __phone_code:int=0
    __capital:str="no capital"

    def get_name(self):
        return self.__name

    def get_continent(self):
        return self.__continent

    def get_population(self):
        return self.__population

    def get_phone_code(self):
        return self.__phone_code

    def get_capital(self):
        return self.__capital

    def set_name(self, name):
        self.__name=name

    def set_population(self,population):
        self.__population=population

    def set_phone_code(self, phone_code):
        self.__phone_code=phone_code

    def set_capital (self, capital):
        self.__pcapital=capital