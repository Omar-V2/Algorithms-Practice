def urlify(s):
    s_list = list(s.strip())
    for index, value in enumerate(s_list):
        if value == " ":
            s_list[index] = "%20"
    return "".join(s_list)

print(urlify("hi there"))
print(urlify("Mr John Smith    "))