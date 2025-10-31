import time
import datetime as dt
from mylibrary import MyMailer
import concurrent.futures as futures

import random
def randomwork(name):
    randomSecond = random.randrange(1,9)
    print("[%s]작업을 %d초 동안 수행합니다." %(name, randomSecond))
    for i in range(0,randomSecond):
        time.sleep(1)
        print("[%s] %d초..." %(name, i+1))
    print("[%s] 작업이 종료되었습니다." %name)
    return randomSecond

startTime = dt.datetime.now()
names = ['Lee', 'Kim', 'Hong', 'Park', 'Nam']
processes = []
resultSet = []

with futures.ThreadPoolExecutor(max_workers=4) as executor:

    for n in names:
        pro = executor.submit(randomwork,n)
        processes.append(pro)
    for p in processes:
        result = p.result()
        resultSet.append(result)
print("비동기 처리가 총 %d초의 작업을 수행하였습니다." %sum(resultSet))

