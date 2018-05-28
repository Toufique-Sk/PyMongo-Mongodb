import pymongo
from pymongo import MongoClient
import pprint
from collections import OrderedDict

client= MongoClient()

database= client.books
print database


def insert():
    try:
	    Book_id = raw_input('Enter Book_id :')
	    Book_name = raw_input('Enter Book Name :')
	    Author_name = raw_input('Enter Author Name :')
	    edition = raw_input('Enter Edition :')
    
    except Exception, e:
        print str(e)
    temp_dict={
        	"_id": Book_id,
        	"Book_name":Book_name,
        	"Author_name":Author_name,
        	"Edition":edition
        }    
    database.books.insert_one(temp_dict)
    print '\nInserted data successfully\n'


def update():
    try:
	    criteria = raw_input('\nEnter Book-id to update the record\n')
	    Book_name = raw_input('\nEnter Book_name to update\n')
	    Author_name = raw_input('\nEnter Author_name to update\n')
	    Edition = raw_input('\nEnter Edition to update\n')

	    database.books.update_one(
	        {"_id": criteria},
	        {
	        "$set": {
	            "Book_name":Book_name,
	            "Author_name":Author_name,
	            "Edition":Edition
	        }
	        }
	    )
	    print "\nRecords updated successfully\n"    
    
    except Exception, e:
    	print str(e)

def delete():
    try:
	    criteria = raw_input('\nEnter Book-id to update the record\n')

	    database.books.delete_many({"_id": criteria})
	    print "\nRecord deletion successfully\n"    
    
    except Exception, e:
    	print str(e)



def read():
    try:
	    findbook = database.books.find()
	    dataarray=[]
	    print type(findbook)
	    print '\n All data from Books Database \n'
	    for value in findbook:
	        dataarray.append(value)
	    print "--------------------------------------------------------------------------------------------------------------------------"
	    print ("Book_id			Book_name						Author_name 				Edition")
	    print "--------------------------------------------------------------------------------------------------------------------------"
	    for i in dataarray:
	     	print(str(i['_id'])+"		 "+i['Book_name']+" 			"+i['Author_name']+"				 "+i['Edition'])

	    dataarray=[]
	    print dataarray
	    		
    except Exception, e:
        print str(e)


def main():

    while(1):
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete, 0 to exit\n')
    
        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        elif selection == '0':
        	exit()
        else:
            print '\nINVALID SELECTION \n'

if __name__=='__main__':
	main()