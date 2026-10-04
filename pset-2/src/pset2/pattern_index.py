def patternIndex(text: str, pattern: str) -> list[int]:
	list_index  = []
	
	for i in range(len(text)):
		if text[i:(i+len(pattern))] == pattern:
			list_index.append(i)

	return list_index
