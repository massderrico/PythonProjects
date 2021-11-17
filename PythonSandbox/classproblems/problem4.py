digits = int(input("What is the 4 first digits: ")) #user inputs first 4 digits


digit1 = digits//1000 #calculates first digit
digit2 = (digits - (digit1*1000))//100 #calculates second digit
digit3 = (digits - (digit1*1000 + digit2*100))//10#calculates third digit
digit4 = (digits - (digit1*1000 + digit2*100 + digit3*10)) #calculates fourth digit

check_digit = (digit1 + digit2 +digit3 + digit4)%10 #calculates the check digit


print(str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(check_digit)) #prints the final 5 digit customer number