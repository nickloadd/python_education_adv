f = open('C:/Users/admin/PycharmProjects/repos/task.txt')
s = []
z = []
list = []
for line in f:
    z = []
    # print(line)
    s = line.split(",")
    z.append(s[1].strip())
    z.append(s[2].strip())
    list.append(z)

#print(kek)


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


print(email_gen(list))

# for i in s[1:]:
#     if (len(i) == 1):
#         print(line)
# print(line.split(","))
# z = line.split(",")
# for i in z:
#     print(i)
# s.append(z)
# print(s)
# print(len(s))

# print(s[2])
