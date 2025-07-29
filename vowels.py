def vowels(s):
    vowels_list=['a','e','i','o','u']
    found=False
    count=0
    for v in vowels_list:
        if v in s:
            found= True
            count=count+1
            print(v)
            
        if found:
            print("there are vowels")
            print("The count is",count)
        else:
            print("no vowels")
vowels("aeroplaneu")

        
    
