# ---------------------------------
# 메일 방송 기능
# -------------------------------
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# 메일 발송에 필요한 정보 설정 --------------------
from_addr = "ssoo.alter@gmail.com"
to_addr = "c_waterzero@naver.com"
subject = " 파이썬 메일 발송 테스트 "
content = """안녕하세요. 파이썬으로 발송하는 메일입니다,
잘 발송되는지 확인해 보도록 하겠습니다,
하나 둘 ~ 셋
"""
files = []

# SMTP 연동 정보 설정 -----------------------------
content_type = "plain"
username = "ssoo.alter@gmail.com"
password = "rkls keok wsam zduk"
smtp = "smtp.gmail.com"   #고정값
port = 587                #고정값



# 메일 발송 정보 구성 ------------------------------
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = from_addr
msg['To'] = to_addr

msg.attach(MIMEText(content, content_type))

mail = SMTP(smtp)
mail.ehlo
mail.starttls()
mail.login(username,password)
mail.sendmail(from_addr,to_addr,msg.as_string())
mail.quit
