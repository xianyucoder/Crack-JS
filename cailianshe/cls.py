import hashlib
from hashlib import md5

'''
财联社 sign
'''
def USE_SHA(text):
	if not isinstance(text, bytes):
		text = bytes(text, 'utf-8')
	sha = hashlib.sha1(text)
	encrypts = sha.hexdigest()
	return encrypts

def md5value(s):
	a = md5(s.encode()).hexdigest()
	return a
	

a = 'app=CailianpressWeb&last_time=1563498932&os=web&refresh_type=1&rn=20&sv=6.8.0&token='
#4fff994d1c65cd1c621c3ca7d2f4c436
#4fff994d1c65cd1c621c3ca7d2f4c436
b = USE_SHA(a)
c = md5value(b)
print(c)


