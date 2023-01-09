import mysql
from mysql.connector import Error


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(image, title, description, created_at):
    print("Inserting BLOB into images table")
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='pinterestdb',
                                             user='root',
                                             password='1q2w3e4r')

        cursor = connection.cursor()
        sql_insert_blob_query = "INSERT INTO projectapp_project (image, title, description, created_at) VALUES (%s,%s,%s,%s)"

        #Picture = convertToBinaryData(image)


        # Convert data into tuple format
        insert_blob_tuple = (image, title, description, created_at)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into images table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insertBLOB("project/1.jpg", "아스날1", "아스날2", "2023-01-05")
