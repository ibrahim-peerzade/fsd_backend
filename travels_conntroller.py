import database_connect as travels


def save_booking(full_name, Email, Mob_No, Date_and_Time, AddressFrom, AddressTo, Car_Model):
    try:
        connection = travels.connect()
        sql = f"""
        INSERT INTO booking (full_name, Email, Mob_No, Date_and_Time, AddressFrom, AddressTo, Car_Model)
        VALUES ('{full_name}', '{Email}', '{Mob_No}', '{Date_and_Time}', '{AddressFrom}', '{AddressTo}', '{Car_Model}')
        """
        print(f"Executing SQL: {sql}")
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        print(f"Database Error: {e}")
        return False


def user_register(full_name,Email,Mob_no,Gender,Address,username,password):
    connection = travels.connect()
    sql = f"INSERT INTO user_register(full_name,Email,Mob_no,Gender,Address,username,password)VALUES('{full_name}','{Email}','{Mob_no}','{Gender}','{Address}','{username}','{password}')"

    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    return True

def login(username,password):
    connection = travels.connect()
    sql = f"select Id,full_name,Email,Mob_no,Gender,Address FROM user_register where username='{username}' and password ='{password}';"
    print(sql)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result= cursor.fetchone()
    cursor.close()
    connection.close()
    return result