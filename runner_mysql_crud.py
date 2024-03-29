import datetime
import pymysql.cursors
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='your_database_password',
                       db='race_runner',
                       cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "select * from register order by id"
        cursor.execute(sql)
        rows = cursor.fetchall()
        desc = cursor.description
        print("{0:>3}{1:>25}{2:>20}{3:>22}".format(desc[0][0], desc[1][0],desc[2][0], desc[3][0]))

        for row in rows:
            id = row['id']
            register_name = row['register_name']
            dob = row['register_date_of_birth']
            dob = (dob.strftime("%d-%m-%Y"))
            register_distance = row['register_distance']
            print("{0:>3}{1:>25}{2:>20}{3:>22}".format(id, register_name, dob, register_distance))

        delete_id = int(input('Enter id to delete: '))
        if delete_id != "":
            sql = "delete from register where id = %s"
            val = (delete_id)
            cursor.execute(sql, val)
            conn.commit()
            print('Delete sucessfully!')

                    
except :
    conn.rollback()
    
finally:
    conn.close()
