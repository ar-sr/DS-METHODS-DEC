


while True:
    
    
    name=input("enter a string:")
    upper_name=name.upper()
    print(upper_name)


    centercount=int(input("enter the width of centring:"))
    dot=name.center(centercount)
    print("centered string:",dot)



    substring= input("enter a substring to count:")
    result1=name.count(substring)
    print(result1)






    check=input("enter a substring to check at the end:")
    result2=name.endswith(check)
    print(result2)






    findindex=input("enter a substring to find:")
    result3=name.find(findindex)
    print(result3)




    yourname=input("enter your name:")
    age=int(input("enter your age:"))

    text= "hi iam {} and my age is {} ".format(yourname,age)
    print(text)





# if__name__=="__main__":
#     main()














