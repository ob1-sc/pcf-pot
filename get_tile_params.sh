#!/usr/bin/env bash

OM_IP=
OM_USER=
OM_PASS=

while getopts ":i:u:p:" opt; do
  case $opt in
    i)
      OM_IP=$OPTARG
      ;;
    u)
      OM_USER=$OPTARG
      ;;
    p)
      OM_PASS=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

echo $OM_IP
echo $OM_USER
echo $OM_PASS

#om --target https://<IP> --skip-ssl-validation --username <USER> --password <PASS> curl -p /api/v0/staged/products
