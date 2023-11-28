class StarCinema:
    hall_list = []
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def entry_hall(hall):
        StarCinema.hall_list.append(hall)
        
class Hall(StarCinema):
    def __init__(self, row, col, hall_no) -> None:
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        StarCinema.entry_hall(self)
        super().__init__()
    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        seats = []
        for i in range(self.__row):
            row = []
            for j in range(self.__col):
                row.append(0)
            seats.append(row)
        self.__seats[id] = seats

    def view_show_list(self):
        print('--------------------------------------------------')
        for show in self.__show_list:
            print(f'MOVIE NAME: {show[1]} ID: {show[0]} TIME: {show[2]}')
        print('--------------------------------------------------')
    def book_seats(self, id, row_num, col_num):
        seat = (row_num, col_num)
        match = False
        if id in self.__seats:
            for row in range(self.__row):
                for col in range(self.__col):
                    if row == row_num and col == col_num:
                        if self.__seats[id][row][col] == 0:
                            self.__seats[id][row][col] = 1
                            print('SEAT BOOKED SUCCESSFULLY!')
                            match = True
            if match == False:
                print(f'{seat} SEAT IS NOT AVAILABLE')
        else:
            print(f'SHOW ID - {id} IS NOT VALID, TRY ANOTHER')
            

    def view_available_seats(self, id):
        if id in self.__seats:
            print(f"Available Seats for Show {id}:")
            for seat in self.__seats[id]:
                print(seat)    
        else:
            print(f"Show with ID {id} not found.")

    

cineplex = Hall(5,5,1)
cineplex.entry_show(111, 'IRON MAN', '12/December/2023')
cineplex.entry_show(232, 'BAT MAN', '12/December/2023')
cineplex.entry_show(111, 'SPIDER MAN', '12/December/2023')

while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOKED TICKET')
    print('4. EXIT')
    print('Select an option: ')
    
    choice = int(input())
    if choice == 1:
        cineplex.view_show_list()
    if choice == 2:
        id = int(input('ENTER SHOW ID: '))
        cineplex.view_available_seats(id)
    if choice == 3:
        id = int(input('ENTER SHOW ID: '))
        row_num = int(input('ENTER ROW NUMBER: '))
        col_num = int(input('ENTER COLUMN NUMBER: '))
        cineplex.book_seats(id, row_num, col_num)
    if choice == 4:
        break

