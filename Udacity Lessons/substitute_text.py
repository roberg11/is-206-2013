##given_string = "I think %s is a perfectly normal thing to do in public."

def sub1(s):
    return given_string % s


##print sub1("running")
##print sub1("sleeping")


############


##given_string2 = "I think %s and %s are perfectly normal things to do in public."

def sub2(s1, s2):
    return given_string2 % (s1, s2)

##print sub2("running", "sleeping")


############


##given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."

def sub_m(name, nickname):
    return given_string3 % {'name': name, 'nickname': nickname}


##print sub_m("Mike", "Goose") 
