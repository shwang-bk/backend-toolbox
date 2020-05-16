#!/usr/bin/env python

from argparse import ArgumentParser

import hashlib
import hmac
import base64

parser = ArgumentParser()
parser.add_argument('-s', dest='key', required=True)
parser.add_argument('-m', dest='message', required=True)
args = parser.parse_args()

try:
    sign = hmac.new(args.key.encode(), args.message.encode(), digestmod=hashlib.sha256)
    sign_hex = sign.hexdigest()
    sign_b64 = base64.b64encode(sign.digest())
    print(f"Message: {args.message}")
    print(f"Signature(Hex): {sign_hex}")
    print(f"Signature(Base64): {sign_b64}")
except:
    parser.print_help()
    raise