#!/bin/bash
urlencode() {
    # urlencode <string>
    old_lc_collate=$LC_COLLATE
    LC_COLLATE=C
    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done
    LC_COLLATE=$old_lc_collate
}


URL='http://joybits-hack.servicebus.windows.net/hack-hub/messages'
KEY_NAME=test
KEY='cXiEjiSmJEGVnB+tQL5jamFXqMYPVzoLlokQ8Qp7ZVo='

#URL='http://joybits-hack.servicebus.windows.net'
#KEY_NAME=RootManageSharedAccessKey
#KEY='YNt2o+f8h+cRi17XSUB4hZj1ueF3q7aokKCOltojM2c='

# 1h from now in unix epic
TIMEOUT=`date +%s --date='1 hour'`
URL_ENC=`urlencode $URL`
VALUE=$URL_ENC'\n'$TIMEOUT

echo "url="$URL
echo "timeout="$TIMEOUT  " which is one hour from now = "  `date -d @$TIMEOUT`
echo "Value to Sha=" $VALUE


#Thu Dec 08 2016 06:26:40 UTC-0600 which is 1481200000 
#The string to hash is then http://nifi-eventhub.servicebus.windows.net/hub1\n1481868000
#Before hashing this string we must URL Encode it, which would result in
#   http%3A%2F%2Fnifi-eventhub.servicebus.windows.net%2Fhub1\n1481868000
#
#echo -n -e 'value' | openssl sha256 -binary -hmac 'key' | openssl base64
#example
# echo -e -n 'http%3A%2F%2Fnifi-eventhub.servicebus.windows.net%2Fhub1\n1481868000' | \
# openssl dgst -sha256 -binary -hmac '2hmLYbJk2q5uZ2Yfyl0XSezXbxD+afO9ysh0Vsv4Xq8=' | openssl base64

KEY_SHA=`echo -n -e 'value' | openssl sha256 -binary -hmac 'key' | openssl base64`
echo "key_sha=" $KEY_SHA

KEY_SHA_ENC=`urlencode $KEY_SHA`

echo "key_sha=" $KEY_SHA " key_sha_enc=" $KEY_SHA_ENC

#The value of the authorization property is formatted as
#    Authorization: SharedAccessSignature sr={URI}&sig={HMAC_SHA256_SIGNATURE}&se={EXPIRATION_TIME}&skn={KEY_NAME}
#Using our example values the property are
#    Authorization: SharedAccessSignature sig=ZYxl4SEwnNMa%2Fgir%2BaYgkb5rZv%2F6vUCqh1%2BNZgIGI4s%3D&se=1481868000&skn=hub-user&
# sr=http%3A%2F%2Fnifi-eventhub.servicebus.windows.net%2Fhub1
#use curl to confirm the token we have generated works
#    curl -v -H 'Authorization: SharedAccessSignature sig=ZYxl4SEwnNMa%2Fgir%2BaYgkb5rZv%2F6vUCqh1%2BNZgIGI4s%3D&se=1481868000&skn=hub-user&
# sr=http%3A%2F%2Fnifi-eventhub.servicebus.windows.net%2Fhub1' --data 'hello world!' https://nifi-eventhub.servicebus.windows.net/hub1/messages?timeout=60\≈i-version=2014-01

curl -v -H 'Authorization: SharedAccessSignature sig='$KEY_SHA_ENC'&se='$TIMEOUT'&skn='$KEY_NAME'&sr='$URL_ENC  -d'hi'\
 https://joybits-hack.servicebus.windows.net/hack-hub/messages


