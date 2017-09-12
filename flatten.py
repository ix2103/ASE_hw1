
# ****************************************************
# Ida Xu
# 4/5/17
# file: flatten.py
# 
# Function that accepts an arbitrarily-deep nested Array-like structure and returns flattened structure with any null values remove
# ****************************************************def flatten(array):
import sys

def flatten(array): 
	try: 
  		if isinstance(array, ( int, str, float, complex) ):
    			return array;
  		flattened = []
  		for element in array: 
    			# for int, str, float, complex, no need to flatten more, just append
    			if isinstance( element, ( int, str, float, complex ) ):
      				flattened.append(element)
    			# Else, if not None 
    			elif element != None: 
      				for sub_element in flatten(element): # calls flatten recursively 
        				flattened.append(sub_element)
  		return flattened;
	except TypeError:
  		print ("Invalid input")
  		sys.exit()
