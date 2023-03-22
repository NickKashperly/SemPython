dict = {"V ": "S001", " V": "S002", "VI": "S001",
        " VI ": "S005", "VII": "S005", "V": "S009", "VIII": "S007"}
a = set()
for item in dict:
    a.add(dict[item])
print(a)


# mass = input().split(", ")
# new_mass = []
# for i in mass:
#     if i not in new_mass:
#         new_mass.append(i)
# count = len(new_mass)
# print(count)


a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {" V ": " S009 "}, {" VIII": " S007 "}]
s = set()
for i in a:
    s.add(*i.values())

print(*s)


data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
    "VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]  # список
print(data)
result_set = set()
for elem in data:
    for value in elem.values():
        result_set.add(value.strip())
print(result_set)
