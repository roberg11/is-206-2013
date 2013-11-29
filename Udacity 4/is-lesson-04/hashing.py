import hashlib
import random
import hmac
import string

SECRET = 'imsosecret'

def hash_str(s):
    return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
    return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
    val = h.split('|')[0]
    if h == make_secure_val(val):
        return val

x =  make_secure_val("test!!")
#print check_secure_val(x)

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

#print make_salt()

def make_pw_hash(name, pw, salt = None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

#print make_pw_hash('spez', 'hunter2')

def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    return h == make_pw_hash(name, pw, salt)


h = make_pw_hash('spez', 'hunter2')
print h
print valid_pw('spez', 'hunter2', h)
