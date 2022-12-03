import math
from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)
@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__' :
    app.run()


'''
#sort with and without built in fuctions
a = [1,3,5,3,6,8,8]
a.sort()
b= list(set(a))

sort_list = []
print('second largest number = '+str(b[len(b)-2]))

while a:
    minimum = a[0]
    for x in a:
        if x< minimum:
            minimum = x
    sort_list.append(minimum)
    a.remove(minimum)

print(sort_list)

print(math.factorial(4))
num = 145
sum1 = 0
while (num >0):
    dig = num % 10
    sum1 = sum1+ math.factorial(dig)
    print(sum1)
    num = num // 10
print(sum1)

n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**len(a),a))
print(a)
print(b)


#prim number
a=int(input("Enter number: "))
k=0
print(a//2+1)
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")

# reverse a number and sum of digits in number
num = int(input('please enter number'))
rev = 0
dig_sum = 0
while (num >0):
    dig = num % 10
    rev = rev*10+ dig
    num = num // 10
    dig_sum = dig_sum+dig


print('ssk revese = '+str(rev))
print(dig_sum)

# average of a number
list1 = [1,2,4,5]
print( sum(list1)/len(list1))


list1 = [1,2,4,5]
print(list1 * 2)  # [1,2,4,5,1,2,4,5]


# copy of list
names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names1[2] = 'ssk'
names3[1] = 'Bob'

print(names1)
print(names2)
print(names3)
'''