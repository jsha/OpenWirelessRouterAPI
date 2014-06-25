#!/usr/bin/python
#
# Authentication module.
#
# Contains: Password checking, authentication token checking,
# auth_token rotation and expiration, rate limiting.

import bcrypt
import time
import os

def constant_time_equals(a, b):
  a = bytearray(a)
  b = bytearray(b)
  if len(a) != len(b):
    return False

  result = 0
  for x, y in zip(a, b):
    result |= x ^ y
  return result == 0 

class Auth:
  # Filenames
  PASSWORD = 'password'
  AUTH_TOKEN = 'auth_token'
  SESSION_DURATION = 60 * 60 * 24 # One day in seconds

  def __init__(self, path):
    self.path = path

  def is_password(candidate):
    with open(os.path.join(self.path, PASSWORD), 'r') as f:
      hashed = f.read()
    return bcrypt.checkpw(candidate, hashed)

  def save_password(new_password):
    hashed = bcrypt.hashpw(new_password, bcrypt.gensalt(10))
    with open(os.path.join(self.path, PASSWORD), 'w') as f:
      f.write(hashed)

  def is_authentication_token(candidate):
    with open(os.path.join(self.path, AUTH_TOKEN), 'r') as f:
      (stored_token, expires) = f.read().split(" ")
    # TODO: Add expiry checking
    if (token.match(r'[a-f0-9]{40}') and
        constant_time_equals(stored_token, candidate)):
      return True
    else
      return False
    pass

  def regenerate_authentication_token():
    random_bytes = bytearray(os.urandom(20))
    new_token = ''.join('02x' % b for b in random_bytes)
    expires = int(time.time())
    with open(os.path.join(self.path, AUTH_TOKEN), 'r') as f:
      f.write(' '.join(new_token, expires))
    return new_token

if __name__ == '__main__':
  print 'hi'
