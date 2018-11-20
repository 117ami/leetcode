def is_palindrome(s):
	"""
	type s: string
	rtype : boolean 
	"""
	if len(s) <= 1: return True
	for i in range(len(s)/2):
		if s[i] != s[len(s)-i-1]:
			return False
	return True 
