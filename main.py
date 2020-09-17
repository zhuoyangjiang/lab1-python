import sys
number = input("Enter temperature: ")
type_tem = input("Enter unit in F/f or C/c: ")
if type_tem == 'C' or type_tem == 'c':
    print(f'{number}° in Celsius is equivalent to { float(number)*1.8+32}° Fahrenheit.')
elif type_tem == 'F' or type_tem == 'f':
    print(f'{number}° in Fahrenheit is equivalent to { (float(number)-32)/1.8}° Celsius.')
else:
    print(f"Invalid unit({type_tem}).")
