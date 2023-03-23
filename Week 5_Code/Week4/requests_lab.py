from ast import Delete
from urllib import response
import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id) 
    response = requests.get(geturl)
    return response.json()


def createBook(book):
    

    response = requests.post(url, json = book)

    #other way to do this commented out below

    #headers = {"Content-type": "application/json"}
    #response = requests.post(url, data = json.dumps(book), headers = headers)
    return response.json()
    

def updateBook(id, bookdiff):
    updurl = url + "/" + str(id) 
    response = requests.put(updurl, json = bookdiff)
    return response
  

def deleteBook(id):
    delurl = url + "/" + str(id) 
    response = requests.delete(delurl)
    return response.json()


if  __name__ == "__main__":
    book = {
        'Author' : "test_el_3",
        'Title' : "test_el_title_3",
        'Price' : 100
    }

    bookdiff = {

        'Price' : 1002035
    }
    print(getBookById(119))
    #print(deleteBook(116))
    #print(createBook(book))
    #print(updateBook(119, bookdiff))