# class to log daily data
from audioop import reverse
from mypytable import MyPyTable


class Milo:

    resturants_file = "resturants.csv"
    resturants_header = ["Resturants", "Frequency"]
    resturants_table = MyPyTable(resturants_header)

    training_file = "training.csv"
    training_header = ["Days trained", "Time trained", "Location"]
    training_table = MyPyTable(training_header)

    # resturant log methods
    def init_file(self, filename, header):
        outfile = open(filename, "w")
        for name in header:
            outfile.write(name + ",")
        outfile.write("\n")
        outfile.close()

    def read_resturants(self):
        self.resturants_table.load_from_file(self.resturants_file)

    def log_resturant(self, resturant):
        row_index = -100
        resturants_col = self.resturants_table.get_column(0)
        for index, resturant_name in enumerate(resturants_col):
            if resturant_name == resturant:
                row_index = index

        if row_index == -100:
            frequency = 1
        else:
            frequency = self.resturants_table.data[row_index][1]
            int(frequency)
            frequency += 1

        outfile = open(self.resturants_file, "a")
        outfile.write(resturant + "," + str(frequency) + ",\n")
        outfile.close()

    # training log methods
    def read_training_data(self):
        self.training_table.load_from_file(self.training_file)

    def get_current_training_day(self):
        day = self.training_table.data[-1][0]
        return day

    def log_training_day(self, time_trained=None, location=None):
        current_day = 1
        try:
            current_day = int(self.get_current_training_day()) + 1
        except IndexError:
            pass

        if not time_trained:
            time_trained = "NA"

        if not location:
            location = "NA"
        outfile = open(self.training_file, "a")
        outfile.write(str(current_day) + "," +
                      str(time_trained) + "," + location + ",\n")
        outfile.close()

    def user_interface(self):
        while(True):
            menu = "\n\n\n1. Log resturant\n2. Log Training day\n3. Quit"
            print(menu)
            mode = int(input("Enter a menu option "))

            if mode == 1:  # log resturant
                print("\n\nResturant Log")
                user_choice = int(
                    input("1. Start a blank log\n2. Add to log\n3. Go back "))
                if user_choice != 3:
                    if user_choice == 1:  # init blank file
                        self.init_file(self.resturants_file,
                                       self.resturants_header)
                    self.read_resturants()
                    resturant = input(
                        "\n\n1Enter the resturant that you want to log: ")
                    self.log_resturant(resturant)

            if mode == 2:  # log training
                print("\n\nTraining Log")
                user_choice = int(
                    input("1. Start a blank log\n2. Add to log\n3. Go back "))
                if user_choice != 3:
                    if user_choice == 1:  # init blank file
                        self.init_file(self.training_file,
                                       self.training_header)
                    self.read_training_data()
                    time = int(input("How long did you train for: "))
                    location = input("Where did you train at: ")
                    self.log_training_day(time, location)

            if mode == 3:  # quit
                break


def main():
    milo = Milo()
    milo.user_interface()


main()
