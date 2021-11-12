import re
my_str = '''Write a regular expression that
 can find all amounts of money in a text. Your 
 expression should be able to deal with different formats 
 and currencies, for example £50,000 and £117.83m as well as 300p, 
 500m euro, 338bn euros, $150bn and $92.88. Make sure that 
 you can at least detect amounts in Pounds, Dollars and Euros, and $100m with that 100p'''

#patt = re.compile(r'\$?\d{1,}\.\d{2}')
#patt = re.compile(r'\d+(?:\.\d+)?')
patt = re.compile(r'\d+(?:.(\d+))+((?:(m)+)|(?:(bn)+)|(?:(p)+))?')
matches = patt.finditer(my_str)
for match in matches : 
    print(match)