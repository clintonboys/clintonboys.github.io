to_sort = [3,4,1,2,5]

def MergeSort(input_list):
	if len(input_list) == 1:
		return input_list
	if len(input_list) == 2:
		if input_list[0] < input_list[1]:
			return input_list
		else:
			input_list.reverse()
			return input_list
	else:
		middle = len(input_list)/2
		new_left = MergeSort(input_list[:middle])
		new_right = MergeSort(input_list[middle:])

#		print new_left
#		print new_right

		input_list = Merge(new_left,new_right,len(input_list))

	return input_list

def Merge(left_list, right_list, n):
	merged_list = []
	for i in range(0,n):
		if len(left_list) == 0 and len(right_list) == 0:
			break
		if len(left_list) == 0:
			merged_list = merged_list + right_list
		elif len(right_list) == 0:
			merged_list = merged_list + left_list
		else:
			if left_list[0] < right_list[0]:
				merged_list.append(left_list[0])
				left_list = left_list[1:]
			else:
				merged_list.append(right_list[0])
				right_list = right_list[1:]
	return merged_list


print MergeSort(to_sort)