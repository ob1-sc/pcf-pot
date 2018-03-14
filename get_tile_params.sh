#!/usr/bin/env bash

while getopts ":u" opt; do
  case $opt in
    a)
      echo "-u was triggered!" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

#om --target https://<IP> --skip-ssl-validation --username <USER> --password <PASS> curl -p /api/v0/staged/products
