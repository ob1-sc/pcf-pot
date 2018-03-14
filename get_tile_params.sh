#!/usr/bin/env bash

while getopts ":u:" opt; do
  case $opt in
    a)
      echo "-u was triggered, Parameter: $OPTARG" >&2
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

#om --target https://<IP> --skip-ssl-validation --username <USER> --password <PASS> curl -p /api/v0/staged/products
