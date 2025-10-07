"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temperatures = [31, 30, 29, 28, 31, 32,]
    return temperatures

def analyze_temps(temp_list):
    avg_temp = 0
    hightest_temp = max(temp_list
    lowest_temp = min(temp_list)

    sum = 0
    for temp in temp_list:
        sum = sum + temp 
    avg_temp = sum / len(temp_list)
    return (avg_temp, hightest_temp, lowest_temp)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg} C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")

my_temps = get_temperatures()
analyze_temps = analyze_temps(my_temps)
display_analysis(analyze_temps[0], analyze_temps[1], analyze_temps[2])