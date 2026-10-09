# from frequent_words import PatternCount as inclass_pattern_count


def patternCount(text: str, pattern: str) -> int:
	count = 0

	for i in range(len(text)):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count

# with open("rosalind_ba1a.txt", "r") as file:
# 	str_list = []
# 	for line in file:
# 		line = line.rstrip()
# 		str_list.append(line)

# 	text = str_list[0]
# 	pattern = str_list[1]

# print(patternCount(text, pattern))