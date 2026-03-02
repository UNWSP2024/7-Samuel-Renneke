#Rainfall
#Samuel Renneke, 3/1/2026
def rainfall_calculator():
    #creating list
    rain_list = []
    for i in range (12):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        rain_list.append(float(input(f"Enter the amount of rain in {months[i]}: ")))

    #math functions
    total_rain = sum(rain_list)
    average_rain = total_rain / 12
    highest_rain = max(rain_list)
    lowest_rain = min(rain_list)

    #printing
    print(total_rain)
    print(average_rain)
    print(highest_rain)
    print(lowest_rain)

rainfall_calculator()
