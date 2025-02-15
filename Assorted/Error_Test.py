def readposint():
    while True:
        try:
            user_input = input("Input a positive integer: ")
            if not user_input:
                raise ValueError("Please type a positive integer in the command line")
            
            num = int(user_input)
            
            if num <= 0:
                raise ValueError("The input has to be a positive integer.")
            
            return num
            
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nInterupted")
            raise
        except EOFError:
            print("\nWin closed")
            raise

try:
    num = readposint()
    print("The int was:", num)
except KeyboardInterrupt:
    print("Quiting")
except EOFError:
    print("win closed")
