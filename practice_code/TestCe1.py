d = {
    1: 'a',
    2: 'b',
    3: 'c'
}

for a, b in d.items():
    print('{}={}'.format(a, b))

b = """ nihao weishenme bu keyi shuchu yixilie :
        %(name)s
        %(age)d
        %(high)f"""
print(b % dict(name="whoimi", age=25, high=2.34))

name = "whoimi"
age = 25
high = 2.34
t = f""" nihao weishenme bu keyi shuchu yixilie :
        name={name}
        age={age}
        high={high}"""
print("=====>" + t)
