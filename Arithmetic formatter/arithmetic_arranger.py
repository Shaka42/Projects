k = []
c = list()
count_limit = 0


def arithmetic_arranger(a, condition):
    if condition is True:
        try:
            for item in a:
                b = item.split(' ')
                b = tuple(b)
                k.append(b)
            if len(k) > 5:
                raise Exception("Too many problems to solve")
            for (v, d, f) in k:
                if d == "+" or d == "-":
                    pass
                else:
                    raise Exception("Operator must be + or -")
                if len(v) > 4 or len(f) > 4:
                    raise Exception("Error:The numbers should have maximum of 4 digits")
                else:
                    pass
                if d == "+":
                    result = int(v) + int(f)
                    x = ('  '+str(v)+'\n'+'+ '+str(f)+'\n-----\n'+' '+str(result))
                    x = ''.join(x)
                    c.append(x)
                elif d == '-':
                    result = int(v) - int(f)
                    x = ('  '+str(v)+'\n'+'-'+str(f)+'\n-----\n'+' ', str(result))
                    x = ''.join(x)
                    c.append(x)
            line_lists = [item.splitlines()for item in c]
            line1 = zip(*line_lists)
            for lines in line1:
                print("".join('{:>8}'.format(line) for line in lines))
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(e)

