employee_names = [
    "Syren Vale",
    "Marcus Bennett",
    "Darius Cole",
    "Nadia Brooks",
    "Cameron Ellis",
    "Jordan Hayes",
    "Maya Carter",
    "Adrian Foster",
    "Talia Morgan",
    "Xavier Reed",
    "Kiara Bennett",
    "Devin Parker",
    "Amara Collins",
    "Isaiah Grant",
    "Elena Brooks",
]

departments = [
    "Executive",
    "Executive",
    "Executive",
    "Security",
    "Security",
    "Security",
    "Finance",
    "Finance",
    "Finance",
    "IT",
    "IT",
    "IT",
    "Operations",
    "Operations",
    "Operations",
]

syren = {"name": "Syren Vale", "department": "Executive"}

marcus = {"name": "Marcus Bennett", "department": "Executive"}

nadia = {"name": "Nadia Brooks", "department": "IT"}

print(syren["name"])
print(syren["department"])

print(marcus["name"])
print(marcus["department"])

print(nadia["name"])
print(nadia["department"])

print(syren.keys())
print(syren.values())
print(syren.items())

company = {
    "syren": {"name": "Syren Vale", "department": "Executive"},
    "marcus": {"name": "Marcus Bennett", "department": "Executive"},
    "nadia": {"name": "Nadia Brooks", "department": "IT"},
}

employees = [
    {"name": "Syren Vale", "department": "Executive", "active": True},
    {"name": "Marcus Bennett", "department": "Executive", "active": True},
    {"name": "Nadia Brooks", "department": "IT", "active": False},
]

print(employees[0]["name"])
print(employees[0]["department"])

print(employees[1]["name"])
print(employees[1]["department"])

for employee in employees:
    print(employee["name"], employee["department"])

for employee in employees:
    if employee["department"] == "Security":
        print(employee["name"], "works in Security")
    elif employee["department"] == "Executive":
        print(employee["name"], "works in Executive")
    else:
        print(employee["name"], "works somewhere else")

for employee in employees:
    if employee["active"] == True:
        print(employee["name"], "is active")
    else:
        print(employee["name"], "is inactive")

search_name = "Marcus Bennett"

for employee in employees:
    if employee["name"] == search_name:
        print(employee["name"], employee["department"])

while True:
    found = False

    search_name = input("Enter employee name or type 'exit': ")

    if search_name == "exit":
        break

    for employee in employees:
        if employee["name"] == search_name:
            found = True

            print("Employee found:")
            print("Name:", employee["name"])
            print("Department:", employee["department"])

            if employee["active"]:
                print("Status: Active.")
            else:
                print("Status: Inactive.")

    if found == False:
        print("Employee not found.")
