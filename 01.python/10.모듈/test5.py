# 다른 디렉터에 있는 모듈을 불러오는 방법

# import mod3 : 다른 파일에 있어서 오류남. 

import sys

print(sys.path)
# path에 뜨는 경로들 중에서 불러오겠다

sys.path.append(r'C:\Project\01.python\10.모듈\tmp')

import mod3

print(sys.path)
print(mod3.add(mod3.PI,4.4))

