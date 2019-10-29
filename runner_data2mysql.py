import pymysql.cursors
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='taweerat',
                       db='race_runner',
                       cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        while True:
            register_name = input("ป้อนชื่อ-นามสกุล :")
            register_date_of_birth = input("ป้อนวันเดือนปีเกิด รูปแบบ yyyy-mm-dd:")
            register_distance = int(input("ป้อนระยะทาง 10/21/42 :"))
            sql = "INSERT INTO `register` \
                    (`register_name`,`register_date_of_birth`,\
                    `register_distance`) VALUES (%s,%s,%s)"
            cursor.execute(sql,(register_name, register_date_of_birth, register_distance))
except KeyboardInterrupt:
    conn.commit()
finally:
    conn.close()
