# berlin-hackfest
BigChainDB blockchain hackfest

# Goal
Implement workflow which allow collect telemetry data from various sources and process that data using [BigChainDB](https://github.com/bigchaindb/bigchaindb).
This project implement very simplified end-to-end soluton which can be used as demo case for BigChainDB practical appliance.
If you familiar with BigChainDB you might skip into and just to to [Implementation] part
# BigChainDB

# Implementation

Workflow is here
1) We do register new device 
2) If device is already registered we look up for transactions related to this device and update existing assests with data from that
device
3) Transfer device to another owner (*not implemented*)

## Register new device

In real life devices do not keep cryptokeys and that do they have is just some properties like (VIN/serial number/color/model name).
But what can you do with BigChainDB is lookup by transactionid or by public key (which was part of public/private key pair and use
on 'CREATE' transaction ) - when you just want to check is that device is already registered in database and device itself
don't keep that public key there's an challenge. 
### Device may securely keep it's keys
In that case then you get new device you might check is there any keys on device - if not - generate them and add device to database.
If there's a keys here - you just ask for _public_key_ from device and then then do lookup using that.

### Device can not keep it's keys
Typical scenario - 99.95%(or even more:-)) real life IoT devices aren't capable for doing that and that do they have just
printed somewhere serial number/VIN/something created by their manufacturer.

There's two options here:
* Use device unique id (serial number/VIN/whenever unique number) as public key - not really treat it as key, but put it in 
'CREATE' transaction. As soon as you never use that pair for sign/check/any other cryptooperations, you're good. But's a hack -
you put something which is not key into pair public/private key, so these two number are not a keys at all. 
Good thing about that hack that you use that unique id anywhere as reference to all transactions which related to this device
and it will works fine. Also this approach doesn't required any central authority to be involved - that you need is just to 
use that unique id for lookup transactions and you do not depend at all about who/when added that device into db before.

* 
Use some kind of Central Authority which will be provide one entry point to add/lookup device operations. So we have ha CA and always when we add new device we should reach that CA. This CA have one public/private keypair which used for all devices, so when new device came up on they just get all transactions for all devices and then lookup in these transactions for this device. Benefits here is that we have real (normal ones) cryptographic keypair which can be treated anywhere properly and there's no any hack about that. Another thing is that here we have much more possibilities for lookup for devices - for example we can do non-strict search by using not only unique id, but also using some other properties like manufacturing data (year, color, type, factory) to double check that this device id is correct. Actually we do download all transactions into some storage and then do lookup as we want - it surely will require much more resources from technical point ( i.e. RAM/CPU or even cluster of resources ), but will give two very important point :
  - using public/private key pair in correct way
  - wide set ( unlimited i may say ) of possibilities to lookup for device.
There's some downsides as well:
  - we do stick with one CA, if we talk about let's say smart cars - it should be car manufacturer ( like VolksWagen ). It's not a really convenient thing and brings many potential inconveniences from end-user point of view - like you need to reach somehow that CA (i.e. go to their website). In worst case it will bring too much beaurocracy and people won't use that - so practical implementation should be end-user oriented, not process-driven :-)
  - In any case costs of this approach will be high - more time should be taken to lookup and effecient implementation should require more computational resources.
  
  
  
  

