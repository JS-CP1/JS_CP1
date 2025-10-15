import re
import math
quadratic = input("What is your quadratic? (PUT IN STANDARD FORM)\n ")
terms = re.findall(r'[+-]?\s*[^+-]+', quadratic)
terms = [term.strip() for term in terms if term.strip()]
terms = [term[1:] if term.startswith('+') else term for term in terms]
print("Terms:", terms)
#CHECK IF FACTORABLE
if len(terms) > 4 or len(terms) < 2:
    print("This quadratic is not factorable over the integers.")
else:
    print("This quadratic may be factorable over the integers.")
    if len(terms) == 2:
        if 'x^2' in terms[0] and math.sqrt(terms[1]).is_integer() and terms[1] <= 0:
            c = math.sqrt(terms[1])
            if c == 0 and terms[1] == "x^2":
                print("The factors of this quadratic are (x)(x)")
            find factors of a and c
    elif len(terms) == 3:
        pass
    elif len(terms) == 4:
        pass
    else:
        print("This quadratic is not factorable over the integers.")