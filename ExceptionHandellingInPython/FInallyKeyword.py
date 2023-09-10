def funct():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index = "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always executed")

# the above function is terminated after the return but the 'finally' block will definitely be executed but if you use a nor,al print state,emt instead of finally keyword then that will not be executed.
funct()
