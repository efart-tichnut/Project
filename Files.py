names_list=['efrat','yael','avital','tamar','noa','rachel','shira']

file_name=input("enter file name...")
file_name+='.txt'
# with open(file_name,"+at") as f:
#     for l in names_list:
#         f.write(l+'\n')
#         lines = f.readlines()
#         for index, l in enumerate(lines):
#             if index%2==0:
#                 print(index, l, end='')
f = open(file_name)
lines = f.readlines()
for index, line in enumerate(lines):
     if index%2==0:
         print(line, end='')
f.close()