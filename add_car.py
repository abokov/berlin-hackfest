#!/usr/bin/env python3

import json
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from ca_keys import *

#key="5dkyyZN5TKniDcZRkKmJJ4pLxMXkyVxG49Wo1a2H4Lbs"
bdb = BigchainDB('http://localhost:9984')
list = bdb.outputs.get(CA_public_key)

#example of id
id_len=len("d7c12fecde7791a39b4ee997808ae70d3d02901d3d6d51e20819ee182d97be2e")
ids=[]
for i in list:
#	val=i[16:16+id_len]
	val=i
	ids.extend(val)
	print (val)


for i in ids:
	transaction = bdb.transactions.retrieve(i)
	print(transaction)
	

exit

my_car = {
        'data': {
           'car': {
                'model': 'abcd1k',
		'VIN': 'empty',
                'manufacturer': 'vm',
		'owner': '@dealer'
	     },
        },
    }

print ("Add car into database..")
my_car['data']['model']=input("Enter model:");
my_car['data']['VIN']=input("Enter VIN:")

print ("Lookup for VIN in database...")


