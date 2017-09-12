# ****************************************************
# Ida Xu
# 4/5/17
# file: README.txt
# 
# readme for flatten.py and test_flatten.py
# ***************************************************

I did this assignment in Python 3
flatten.py contains the flatten function. 
test_flatten.py tests the flatten function.

My function first checks if array is type int, str, float or complex and if it is, then there is no need to flatten it so it returns array. 
If it isn't though, it instantiates flattened [] and for each element in array, it checks if it is type int, str, float or complex. If it is, then it appends the element onto flattened, if it isn't and it is also not None, it calls flatten recursively and appends the sub_element. The function returns flattened. 

I assumed that array is a valid input (all the syntax is correct), and only accounted for if it was a null value (exit program). I also assumed that an empty string is not a null value. 

To run the test driver enter <python test_flatten.py> in command line. To test the function in your own test driver please  <import flatten>.

Thank you!

