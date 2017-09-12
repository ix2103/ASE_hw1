# ****************************************************
# Ida Xu
# 4/5/17
# file: test_flatten.py
# 
# Tests the function in flatten.py
# ****************************************************
import flatten
 
def main():
	#example test
	arr1 = [0, 2, [[2, 3], 8, 100, None, [[None]]], -2] 
	#different data types and nesting more
	arr2 = [ "hi!", "", 1, [None, 73, [None, 3, [1, None, ["plshireme"], 5]], 1.3, 1, -2], [(1, None, [3, None, 2], "2"), None]]
	#empty arrays
	arr3 = [[[]], 1]
	#input isn't array
	arr4 = "abc"
	#array with only None
	arr5 = [None]
	#null input
	arr6 = None
		
	test1 = flatten.flatten(arr1)
	print (test1)

	test2 = flatten.flatten(arr2)
	print (test2)

	test3 = flatten.flatten(arr3)
	print (test3)

	test4 = flatten.flatten(arr4)
	print(test4)

	test5 = flatten.flatten(arr5)
	print(test5)

	test6 = flatten.flatten(arr6)
	print(test6)
	
main()
