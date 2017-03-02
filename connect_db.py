import json
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

bdb = BigchainDB('http://localhost:9984')


vm_golf = {
        'data': {
           'car': {
                'serial_number': 'abcd1k',
                'manufacturer': 'vm',
		'owner': '@dealer'
	     },
        },
    }


metadata = {'retail_price': '1000EUR'}

vw_car = generate_keypair()


print ("Step 1: Create transaction..")

prepared_creation_tx = bdb.transactions.prepare(
      operation='CREATE',
      signers=vw_car.public_key,
      asset=vm_golf,
      metadata=metadata,
   )


if (input("Type 'D' to debug print: ") == "D"):
	print ("prepared_creation_tx=", json.dumps(prepared_creation_tx, indent=2))

print ("Step 2: Sign transcation by vw_car")
fulfilled_creation_tx = bdb.transactions.fulfill(prepared_creation_tx, private_keys=vw_car.private_key)

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



