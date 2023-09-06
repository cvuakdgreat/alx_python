def multiple_returns(sentence):
	lens = len(sentence)
	if lens == 0:
		return None
	else:
		first = sentence[0]
		return lens, first
