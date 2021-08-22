# These functions need to be implemented
import mysql.connector
from mysql.connector import errorcode
import jwt
import hashlib
from flask import abort
from werkzeug.exceptions import Forbidden

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
                    hashedPassword = hashlib.sha512(saltedInput.encode()).hexdigest()
                    print("Hashed password: ", hashedPassword)

                    # verify if hashes are the same
                    # if so return the hashed passowrd
                    if hashedPassword == local_password:
                        # JWT token generation
                        payload = { "role": role }
                        token = jwt.encode(payload, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithm="HS256")
                        print("PAYLOAD sent: role and hash", payload)
                        return token
                    else:
                        raise Forbidden()
                        # abort(403)

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
        token =  authorization.replace("Bearer ", "")
        print("AUTH: ", token)
        try:
            jwt.decode(token, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithms="HS256")
            return "You are under protected data"
        except:
            raise Forbidden()
            # abort(403)
