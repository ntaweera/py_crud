import datetime
import pymysql.cursors
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='taweerat',
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

        edit_id = int(input('Enter id to edit: '))
        edit_name = input('Enter new name/ or press enter if no change:')
        if edit_name != "":
            sql = "update register set register_name = %s where id = %s"
            val = (edit_name, edit_id)
            cursor.execute(sql, val)
        edit_dob = input('Enter new date of birth/ or press enter if no change:')
        if edit_dob != "":
            sql = "update register set register_date_of_birth = %s where id = %s"
            val = (edit_dob, edit_id)
            cursor.execute(sql, val)
            
        edit_distance = input('Enter new distance/ or press enter if no change:')
        if edit_distance != "":
            edit_distance = int(edit_distance)
            sql = "update register set register_distance = %s where id = %s"
            val = (edit_distance, edit_id)
            cursor.execute(sql, val)
        conn.commit()

                    
except :
    conn.rollback()
    
finally:
    conn.close()
