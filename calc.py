# calc.py
import math

def calculate(current_value, num, clear):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == 'sqrt':
            try:
                # Safely evaluate the current expression
                return current_value + num
            except:
                return 'Error'
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                if "√" in current_value:
                    # Get the index of the sqrt sign
                    sqrtindex = current_value.index("√(")+2
                    # Find the value of everything after the sqrt value
                    sqrtRes = str(math.sqrt(eval(current_value[sqrtindex:])))
                    # Find the value of everything before the sqrt value and the sqrt value
                    return str(eval(current_value[:(sqrtindex-2)]+sqrtRes))
                else:
                    return str(eval(current_value))
            except ValueError as e:
                print(e)
        else:
            # Append the pressed button value to the current value
            return current_value + num
    return current_value
