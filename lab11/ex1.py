import psycopg2 as pgsql

def create_connection():
    try:
        connection = pgsql.connect(host="localhost", dbname="phonebook", user="postgres",
                                   password="12345678", port="5432")
        return connection
    except pgsql.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_pattern():
    query = """SELECT * FROM users WHERE """
    print("Do you want to search by surname(choose - 0) / name(choose - 1) / break(any number) enter the number:")
    mode = int(input())
    if mode == 0:
        query += "surname"  
        print("Enter string")
        substr = input()
        print("""Select option:
        1-surname is equal to string
        2-surname starts with the string
        3-surname ends with the string
        4-surname contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    elif mode == 1:
        query += "name"
        print("Enter string")
        substr = input()
        print("""Select option:
        1-name is equal to string
        2-name starts with the string
        3-name ends with the string
        4-name contains the string""")
        mode1 = int(input())
        if mode1 == 1:
            query += "='{}'".format(substr)
        elif mode1 == 2:
            query += " iLIKE '{}%'".format(substr)
        elif mode1 == 3:
            query += " iLIKE '%{}'".format(substr)
        else:
            query += " iLIKE '%{}%'".format(substr)
    else:
        return "error"
    return query

def insert(surname, name, phone):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT count(*) FROM users WHERE surname='{}' AND name='{}'".format(surname, name))
            if cursor.fetchone()[0] == 0:
                cursor.execute("""INSERT INTO users VALUES ('{}','{}', {})""".format(surname, name, phone))
            else:
                cursor.execute("""UPDATE users SET number={} WHERE surname='{}' AND name='{}'""".format(phone, surname, name))
            connection.commit()
        except pgsql.Error as e:
            print("Error executing insert/update query:", e)
        finally:
            if cursor:
                cursor.close()
            connection.close()

def loop_insert():
    banned = []
    while True:
        print("Want to enter a person's data? yes/no")
        mode = input().strip().lower()
        if mode == "no":
            break
        if mode != "yes":
            print("Please enter 'yes' or 'no'.")
            continue
        try:
            person = input("Enter surname, name, phone (separated by spaces): ").strip().split()
            if len(person) != 3:
                banned.append(person)
                print("Invalid input:")
                continue
            surname, name, phone = person
            if not phone.isdigit():
                banned.append(person)
                print("Invalid phone number: Must be digits only.")
                continue
            insert(surname, name, phone)
        except Exception as e:
            print("Error processing input:", e)
            banned.append(person)
    if banned:
        print("This data was not added due to incorrect format:")
        for item in banned:
            print(item)

def pagination():
    query = create_pattern()
    if query == "error":
        return "error"
    print("Need offset? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter offset:")
         offset = int(input())
         query += " OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode = input()
    if mode.lower() == "yes":
         print("Enter limit:")
         limit = int(input())
         query += " LIMIT {}".format(limit)
    query += ";"
    return query

def run_pagination():
    query = pagination()
    if query == "error":
        print("Пользователь отменил поиск.")
        return
    print("\nВаш SQL-запрос:")
    print(query)
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                print("Результаты запроса:")
                for row in rows:
                    print(row)
        except pgsql.Error as e:
            print("Ошибка при выполнении запроса:", e)
        finally:
            connection.close()


def delete():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from users")
            print(cursor.fetchall())
            print("Do you wanna delete by surname(0)/name(1)/number(2) enter the number")
            mode = int(input())
            if mode == 0:
                print("Enter surname to delete:")
                surname = input()
                query = "DELETE FROM users WHERE surname='{}'".format(surname)
            elif mode == 1:
                print("Enter name to delete:")
                name = input()
                query = "DELETE FROM users WHERE name='{}'".format(name)
            else:
                print("Enter number to delete:")
                number = input()
                query = "DELETE FROM users WHERE number={}".format(number)
            cursor.execute(query)
            connection.commit()
        except pgsql.Error as e:
            print("Error executing delete query:", e)
        finally:
            if cursor:
                cursor.close()
            connection.close()


def select_all():
    connection = create_connection()
    if connection:
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM users;")
                    rows = cursor.fetchall()
                    print(f"Contents of table users:")
                    if rows:
                        for row in rows:
                            print(row)
                    else:
                        print("Table is empty.")
        except pgsql.Error as e:
            print(f"Error executing query on table users", e)
        finally:
            connection.close()

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1 - Вставить данные")
        print("2 - Показать всех пользователей")
        print("3 - Создать SQL-запрос (поиск)")
        print("4 - Поиск с offset и limit (пагинация)")
        print("5 - Удалить пользователя")
        print("0 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            loop_insert()
        elif choice == "2":
            select_all()
        elif choice == "3":
            query = create_pattern()
            print("Сформированный SQL-запрос:")
            print(query)
        elif choice == "4":
            run_pagination()
        elif choice == "5":
            delete()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

