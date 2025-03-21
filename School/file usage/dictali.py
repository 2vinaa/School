if __name__ == "__main__":

    with open("read_exercise.txt", "r+") as my_file:
        first_line = my_file.readline()
        first_line = first_line.strip().split(", ")
        print(first_line)
        second_line = my_file.readline()
        second_line = second_line.strip().split(",")
        print(second_line)


        final_dict = dict(zip(first_line, second_line))
        print(final_dict)
