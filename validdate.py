import sys

day=int(sys.argv[1])
month=int(sys.argv[2])

if month < 1 or month>12:
    print("Invalid")
else:
   if month==4 or month==6 or month==9 or month==11:
        if day>0 and day < 31:
            print("valid")
        else:
            print("invalid")
   else:
        if month==2:
            if day>0 and day<30:
                print("valid")
            else:
                print("invalid")
        else:
            if day>0 and day<32:
                print("valid")
            else:
                print("invalid")
    
                
        
