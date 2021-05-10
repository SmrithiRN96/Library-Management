import pymongo
from pymongo import MongoClient
client = MongoClient()


class Library :
	def __init__(self) :
		self.db = client.test_database
		self.collection = self.db.test_collection
		self.collection.create_index("ID",unique = True)
	def insert(self) :
		bid = input("Enter book id : ")
		bname = input("Enter book name : ")
		bauthor = input("Enter book author : ")
		post = {"ID" : bid,
			"Name" : bname,
			"Author" : bauthor}
		x = self.collection.insert_one(post)
		print(x)
	def delete(self) :
		a = input("Enter the id of the book you want to delete : ")
		query = {"ID" : a}
		x =  self.collection.delete_one(query)
		print(x)
	def search(self) :
		b = input("Enter id to get book details : ")
		fquery = {"ID" : b}
		doc = self.collection.find(fquery)
		for x in doc :		
			print(x)
	def get(self) :
		for y in self.collection.find() :
			print(y)
	def update(self) :
		i = input("Enter id of the book you want to update : ")
		n = input("Enter updated book name : ")
		au = input("Enter updated book author : ")
		self.collection.update_one({"ID" : i},{"$set" :{"Name" : n,"Author" : au}})
		print("Updated Details")
		fquery = {"ID" : i}
		doc = self.collection.find(fquery)
		for x in doc :
			print(x)

ob = Library()

print("Option 1 : Data Insertion\nOption 2 : Data Updation\nOption 3 : Get Data\nOption 4 : Delete Data\nOption 5 : Search Data\nOprion 6 : Exit")
while(True) :
	ch = int(input("Select your option : "))
	if(ch == 1) :
		ob.insert()
	elif(ch == 2) :
		ob.update()
	elif(ch == 3) :
		ob.get()
	elif(ch == 4) :
		ob.delete()
	elif(ch == 5) :
		ob.search()
	elif(ch == 6) :
		break
