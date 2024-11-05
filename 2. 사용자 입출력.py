입력,출력을 공부해보자!

우리들이 사용하는 대부분의 완성된 프로그램은 사용자 입력에 따라 그에 맞는 출력을 내보낸다. 
대표적인 예로 게시판에 글을 작성한 후 [확인] 버튼을 눌러야만(입력) 우리가 작성한 글이 게시판에 올라가는(출력) 것을 들 수 있다.

사용자 입력 활용하기

1. input사용하기.

message = input()
=>아 집가고싶다.
message
아 집가고싶다.

input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장한다.

프롬프트를 띄워 사용자 입력받기
사용자에게 입력받을 때 ‘숫자를 입력하세요’나 ‘이름을 입력하세요’라는 안내 문구 또는 질문을 보여 주고 싶을 때가 있다. 
그럴 때는 input()의 괄호 안에 안내 문구를 입력하여 프롬프트를 띄워 주면 된다.

input("안내_문구")
이런 식으로

message = input("숫자를 입력하세요: ")
숫자를 입력하세요:

이런식으로 출력이 된다.

‘숫자를 입력하세요’라는 프롬프트에 3을 입력하면 변수 message에 값 3이 대입된다. 
print (message)로 출력해서 제대로 입력되었는지 확인해 보자.

message = input("숫자를 입력하세요: ")
숫자를 입력하세요: 3
print(message)
3

input은 입력되는 모든 것을 문자열로 취급하기 때문에 message는 숫자가 아닌 문자열이라는 것에 주의하자.
type(number)
<class 'str'>

print 자세히 알기

지금까지 우리가 사용한 print 문의 용도는 데이터를 출력하는 것이었다. 데이터를 출력하는 print 문의 사용 예는 다음과 같다.

py = 123
print(py)
123
thon = "Python"
print(thon)
Python
py_1 = [1, 2, 3]
print(py_1)
[1, 2, 3]

이제 print 문으로 할 수 있는 일에 대해서 좀 더 자세하게 알아보자.

큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("my" "life" "is" "python")  # 1번
mylifeispython
print("my"+"life"+"is"+"python")  # 2번
mylifeispython

=> 공백을 추가하려면
print("my","life","is","python")
my life is python
또는
print("my ""life ""is ""python")
이런식으로 문자에 공백을 넣으면 된다.

한 줄에 결괏값 출력하기
for 문을 공부할 때 만들었던 구구단 프로그램에서 보았듯이 한 줄에 결괏값을 계속 이어서 출력하려면 
매개변수 end를 사용해 끝 문자를 지정해야 한다.

for i in range(10):
    print(i, end=' ')
0 1 2 3 4 5 6 7 8 9
end 매개변수의 초깃값은 줄바꿈(\n) 문자이다.












  




















  



