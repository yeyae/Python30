#for문
#1.전형적인 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)

#2.다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for(first, last) in a:
    print(first + last)

#3.for문의 응용
#총 5명의 학생들이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오

marks = [90, 45, 20, 67, 80]
number = 0
for mark in marks:
    number = number + 1
if mark >= 60:
    print("%d번 학생은 합격입니다." % number)
else:
    print("%d번 학생은 불합격입니다." % number)