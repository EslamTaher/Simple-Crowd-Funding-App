#!/bin/usr/python

from pymongo import MongoClient
from bson.objectid import ObjectId
from Package.Helpers import Helper
from Package.Helpers import UserSession
from Package.Modals import Project
from Package.Modals import User

while True:
    print('> Crowd Funding Application\n')
    print('> Registration - Press (1) \n')
    print('> Login - Press (2) \n')
    inputReader = int(input())
    if inputReader == 1:
        while True:
            firstName = input('> FirstName: ')
            lastName = input('> LastName:')
            email = input('> Email(please enter a valid email): ')


    elif inputReader == 2:
    else:
        print('> Sorry, Enter Valid Input\n')
