initial_limit = int(input("Initial limit: "))
final_limit = int(input("Final limit: "))

new_initial_limit = initial_limit

if initial_limit > final_limit:
    print("The initial limit must be smaller than the final limit!")
elif initial_limit == final_limit:
    print("Sum of numbers from", initial_limit, "till", final_limit)
    print(final_limit)
else:
    print("Sum of numbers from", initial_limit, "till", final_limit)
    while new_initial_limit != final_limit:
        new_initial_limit += 1 

        new_limit = initial_limit + new_initial_limit 
        initial_limit = new_limit

        print("+", new_initial_limit, "-->", new_limit)
