

def generate_response(keys,values,message,status):
    dictionary = dict(zip(keys,values))
    dictionary = {"message":f"{message}", **dictionary}
    dictionary = {"status":f"{status}",**dictionary}
    return dictionary