##############
#Github link
#https://github.com/KuengaWD08/03230140_BIA101_CAP3
#Kuenga Wangchen Dorji
#BBI B
#03230140
##############
#References
#https://www.w3schools.com/python/python_file_handling.asp
#https://www.geeksforgeeks.org/two-pointers-technique/

#Solution score
#12395548

#Solution

class Problem:
    def read_input(): #reads input file
        file_path = r'C:\Users\User\Desktop\CAP3_\140.txt'
        with open(file_path, 'r') as file:
            content = file.read()
        return content
   
    def print_solution(inputs):
       total = 0
       for line in inputs:
          # starts  two pointers
          left = 0
          right = len(line) - 1
        
        # Finds the first digit from left
          while left < len(line) and not line[left].isdigit():
             left += 1
          first_digit = int(line[left]) if left < len(line) else None
        
        # Finds last digit from right
          while right >= 0 and not line[right].isdigit():
             right -= 1
          last_digit = int(line[right]) if right >= 0 else None
        
        #  add them to the total
          if first_digit is not None and last_digit is not None:
            total += int(str(first_digit) + str(last_digit))
       return total
 

# Reads the input file
file_reading = Problem.read_input()

# Calculates
result = Problem.print_solution(file_reading)

# Prints totalt
print("The Total Sum is:", result)


    


          
    


    
