# -------------------------------------
# 4. 날짜 / 시간 관련 기능
# --------------------------------------
import datetime as dt
now_time = dt.datetime.now()
now_str = now_time.strftime("%y-%m-%d %H:%M:%S")

print(now_time. strftime("%y-%m-%d %H:%M:%S"))
print(now_time. strftime("%y년 %m월 %d일 %H시 %M분 %S초"))

# 날짜 형식의 문자열을 날짜 객체로 변환 --------------
date_str = "2017년 01월 02일 14시 44분" #문자열에 대한 날짜 형식을 지정하면 문자열에서 날짜 성분을 추출하여 객체 생성
oldday = dt.datetime.strptime(date_str, "%Y년 %m월 %d일 %H시 %M분")
print(oldday.strftime("%y-%m-%d %H: %M: %S"))


# 날짜 객체에서 특정 값 변경 -----------------------
foo = dt.datetime.now()
print(foo.strftime("%y-%m-%d %H:%M:%S"))
change_date = foo.replace(year=2018, day =16, hour=15)
print(change_date.strftime("%y-%m-%d %H:%M:%S"))

# 두 날짜 간의 차이 계산
dt1 = dt.datetime.now()
dt2 = dt.datetime(dt1.year+1,1,1,0,0,0)
td = dt1-dt2
print(td)

# timedelta 객체의 프로퍼티 -------------------------
print(td.days)
print(td.seconds)
print("올해는 %d일 남았습니다." %td.days)

result = td.total_seconds()
print(result)

# 몇일 후의 날짜 계산_ timedelta
d =dt.timedelta(days=100, seconds=3600)
now_time = dt.datetime.now()
after_time = now_time + d
print(after_time.strftime("%Y-%m-%d %H:%M:%S"))