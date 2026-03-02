# US Population
# Samuel Renneke, 3/1/2026
def main():

    all_entered_values = []
    while True:
        year = int(input("Enter the year: "))
        state = input("Enter the state: ")
        population = int(input("Enter the population: "))

        value = [year, state, population]

        all_entered_values.append(value)

        cont = input("Do you want to add more values? (y/n): ")
        if cont != "y":
            break

    year_to_sum = int(input("Enter the year you want population for: "))

    sum_population_for_year(all_entered_values, year_to_sum)


def sum_population_for_year(all_entered_values, year_to_sum):
    total_population = 0
    for i in all_entered_values:
        if i[0] == year_to_sum:
            total_population = total_population + i[2]
    print(total_population)

# Call the main function.
if __name__ == '__main__':
    main()
