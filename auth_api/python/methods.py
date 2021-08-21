# These functions need to be implemented
import mysql.connector
from mysql.connector import errorcode
import jwt
import hashlib

class Token:

    def generate_token(self, username, password):
        try:
            cnx = mysql.connector.connect(
                user='secret',
                password='noPow3r',
                host='bootcamp-tht.sre.wize.mx',
                database='bootcamp_tht',
            )
            cursor = cnx.cursor()

            query = ("SELECT username, password, salt, role FROM users")
            cursor.execute(query)

            userData = {}
            saltedInput = ""
            for local_username, local_password, salt, role in cursor:
                print(f"Db data: {local_username} {local_password} {salt} {role}")

                # get user salt
                if local_username == username:
                    saltedInput = password + salt

                    # hash salted input
                    hashedPassowrd = hashlib.sha512(saltedInput.encode()).hexdigest()
                    print("Hashed password: ", hashedPassowrd)

                    # verify if hashes are the same
                    # if so return the hashed passowrd
                    if hashedPassowrd == local_password:
                        return hashedPassowrd
                    else:
                        return "Password or Username wrong"

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()


class Restricted:

    def access_data(self, authorization):
        return 'test'
