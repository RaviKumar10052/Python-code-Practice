import re
def studentid(identity):
    if re.search(r'^*[0-9]',identity):
        print("Valid Search")
    else:
        print("Invalid Search")


studentid("13235")