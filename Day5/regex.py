# # regex -> regular expression

# import re
# str = "This is a example of regex"
# match = re.search(r'regex',str)
# print("Start index=",match.start())
# print("End Index =",match.end())



# import re
# str = "This is a example of reg.ex"
# match = re.search(r'.',str)
# print("matched")


# import re
# str = "This is a example of reg.ex"
# pattern="[a-m]"
# match = re.findall(pattern,str)
# print(match)

import re
result = re.compile('\d')
print(result.findall("I went to him at 11 a.m on 18th april 2025"))
result = re.compile('\d+')
print(result.findall("I went to him at 11 a.m on 18th april 2025"))


result = re.compile('ab*')
print(result.findall("ababbabbbabbbb"))


def validate_email(email):
    reg_email = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(reg_email,email):
        return True
    return False
email = "abhijitdalavi1289@gmail.com"
print(validate_email(email))