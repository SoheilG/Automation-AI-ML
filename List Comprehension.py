readings = [22, 25, -99, 21, 28, -99, 24]


# clean_data = []
# for r in readings:
#     if r > 0:
#         clean_data.append(r)


# clean_data = [r for r in readings if r > 0]

# print(clean_data)




# employees = ["Alice", "Bob", "Charlie"]

# employee_map = {e: len(e) for e in employees}

# print(employee_map)


# try:
#     open("data.txt")
# except FileNotFoundError:
#     print("File not found!")\]



import os 
current_files = os.listdir(".")
folders_only = [f for f in current_files if "." not in f]