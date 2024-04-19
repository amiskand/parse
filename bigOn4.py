import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getMilestoneDays(revenues, milestones):
  # Write your code here
  
  rev = revenues
  mil = milestones
  
  n = len(rev)
  o=len(mil)
  
  total = 0
  count = 0
  reach = [0]*o
  other = []
  ptr = 0
  countL = []
  
  mid = math.floor(n/2)
  midL = math.floor(mid/2)
  midR = n - mid + midL
  
  print("n: ",n,"o: ",o,mid,midL,midR)
  def try1:
	  for i in range(n):
	    total += rev[i]
	    for j in range(o):  
	      if reach[j]>0 :
		pass
	      elif total >= mil[j]:
		reach[j] = i+1
		count +=1
   def try2:     
	   for i in range(n):
	    total += rev[i]
	    other.append(total)
	  
	  for i in range(o):
	    ptr = mid
	    #reach.insert(i,bina(mil[i],other))              
	    if other[ptr] == mil[i]  :
	      reach[i] = ptr+1
	      
	    elif other[ptr] > mil[i] :
	      if  other[ptr-1] < mil[i]:
		  reach[i] = ptr+1
	      else: 
		ptr = midL
		if other[ptr] == mil[i] :
		  reach[i] = ptr+1
		elif other[ptr]>mil[i] :  
		  #ptr += 1 
		  while ptr > 0:
		    count+=1
		    if other[ptr]>=mil[i]:
		      reach[i] = ptr+1
		      
		      #break
		    ptr-=1
		  #print("count: ",count)
		  countL.append(count)
		  count=0

		elif other[ptr] < mil[i]:              
		  while ptr <mid:
		    count+=1
		    if other[ptr]>=mil[i]:
		      reach[i] = ptr+1              
		      break
		    ptr+=1
		  #print("count: ",count)
		  countL.append(count)
		  count=0
		    
	    elif other[ptr] < mil[i] :
	      if other[ptr+1] >= mil[i]:
		reach[i] = ptr+2
	      else:
		ptr = midR
		if other[ptr] == mil[i] :
		  reach[i]=ptr+1
		  
		elif other[ptr]<mil[i]:
		  while ptr < n:
		    count+=1
		    if other[ptr]>=mil[i]:
		      reach[i] = ptr+1
		      break
		    ptr+=1
		  #print("count: ",count)
		  countL.append(count)
		  count=0
		  
		elif other[ptr]>mil[i]:
		  while ptr > mid:
		    count+=1
		    if other[ptr]>=mil[i]:
		      reach[i]=ptr
		    ptr-=1
		  #print("count: ",count)
		  countL.append(count)
		  count=0

    
  print("i is: ",i)#,j)
  #print(rev)
  print("max total:",other[-1])
  #print(reach)
  #print(mil)
  print("max count: ",max(countL))
  print("max mil",max(mil))

  if len(reach)==0:
    return -1
    #for j in range(n):
    
  return reach
  
  
  
  
  
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  revenues_3 = []
  milestones_3 = []
  revenues_3.extend(revenues_1)
  revenues_3.extend(revenues_1)
  for i in range(13):
    revenues_3.extend(revenues_3)
  
  milestones_3.extend(milestones_1)
  milestones_3.extend(milestones_2)
  for i in range(len(min(milestones_1,milestones_2))):    
    milestones_3.append(milestones_1[i]+milestones_2[i])
    
  for i in range(len(milestones_3)):
    for j in range(len(milestones_3)):
      milestones_3.append(milestones_3[j]*2) 
    
    
    
  print("mil3 is : ",  len(milestones_3)  )
    
  expected_3 = [2, 4, 4, 5, 11, 9, 4, 8, 4, 13, 10, 7, 13]
  output_3 = getMilestoneDays(revenues_3, milestones_3)
  check(expected_3, output_3)
  
