names = ["Rana", "Amir", "Carey", "Phani", "Swapnith"]
new_names = [nam.upper() for nam in names if len(nam)<6]
print(new_names)