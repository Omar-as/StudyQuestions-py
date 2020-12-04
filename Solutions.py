import re

## Question 1
def find_and_reverse(target, text):
  start_ind = text.find(target)
  if start_ind == -1:
    out = text
  else:
    out = text[:start_ind]
    out += target[::-1]
    out += text[start_ind + len(target):]
  return out

## Question 2
def flip_input():
  print("Enter text:")
  input_list = []
  max_len = 0
  input_list.append(input())
  max_len = max(max_len, len(input_list[-1]))
  while(input_list[-1] != ""):
    input_list.append(input())
    max_len = max(max_len, len(input_list[-1]))
  print("Printing output:")
  for i in range(max_len):
    line = ""
    for str in input_list:
      if len(str) <= i:
        line += " "
      else:
        line += str[i]
    print(line)
  
## Question 3
def shift(shift, text):
  words = text.split()
  out = ""
  for i, w in enumerate(words):
    out += w[shift:]
    out += w[:shift]
    if i != len(words) - 1:
      out += " "
  return out

## Question 4
def obfuscate(text):
  vowels = "aeiou"
  first_w = text.split(" ", 1)[0]
  vow_count = 0
  for ch in first_w:
    if ch in vowels:
      vow_count += 1
  out = text[vow_count-1::vow_count]
  mid_ch = text[len(out) // 2]
  out = out.replace(mid_ch, "?")
  print(out)

## Question 5
def loud_anagrams(text):
  w_list = re.split("[ ,.]", text)
  out = text
  for w in w_list:
    is_anagaram = False
    for w2 in w_list:
      if w != w2 and sorted(w) == sorted(w2):
        is_anagaram = True
    if is_anagaram:
      out = out.replace(w, w.upper())
  return out
    
## Question 6
def bisection_check(int_list, target):
  while len(int_list) > 1:
    elt = int_list[len(int_list) // 2]
    if elt == target:
      return True
    elif elt < target:
      int_list = int_list[len(int_list) // 2 + 1:]
    else:
      int_list = int_list[:len(int_list) // 2]
  return False

## Question 7
colourList = ['red', 'yellow', 'green', 'white']
mixedColours = []
prev_colour = None
for current_colour in colourList:
    if prev_colour is not None:
        mix = prev_colour + current_colour
        mixedColours.append(mix)
    prev_colour = current_colour
print(mixedColours)

## Question 8
def is_factorial(n):
    i = f = 1
    while f < n:
        i += 1
        f *= i
    return f == n

## Question 9
arr = [25, 11, 7, 75, 56]
min = arr[0]   
for i in range(0, len(arr)):    
    #Compare elements of array with min    
   if(arr[i] < min):    
       min = arr[i];

## Question 10
def is_right_angled(a, b, c):
    x, y, z = sorted([a, b, c])
    return x**2 + y**2 == z**2

## Question 11
def sum_series(number_of_terms):
  start = 2
  sum = 0
  for i in range(0, number_of_terms):
      sum += start
      start = (start * 10) + 2
  return sum

def sum_series_modified(pattern, number_of_terms):
  start = pattern
  sum = 0
  for i in range(0, number_of_terms):
      sum += start
      start = (start * 10) + pattern
  return sum


## Question 12
def reverse_string(x):
	if x == '':
		return ''
	return reverse_string(x[1:]) + x[0]

## Question 13
def isPrime(n, i = 2): 
    if n <= 2: 
        return n == 2
    if n % i == 0: 
        return False
    if i * i > n: 
        return True 
    return isPrime(n, i + 1) 

## Question 14
def addDictionaries(dict1, dict2):
	result = {}
	for k,v in dict1.items():
		result[k] = v
	for k,v in dict2.items():
		result[k] = result.get(k, 0) + v
	return result

## Question 15
def findMax(x):
	if len(x) == 1:
		return x[0]
	max_rest = findMax(x[1:])
	if max_rest > x[0]:
		return max_rest
	return x[0]

## Question 16
def getSumRecurse(x):
	if type(x) != type([]):
		return x
	if len(x) == 0:
		return 0
	return getSumRecurse(x[0]) + getSumRecurse(x[1:])



## 28
#by converting to list and back
def increment_tuple(tup):
   l = list(tup)
   for index in range(len(l)):
       l[index] = l[index] + 1
   return tuple(l)
 
#without converting to list and back
def increment_tuple2(tup):
   new_tuple = tuple()
   for element in tup:
       new_tuple += ((element + 1),)
   return new_tuple


## 29
def replace_last(list_of_tuples):
   for index, tup in enumerate(list_of_tuples):
       list_of_tuples[index] = tup[:-1]+(tup[0],)


##30
def reverse_every_other(nested_list):
   for item in nested_list[::2]:
       item.reverse()


##31
def remove_max_from_tuple(tup):
   max_index = tup.index(max(tup))
   return tup[:max_index] + tup[max_index+1:]


##32
def flatten_list(l):
    flat_list = []
    for nested_list in l:
        for item in nested_list:
            flat_list.append(item)
    return flat_list


##33
l = [15,12,18,21,23,36,39]
l_copy = l[:]
for index, item in enumerate(l_copy):
   if (index + item) % 3 == 0:
       l.remove(item)
print(l)

##34
"D is the correct answer."


##35
a = [4, 5, 6, 20]
b = [4, 5, 6, 20]
c = [1, 2, 3]


##36
l1 = [40, 20, 30]
l2 = [40, 20, 30]
l3 = [100, 200, 300]