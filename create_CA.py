#!/usr/bin/env python3

import json
from bigchaindb_driver.crypto import generate_keypair
from pathlib import Path
from berlin_CA import CA_file


my_file = Path(CA_file)
if  my_file.is_file():
	print("CA keys already exists in file :",CA_file)
	exit	


print ("Generate new CA keypair")
my_CA_keys = generate_keypair()

print ("CA_keys.private_key=", my_CA_keys.private_key)
print ("CA_keys.public_key=", my_CA_keys.public_key)

my_file = Path(CA_file)
if not my_file.is_file():
	f = open(CA_file, 'a')
	f.write("#!/usr/bin/env python3\n\n")
	f.write("from bigchaindb_driver.crypto import generate_keypair\n")
	f.write("global CA_private_key\n")
	f.write("global CA_public_key\n")
	f.write("CA_private_key=\"")
	f.write(my_CA_keys.private_key)
	f.write("\"\nCA_public_key=\"")
	f.write(my_CA_keys.public_key)
	f.write("\"\n\n\n")
	f.close


