def patternIndex(text: str, pattern: str) -> list[int]:
	list_index  = []
	
	for i in range(len(text)):
		if text[i:(i+len(pattern))] == pattern:
			list_index.append(i)

	# output = ""

	# for i in range(len(list_index)):
	# 	output += str(list_index[i])
	# 	if (i+1) < len(list_index):
	# 		output += " "

	# # return list_index
	# return output

	return list_index

# with open("rosalind_ba1d.txt", "r") as file:
# 	str_list = []
# 	for line in file:
# 		line = line.rstrip()
# 		str_list.append(line)

# 	text = str_list[1]
# 	pattern = str_list[0]

# print(patternIndex(text, pattern))