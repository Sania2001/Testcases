try :
    # a= 10
    # b = 0
    # c =a/b
    # print(c)
    # print(".....")

    age = 10
    if age<18:
        raise ValueError("Not eligible")
    else:
        ("Eligible for voting")

except ZeroDivisionError as e:
    print("Exception Occured = > " + str(e))

except ValueError as e:
    print("Exception Occured = > " + str(e))

except:
    print("Exception occured")

else:  #will only execute if there is no exception in try block
    print("Program executed Successfully")

finally:
    print("Harman Ltd")



