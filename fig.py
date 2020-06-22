f = input ()
if f == "треугольник":
    a = int(input ())
    b = int(input ())
    c = int(input ())
    p =  0.5 * ( a + b + c)
    print ((p *( p -a ) * (p-b) * (p-c)) ** 0.5)
if f == "прямоугольник":
    a = int(input ())
    b = int(input ())
    print (float(a * b))
if f == "круг":
    a = int(input ())
    p = 3.14
    print (a * a * p)

    