for x in range(3):
 a=int(input('Enter the first number: '))
 b=int(input('Enter the second number: '))
 c=int(input('Enter the third number: '))
 if a>b and b>c:
    print(a,' is big')
    print(b,' is medium')
    print(c,' is small')
 elif a>c and c>b:    
    print(a,' is big')
    print(c,' is medium')
    print(b,' is small')
 elif b>a and a>c:
    print(b,' is big')
    print(a,' is medium')
    print(c,' is small')
 elif b>c and c>a:
    print(b,' is big')
    print(c,' is medium')
    print(a,' is small')
 elif c>b and b>a:
    print(c,' is big')
    print(b,' is medium')
    print(a,' is small')
 elif c>a and a>b:
    print(c,' is big')
    print(a,' is medium')
    print(b,' is small')
 elif a>b and b==c:
    print(a,' is big')
    print('The second and third numbers are equal')
 elif b>a and a==c:
    print(b,' is big')
    print('The first and third numbers are equal')
 elif c>a and a==b:
    print(c,' is big')
    print('The first and second numbers are equal')
 elif a<b and b==c:
    print(a,' is small')
    print('The second and third numbers are equal')
 elif b<a and a==c:
    print(b,' is small')
    print('The first and third numbers are equal')
 elif c<a and a==b:
    print(c,' is small')
    print('The first and second numbers are equal')
 else:
    print('They are all equal')
