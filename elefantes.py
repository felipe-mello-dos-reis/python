def incomodam(n, string = None):
    if  string == None:
        string = ''
    if n>0:
        string+='incomodam '
        return incomodam(n-1, string)
    else:
        return string

def elefantes(n, string = None):
    if string == None:
        string = ''
    if n < 1:
        return string
    if n == 1:
        new_string='Um elefante incomoda muita gente\n'
        return new_string+string
    else:
        new_string = str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
        string=new_string+string
        if n > 2:
            new_string=str(n-1) + ' elefantes incomodam muita gente\n'
            string=new_string+string
        return elefantes(n-1,string)