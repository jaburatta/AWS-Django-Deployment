from django.db import connection
from appfolder.models import Users


class User:

    def __init__(self, userid=None, businessname=None, secretkey=None):
        
        self.userid = userid
        self.secretkey = secretkey
        self.businessname = businessname
    
    def register(self, firstname, lastname, businessname, phone, address, email, password,secretkey):
        cur = connection.cursor()
        
        cur.execute("CALL register (%s,%s,%s,%s,%s,%s,%s,%s);", (firstname, lastname, businessname, phone, address, email, password,secretkey,))
        result = cur.fetchall()
        cur.close()
        return result[0][0]
       
       
        
    def login(self, email, password):

        result = Users.objects.raw(
            "SELECT userid, businessname, secretkey FROM users WHERE email = %s AND pass = MD5(%s)", (email, password,))

        if list(result) != []:
            self.userid = list(result)[0].userid
            self.businessname = list(result)[0].businessname
            self.secretkey = list(result)[0].secretkey
            return result
        else:
            self.userid = None





    # MySQL Version
    # def register(self, firstname, lastname, businessname, phone, address, email, password,secretkey):

    #     cur = connection.cursor()

    #     # call the register stored procedure and pass paramters from user
    #     # stored procedure is used due to the sql sub query involved to check if user exists

    #     cur.callproc('register', [firstname, lastname,
    #                               businessname, phone, address, email, password, secretkey])

    #     result = cur.fetchall()
    #     cur.close()
    #     return result[0][0]

    
