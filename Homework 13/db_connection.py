import peewee
import getpass


db = peewee.MySQLDatabase("HomeWork_13", user="root",
                          password=getpass.getpass(prompt="Enter secret password:"),
                          host="localhost", port=3306)
