def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Invalid unit"


value = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

result = convert_temperature(value, unit)

print("Result:", result)


circle_area = lambda radius: 3.14 * radius ** 2

radius = float(input("Enter radius: "))

result = circle_area(radius)

print("Area of the circle:", result)