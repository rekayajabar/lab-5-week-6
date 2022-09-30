''' CS Lab
Program

Name: Rekaya
Email: rjznp@umsystem.edu

PROBLEM : Describe the problem

 ALGORITHM : 
      Write out the algorithm
 
 ERROR HANDLING:
      Any Special Error handling to be noted.  Wager not less than 0. etc

 OTHER COMMENTS:
      Any special comments'''





import string

def get_school(lib_card):
    if lib_card[5] == '1':
        return "School of Computing and Engineering SCE"
    elif lib_card[5] == '2':
        return "School of Law"
    elif lib_card[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
        
def get_grade(lib_card) :
    if lib_card[6] == '1':
        return "Freshman"
    elif lib_card[6] == '2':
        return "Sophomore"
    elif lib_card[6] == '3':
        return "Junior"    
    elif lib_card[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"

def character_value(c):
    value = ord(c)
    if (value >= 48 and value<=57):
        return value - 48
    elif (value >= 65 and value<=90):
        return value - 65
    
def get_check_digit(lib_card):
    sum = 0
    for i in range(len(lib_card)):
        value = character_value(lib_card[i])
        sum += value * (i+1)
    return sum % 10
        
def verify_check_digit (lib_card):
    if len(lib_card) != 10:
        return (False,"The length of the number given must be 10")
        
    for i in range(5):
        if lib_card[i] < 'A' or lib_card[i] > 'Z':
            msg = "The first 5 characters must be A-Z, the invalid character is at index " \
            + str(i) +" is " + lib_card[i]
            return (False, msg)
    
    for i in range(7,10):
        if lib_card[i] < '0' or lib_card[i] > '9':
            msg = "The last 3 characters must be 0-9, the invalid character is at index "\
                    + str(i) +" is " + lib_card[i]
            return (False, msg)
    
    if (lib_card[5] != '1' and lib_card[5] != '2' and lib_card[5] != '3'):
            return (False, "The sixth character must be 1 2 or 3")
    
    if (lib_card[6] != '1' and lib_card[6] != '2' \
        and lib_card[6] != '3' and lib_card[6] != '4'):
            return (False, "The seventh character must be 1 2 3 or 4")
    
    calculated_value = get_check_digit(lib_card)
    given_value = int(lib_card[9])
    
    if given_value != calculated_value:
        msg = "Check digit " + str(given_value) + " does not match calculated value " \
               + str(calculated_value)
        return (False,msg)
        
    return (True,"Library card is valid.")
      

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        lib_num = input("Enter Libary Card. Hit Enter to Exit ==> ").upper().strip()
        if lib_num == '':
            break 

        result, error = verify_check_digit(lib_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(lib_num)))
            print("The card belongs to a {}".format(get_grade(lib_num)))
        else:
            print("Libary card is invalid.")
            print(error)    


       
