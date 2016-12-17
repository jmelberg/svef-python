import sys
import json


''' Address book '''

if len(sys.argv) > 1:
    new_entry = {}
    name = sys.argv[1]
    new_entry['name'] = name

    if name:
        phone = raw_input("What is {}'s phone number? ".format(name))
        email = raw_input("What is {}'s email address? ".format(name))

        # If phone
        if len(phone) > 0:
            new_entry['phone'] = phone
        
        # If email
        if len(email) > 0:
            new_entry['email'] = email

        # Write new address book entry to file
        with open('addressbook.txt', 'a') as f:
            f.write(json.dumps(new_entry) + '\n')


''' TODO
    1. Add two more fields:
       Favorite color
       Favorite holiday food
    
    2. If the name inputted in is "master" output entire addressbook

'''


