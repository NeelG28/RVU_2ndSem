def dict_input():
    dict1=eval(input("Enter first dictionary : "))
    dict2=eval(input("Enter second dictionary : "))
    
    merge_dict=dict1.copy()
    for key,value in dict2.items():
        if key in merge_dict:
            merge_dict[key]+=value
        else:
            merge_dict[key]=value

    
    
    print(f"Merged Dictionary : {merge_dict}")

dict_input()
