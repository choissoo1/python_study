import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
# --------------------------------
# 메일 발송 함수
# --------------------------------
def sendMail(from_addr, to_addr, subject, content, files=[] ):
    content_type = "plain"
    # 로그인 계정 이름(네이버=아이디, 구글 = 메일주소)
    username = "ssoo.alter@gmail.com"
    # 비밀번호(네이버=개인비밀번호, 애플리케이션 비밀번호, 구글=앱 비밀번호)
    password = "rkls keok wsam zduk"

    # 구글 발송 서버 주소와 포트(고정값)
    smtp = "smtp.gmail.com"   
    port = 587               
    # 네이버 발송 서버 주소와 포트(고정값)
#   smtp = "smtp.naver.com"
#   port = 465
    msg = MIMEMultipart()
    msg['Subject'] = subject  #메일 제목
    msg['From'] = from_addr   #보내는 사람
    msg['To'] = to_addr       #받는 사람

    msg.attach(MIMEText(content, content_type))

# ------------------------------
# 메일 발송 정보에 첨부파일 추가
# ---------------------------------
    if files:
        for file_item in files:
            if os.path.exists(file_item):
                #바이너리(b) 형식으로 읽기(r)
                with open(file_item,'rb') as f:
                    #전체 경로에서 파일의 이름만 추출
                    basename = os.path.basename(file_item)
                    #파일의 내용과 파일이름을 메일에 첨부할 형식으로 변환
                    part = MIMEApplication(f.read(),Name=basename)


                    #파일 첨부
                    part['Content-Disposition'] = 'attachment; filename="%s"' % basename
                    msg.attach(part)
                    print(basename,"(이)가 첨부되었습니다.")

    mail = SMTP(smtp)
    mail.ehlo()
    mail.starttls()
    mail.login(username,password)
    mail.sendmail(from_addr, to_addr, msg.as_string())  
    mail.quit()


# -------------------------
# 테스트 코드
# ---------------------------
if __name__ == "__main__":
    sendMail("ssoo.alter@gmail.com", "c_waterzero@naver.com", "메일 발송 모듈 테스트", "이것은 테스트 입니다.")

# ---------------------------
# 2. 메일링 리스트 구현
# ----------------------------
