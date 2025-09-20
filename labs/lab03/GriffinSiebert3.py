import sys;
import formulas;

def main():
    if (len(sys.argv) <= 1):
        print("Need to provide operator.")
        sys.exit(-1)
    elif (len(sys.argv) <= 3):
        print("Need to provide at least two values.")
        sys.exit(-1)
    else:
        operator = sys.argv[1]
        values = sys.argv[2:]

        valid_operations = ["add", "subtract", "multiply", "divide", "choose"]
        if (operator not in valid_operations):
            print("Valid operator names (add, subtract, multiply, divide, choose)")
            sys.exit(-1)
        else:
            for i in range(len(values)):
                values[i] = float(values[i])
            match operator:
                case "add":
                    val = formulas.add(values)
                    print("Answer = " + f"{val:.2f}")
                case "subtract":
                    val = formulas.subtract(values)
                    print("Answer = " + f"{val:.2f}")
                case "multiply":
                    val = formulas.multiply(values)
                    print("Answer = " + f"{val:.2f}")
                case "divide":
                    val = formulas.divide(values)
                    print("Answer = " + f"{val:.2f}")
                case "choose":
                    val = formulas.choose(values)
                    print("Answer = " + f"{val:.2f}")
                case _:
                    print("Valid operator names (add, subtract, multiply, divide, choose)")
                    sys.exit(-1)




if __name__ == '__main__':
    main()