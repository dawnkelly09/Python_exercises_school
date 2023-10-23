highway_number = int(input())

# check if between 1 and 999 (is valid highway #?)
if highway_number > 0 and highway_number < 1000:   
    #check if between 1-99 (is primary?)
    if highway_number > 0 and highway_number < 100:
        # is primary highway print ({highway_number} is primary,)
        print(f"I-{highway_number} is primary, ", end='')
        #check if highway_number % 2 == 0 (is even?)
        if highway_number % 2 == 0:
            #is east/west print("going east/west.")
            print("going east/west.")         
        else: 
            # is north/south print("going north/south.")
            print("going north/south.")
    elif highway_number > 99 and highway_number % 100 != 0:
        # 
        # is auxiliary highway print (I-{highway_number} is auxiliary,)
        print(f"I-{highway_number} is auxiliary, ", end='')
        # extract the primary
        primary_number =  highway_number % 100
        print(f"serving I-{primary_number}, ", end='')
        #check if highway_number % 2 == 0 (is even?)
        if highway_number % 2 == 0:
            #is east/west print("going east/west.")
            print("going east/west.")         
        else: 
            # is north/south print("going north/south.")
            print("going north/south.")
    else:
        print(f"{highway_number} is not a valid interstate highway number.")
else:
    print(f"{highway_number} is not a valid interstate highway number.")
