import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="sayacpp"
)

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (name, number))

def importFromCSV():
    filename = "info.csv"
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                personName, phoneNumber = row
                cur.execute('INSERT INTO public.phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (personName, phoneNumber))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def update_contact(personName, phoneNumber):
    cur.execute('UPDATE public.phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (phoneNumber, personName))

def queryData():
    cur.execute('SELECT * FROM public.phone_book;')
    data = cur.fetchall()
    path = r"C:\Users\Аскар\Desktop\code\python\Lab10\phonebook\queredData.txt"

    with open(path, "w") as f:
        for row in data:
            f.write(f"Name: {row[1]}\nNumber: {row[2]}\n")

def deleteData():
    print("Which name do you want to delete?\n")
    personName = input()
    cur.execute('DELETE FROM public.phone_book WHERE "PersonName" = %s;', (personName,))

def deleteAllData():
    cur.execute('DELETE FROM public.phone_book;')

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload from csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from the table by person name\n\
          6. Delete all data from the table\n\
          7. Exit")
    x = int(input("Enter number 1-7\n"))
    if x == 1:
        inputData()
    elif x == 2:
        importFromCSV()
    elif x == 3:
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif x == 4:
        queryData()
    elif x == 5:
        deleteData()
    elif x == 6:
        deleteAllData()
    elif x == 7:
        done = True
    conn.commit()

cur.close()
conn.close()
