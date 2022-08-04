total_members = 0

while total_members != 4:
    total_members += 1
    print("Information for member", total_members)
    name = str(input("Name: "))
    age = int(input("Age: "))
    member_for_how_many_years = int(input("Member for how many years: "))

    if member_for_how_many_years >= 5:
        if age < 12:
            discount = (20 / 100) * 10
            print("Member fee for", name, "=", 20 - discount)
        if age >= 12 and age <= 18:
            discount = (50 / 100) * 10
            print("Member fee for", name, "=", 50 - discount)
        if age > 18:
            discount = (95 / 100) * 10
            print("Member fee for", name, "=", 95 - discount)
    
    else:
        if age < 12:
            print("Member fee for", name, "= 20")
        if age >= 12 and age <= 18:
            print("Member fee for", name, "= 50")
        if age > 18:
            print("Member fee for", name, "= 95")
