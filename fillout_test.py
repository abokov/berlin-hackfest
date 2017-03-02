#!/usr/bin/env python3

import json
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from ca_keys import *

bdb = BigchainDB('http://localhost:9984')

def add_car(vw_car,my_public_key,my_private_key):
	print ("Step 1: Create transaction for car :", vw_car['data']['car']['VIN'])
	
	prepared_creation_tx=bdb.transactions.prepare(operation='CREATE',signers=my_public_key,asset=vw_car)


	if (input("Type 'D' to debug print: ") == "D"):
	        print ("prepared_creation_tx=",json.dumps(prepared_creation_tx,indent=2))

	print ("Step 2: Sign transcation by vw_car")
	fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys=my_private_key)

	if (input("Type 'D' to debug print: ") == "D"):
        	print ("fulfilled_creation_tx=", json.dumps(fulfilled_creation_tx, indent=2))


	print("Step 3: Send transaction to BigChainDB")
	sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)
	print("sent_creation_tx == fulfilled_creation_tx : ",sent_creation_tx == fulfilled_creation_tx)
	txid=fulfilled_creation_tx['id']
	print("transcation id: ", txid)
	status=bdb.transactions.status(txid)
	trials=0
	while True:
	        if status.get('status') == 'valid':
        	        break
	        status=bdb.transactions.status(txid)
        	trials+=1

	print("Transction status (trials: ",trials,")\n",json.dumps(status, indent=2))



my_car1 = {
        'data': {
           'car': {
                'model': 'VW jetta',
		'VIN': '1',
                'manufacturer': 'VW',
		'owner': '@dealer'
	     },
        },
    }


my_car2 = {
        'data': {
           'car': {
                'model': 'VW touran',
                'VIN': '2',
                'manufacturer': 'VW',
                'owner': '@dealer'
             },
        },
    }

my_car3 = {
        'data': {
           'car': {
                'model': 'VW golf',
                'VIN': '3',
                'manufacturer': 'VW',
                'owner': '@dealer'
             },
        },
    }




add_car(my_car1,CA_public_key,CA_private_key)
add_car(my_car2,CA_public_key,CA_private_key)
add_car(my_car3,CA_public_key,CA_private_key)


