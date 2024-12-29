"""i: int=0
while i<5:
    print(i)
    i+=1
    break
else:
    print("success")
"""
#f string
"""i: int=1000000000
print(f'{i:_}')
print(f'{i:,}')
"""
"""var: str=" Ulaganathan "
print(f'{var:_>30}')
print(f'{var:#<30}')
print(f'{var:!^30}')
"""
from datetime import datetime
"""now: datetime = datetime.now()
print(f'{now:%d.%m.20%y || %H.%M.%S}')
print(f'{now:%c}')
print(f'{now:%I%p}') # AM | PM
"""
"""n: float = 12345.5437
print(n)
print(round(n, 2)) # OR use f string
print(f'Result: {n:.2f}')
print(f'Result: {n:.0f}')
print(f'Result: {n:.3f}')
print(f'Result: {n:,.3f}')
"""
a: int = 3
b: int = 10
Friend_Name: str = "Jayaraman"
print(f'a + b = {a + b}') # OR
print(f'{a + b = }')
print(f'{bool(a)}')
print(f'{Friend_Name = }')
