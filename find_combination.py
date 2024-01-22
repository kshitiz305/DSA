def find_combinations(index,lis,path,answer,target_number):
	if len(path) == target_number:
		return answer.append(path[:])
	if index == len(lis):
		return

	path.append(lis[index])
	find_combinations(index+1,lis,path,answer,target_number)
	path.pop()
	find_combinations(index+1,lis,path,answer,target_number)


def combination(lis,target_number):
	n = len(lis)
	answer = []
	find_combinations(0, lis, [], answer, target_number)
	return answer




print(combination([1,2,3,4],2))