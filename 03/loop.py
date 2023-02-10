#while loop
i = 1
while i <= 3 :
    print('meow')
    i = i + 1
#for loop
print("****************")
for i in range(3):
    print("meow")

#list
students = ["heroime", "harrry", "Ron"]
print(students[0])
#instead use forloop
for s in students:
    print(s)

#to iterate each as 0,1,2, then use range alwasy contains number so use len to put length
for i in range(len(students)):
    print(i+1, students[i])

#dictionaries   - used if you want to associate something with other ie. key value pairs
students = {
    "Heroime": "Gryffendor",
    "Robert": "California",
    "Harry": "Taska",
    "Drone": "Rambox"
}

for student in students:
    print(student)  # returns keys  only 

for student in students:
    print(student, students[student], sep=',')  # returns key & value
