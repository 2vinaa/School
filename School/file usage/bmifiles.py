import csv

def read_dict(filename,headers):
    people =[]
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            people.append(dict(zip(headers,line)))
        return people

def calc_bmi(height, weight)

if __name__ == "__main__":

    lista = ["name", "height", "weight", "gender"]
    x = read_dict("people.csv", lista)

    print(x)