프로그램의 입출력을 공부해보자.

명령 프롬프트를 사용해 본 독자라면 다음과 같은 명령어를 사용해 봤을 것이다.

C:\> type py_1.txt

type은 바로 뒤에 적힌 파일 이름을 인수로 받아 해당 파일의 내용을 출력해 주는 명령어이다. 
대부분의 명령 프롬프트에서 사용하는 명령어는 다음과 같이 인수를 전달하여 프로그램을 실행하는 방식을 따른다.

명령어 [인수1 인수2 ...]
이러한 기능을 파이썬 프로그램에도 적용할 수 있다.

sys 모듈 사용하기
파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있다. sys 모듈을 사용하려면 다음 예의 import sys처럼 import 명령어를 사용해야 한다.

# sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)

위는 프로그램 실행 시 전달받은 인수를 for 문을 사용해 차례대로 하나씩 출력하는 예이다. sys 모듈의 argv는 프로그램 실행 시 전달된 인수를 의미한다.
즉, 다음과 같이 입력했다면 argv[0]은 파일 이름 sys1.py가 되고 argv[1]부터는 뒤에 따라오는 인수가 차례대로 argv의 요소가 된다.

이 프로그램을 C:\doit 디렉터리에 저장한 후 인수를 전달하여 실행하면 다음과 같은 결과를 볼 수 있다.

명령 프롬프트를 열고 cd C:\doit 명령을 실행하여 C:\doit 디렉터리로 이동한 후 다음 명령을 실행해 보자.
C:\doit>python sys1.py aaa bbb ccc
aaa
bbb
ccc

# sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')

문자열 관련 함수인 upper()를 사용하여 프로그램 실행 시 전달된 인수를 모두 대문자로 바꾸어 주는 간단한 프로그램이다. 
명령 프롬프트 창에서 다음과 같이 실행해 보자.

sys2.py 파일이 C:\doit 디렉터리 안에 있어야만 한다.

C:\doit>python sys2.py life is too short, you need python

출력 결과는 다음과 같다.

LIFE IS TOO SHORT, YOU NEED PYTHON














