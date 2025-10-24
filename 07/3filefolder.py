# 현재 폴더 내의 하위 항목들의 이름을 리스트로 리턴받
import sys
import os

ls = os.listdir('/')
print(ls)

#특정 폴더나 피일이 존재하는지 확인 -> 상대경로일 경우 현재 소스파일 기준
k = os.path.exists('./hello')
print(k)

#절대경로 확인 -> 존재하지 않더라도 경로값은 확인 가능
print( os.path.abspath('./hello'))

# 폴더의 생성과 삭제 ---------------------
if os.path.exists('./hello') == False:
    #없다면 생성
    os.mkdir('./hello')
    print('hello 폴더를 생성했습니다.')
else:
    #있다면 삭제 --> 빈 폴더만 삭제 가능
    os.rmdir('./hello')
    print('hello 폴더를 삭제했습니다.')

# 파일이나 폴더 검색 -------------------------
import glob as gl
ls = gl.glob('*')   #*.ipynb, *2*
print(ls)

#폴더트리 생성 및 삭제 -----------------------
import shutil
if os.path.exists('python') == False:
    os.makedirs('python/test/hello/world', exist_ok=True)
    print('python 폴더와 하위 폴더들을 생성 했습니다.')
else:
    shutil.rmtree('python')
    print('python 폴더가 삭제되었습니다.')
# 파일의 복사 및 삭제 작업

