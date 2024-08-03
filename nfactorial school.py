class CinemaTicketSystem:
    def __init__(self):
        # Словари для хранения данных о фильмах, пользователях и билетах
        self.movies = {1:'Deadpool 3',
                       2:'Harry Potter 4'}
        self.users = {1: 'Arman',
                      2: 'Dauren'}
        self.tickets = {}
        # Счетчики для уникальных идентификаторов
        self.movie_counter = 1
        self.user_counter = 1
        self.ticket_counter = 1

    def addMovie(self, movieName):
        if self.movies:
            self.movie_counter = max(self.movies.keys())+1
        movie_id = self.movie_counter
        self.movies[movie_id] = movieName
        self.movie_counter += 1
        return movie_id

    def showAllMovies(self):
        if not self.movies:
            print("Нет доступных фильмов.")
            return
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        if self.users:
            self.user_counter = max(self.users.keys()) + 1
        user_id = self.user_counter
        self.users[user_id] = userName
        self.user_counter += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId not in self.users:
            print("Пользователь не найден.")
            return None
        if movieId not in self.movies:
            print("Фильм не найден.")
            return None
        if self.tickets:
            self.ticket_counter = max(self.tickets.keys()) + 1
        ticket_id = self.ticket_counter
        self.tickets[ticket_id] = {'user_id': userId, 'movie_id': movieId}
        self.ticket_counter += 1
        return ticket_id

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        else:
            return False

def print_menu():
    print("\nЗдравствуйте, у вас есть следующие доступные функции:")
    print("1. Добавить новый фильм")
    print("2. Показать все доступные фильмы")
    print("3. Добавить нового пользователя")
    print("4. Купить билет")
    print("5. Отменить покупку билета")
    print("6. Завершение программы\n")

def main():
    cinemaSystem = CinemaTicketSystem()

    while True:
        print_menu()
        choice = input("Введите номер выбранного действия: ")


        match choice:
            case '1':
                movieName = input("Введите название фильма: ")
                movieId = cinemaSystem.addMovie(movieName)
                print(f"Фильм '{movieName}' добавлен. ID: {movieId}")

            case '2':
                cinemaSystem.showAllMovies()

            case '3':
                userName = input("Введите имя пользователя: ")
                userId = cinemaSystem.addUser(userName)
                print(f"Пользователь '{userName}' зарегистрирован. ID: {userId}")

            case '4':
                userId = int(input("Введите ID пользователя: "))
                movieId = int(input("Введите ID фильма: "))
                ticketId = cinemaSystem.buyTicket(userId, movieId)
                if ticketId is not None:
                    print(f"Билет куплен. ID: {ticketId}")

            case '5':
                ticketId = int(input("Введите ID билета для отмены: "))
                result = cinemaSystem.cancelTicket(ticketId)
                if result:
                    print("Билет успешно отменен.")
                else:
                    print("Билет с таким идентификатором не найден.")

            case '6':
                print("Завершение программы.")
                break

            case _:
                print("Неверный выбор, пожалуйста, выберите корректный номер действия.")


if __name__ == "__main__":
    main()
