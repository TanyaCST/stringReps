from frequent_words import FrequentWords as inclass_frequent_words


def frequentWords(text: str, k: int) -> set[str]:
	frequency_dict = {}
	for i in range(len(text)):
		pattern = text[i:i+k]
		if pattern not in frequency_dict.keys():
			frequency_dict[pattern] = 1
		else:
			frequency_dict[pattern] += 1
	
	max_frequency = 0
	for key in frequency_dict.keys():
		if max_frequency < frequency_dict[key]:
			max_frequency = frequency_dict[key]

	most_frequent = []
	for pat in frequency_dict.keys():
		if frequency_dict[pat] == max_frequency:
			most_frequent.append(pat)
	
	return most_frequent
