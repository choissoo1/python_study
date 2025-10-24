#Mymod1.py 파일을 참조
from mylibrary import MyMod1
# 참조한 파일에 정의된 함수는 '파일리음.함수명'형식으로 접근
print(MyMod1.plus(3,4))
print(MyMod1.minus(3,4))

# ---------------------------------------------------------------

from mylibrary import MyMod2
# MyMod2에 정의된 Member라는 클래스에 "모듈이름.클래스이름"으로 접근
# -> import된 클래스는 정의된 기능을 다른 변수에 부여해야 사용 가능
#   ==> 객체
# -> 클래스에 생성자가 포함되어 있고 생성자가 파라미터를 갖는 경우
#    객체 생성시에 생성자 파라미터를 전달해야 함
mem = MyMod2.Member('파이썬 학생', 'ssoo.alter@gmail.com')
mem.view_info()

# -----------------------------------------------------------------
from mylibrary import MyMod3
#모듈안의 객체를 통해서 기능에 접근
print(MyMod3.my_clac.plus(30,15))
print(MyMod3.my_clac.minus(30,15))

#--------------------------------------------------------
from mylibrary import MyMod1 as hello
## [   별칭이름.함수명  ] 모듈에 포함된 기능들의  접근
print(hello.plus(3,4))
print(hello.minus(3,4))

#--------------------------
## [  별칭이름.클래스()   ]
# MyMod2 모듈에 User라는 별칭을 적용하여 import
from mylibrary import MyMod2 as User

mem = User.Member('파이썬 학생', 'ssoo.alter@gmail.com')
mem.view_info()

#----------------------------------
## [   별칭이름.객체명 ]
from mylibrary import MyMod3 as MyObject
print(MyObject.my_clac.plus(30,15))
print(MyObject.my_clac.minus(30,15))

# ----------------------------------
## 모듈 이름 없이 함수에 직접 접근
from mylibrary.MyMod1 import plus
#골라서 가져온 기능들은 앞에 모듈이름을 적용하지 않고,
#직접 접근
print(plus(3,4))
#minus 함수는 import 하지 않았으므로 사용 불가 --> 에러
#print(minus(3,4))
#--------------------------------------
## 모듈 이름 없이 함수에 직접 접근
# MyMod2 모듈에서 Member라는 이름의 기능만 지정해서 참조
from mylibrary.MyMod2 import Member
#from절로 특정 기능만 골라서 참조한 경우 모듈이름 없이 직접 접근.
# 참조된 기능이 클래스이므로, 객체로 생성해야만 사용가능.
mem = Member('파이썬 학생', 'ssoo.alter@gmail.com')
mem.view_info()