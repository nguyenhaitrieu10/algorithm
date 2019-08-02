import test
import postfix

s = "  -5.5  /2 + -3*(4/-8 -2)  "
s = postfix.calculate(s)
print(s)

