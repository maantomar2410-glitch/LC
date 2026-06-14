def jbbu(code,k):
    #if k is 0 then use a for loop to make each element 0
        new_code=code+code
        initial=0
        if(k>0):
            
            for i in range(1,k+1):
                initial=initial+code[i]
            for i in range(len(code)):
                add=new_code[k+1+i]
                remove=new_code[i+1]
                code[i]=initial
                initial=initial-remove+add
            return code
        else:
            for i in range(abs(k)):
                initial=initial+new_code[len(code)+k+i]
            for i in range(len(code)):
                add=new_code[len(code)+i]
                remove=new_code[len(code)+k+i]
                code[i]=initial
                initial=initial-remove+add
                
            return code