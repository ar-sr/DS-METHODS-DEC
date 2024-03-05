name_list=[]

# def main()
#     print("Enter The Opertaions:1.Add Name,2.Remove Name,3.Append Name,4.Insert Name,5.Pop Name,6.Reverse Order,7.Extend List,8.Get Numbers And Sort,9.Exit")
#     op=input("Select The Operation:")
        
    
if op=="1":
        add_name=input("Enter Your Name:")
        name_list.append(add_name)
        print(name_list)
            
            
            
            
if op=="2":
        remove_name=input("Enter The Name To Remove:")

        name_list.remove(remove_name)
        print(name_list)
    


if op=="3":
        app_name=input("Enter The Name To Append:")
        name_list.append(app_name)
        print(name_list)



if op=="4":
        in_name=input("Enter The Name To Insert:")
        name_list.insert(in_name)
        print(name_list)
            
            
if op=="5":
        pop_name= int(input("Enter The Name Position To Pop:"))
        popped=name_list.pop(pop_name)
        print(popped)
            
            
            
            
            
if op=="6":
        name_list.reverse()
        print(name_list)
            
            
            
            
            
if op=="7":
        extend_name=input("Enter The List To Extend:")
        listed=name_list.extend(extend_name)
        print(listed)    
            
            
if op=="8":
        sorted=name_list.sort()
        print(sorted)
            
            
if op=="9":
    print("Have A Nice Day!")



