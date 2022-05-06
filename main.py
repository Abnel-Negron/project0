#Welcome to my first python project
from collections import UserList
import re
import pymongo
from bson.objectid import ObjectId


#mongodb connection below
#=============================================================
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.record_book
    #collection=db.Records
records = db.records
relation = db.relation
post_id = records.insert_one({"p" : 1}).inserted_id
post_id = relation.insert_one({"p" : 1}).inserted_id
print(post_id)
#===============================================================

from tabulate import tabulate
text = """
This is Abnel's Record Book
"""
table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)
#prints our the menu options
menu_options = {
    1: 'Would you like to add to records?',
    2: 'Would you like to add to relationship?',
    3: 'Would you like to delete?',
    4: 'Would you like to update?',
    5: 'Would you like to show?',
    6: 'Exit',

}
#defines the methods to perform CRUD

def AddContact(Name,phone_num,Email,Address,DOB):
    try:
        record = {
            "Name" : f"{Name}",
            "phone_num" : f"{phone_num}",
            "Email" : f"{Email}",
            "Address" : f"{Address}",
            "DOB": f"{DOB}"
        }
        dbResponse = db.records.insert_one(record)
        print(dbResponse.inserted_id)
    except:
            pass
#
def AddRelation(Names,relationship,knownFor):
    try:
        relationz = {
            "Name" : f"{Names}",
            "Relation" : f"{relationship}",
            "KnownFor" : f"{knownFor}"
        }
        dbResponse = db.relation.insert_one(relationz)
        print(dbResponse.inserted_id)
    except:
        pass

############
def delete(id):
	delete_record = db.records.delete_one({'_id':ObjectId(id)})
	return delete_record

# def updateRecord(id):
#     myquery = db.records.update_one({'_id':ObjectId(id)})
#     print(myquery)


#below list
def index():
	for x in db.records.find():
            print(x)
def indexx():
    for y in db.relation.find():
            print(y)
print(UserList)


######################################
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('You got more friends? \'Option 1\'')


def option2(): 
     print('How close are you to them? \'Option 2\'')

def option3():
     print('Time to delete \'Option 3\'')

def option4():
    print('Lets see the update \'Option 4\' ')

def option5():
    print('See all your friends \'Option 5\' ')

def option6():
    print('Handle option \'Option 6\' ')

if __name__=='__main__':
    option = ''
    while(True):
        print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Checks what choice was entered 
        if option == 1:
            name = input("Please enter name: ")
            phone_num = int(input("Please enter phone number: "))
            email = input("Please enter email: ")
            address = input("Please enter address: ")
            DOB = input("Please enter DOB: ")
            add = AddContact(name,phone_num,email,address,DOB)
            

        elif option == 2:
            names = input("Please enter name: ")
            relationship = input("What is your relation to them? ")
            knownFor = input("How long have you known each other? ")
            relat = AddRelation(names,relationship,knownFor)
            
           #option1()
        elif option == 3:
            dele = input("Please enter the ID you want to delete: ")
            delete(dele)
            print(" That person is not your friend anymore :( ")
            break
        elif option == 4:
            userID = input("Please enter the ID you want to update: ")
            temp1 = input("Enter their name: ")
            temp2 = input("Enter phone number: ")
            db.records.insert_one({'Name': temp1, 'phone_num': temp2})

            #option3()
        elif option == 5:
            print("\nHere you will see the entire record")
            index()
            print(index)
            print('\n')
            indexx()
            print(indexx)
            print('\n')
            
        elif option == 6:
            print('Thanks for choosing the #1 phone record system in the world! :)')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')







        






    
 