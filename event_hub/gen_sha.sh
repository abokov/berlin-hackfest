#Endpoint=sb://joybits-hack.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=cXiEjiSmJEGVnB+tQL5jamFXqMYPVzoLlokQ8Qp7ZVo=;EntityPath=hack-hub
PARAM='http%3A%2F%2Fjoybits-hack.servicebus.windows.net%2Fhack-hub\n1486567108'
KEY=cXiEjiSmJEGVnB+tQL5jamFXqMYPVzoLlokQ8Qp7ZVo=
KEY2=OadEer4oMLXqTbnIxhMwa7apmrpEJe%2F6JeTJecQYj1I%3D
#echo -e -n 'http%3A%2F%2Fnifi-eventhub.servicebus.windows.net%2Fhub1\n1481868000' | openssl dgst -sha256 -binary -hmac '2hmLYbJk2q5uZ2Yfyl0XSezXbxD+afO9ysh0Vsv4Xq8=' | openssl bas
echo -e -n $PARAM | openssl dgst -sha256 -binary -hmac $KEY2 | openssl base64


