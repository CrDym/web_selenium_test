# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 15:48
# @Author  : Cr
# @File    : function.py
from selenium import webdriver
import os
import smtplib
from BSTestRunner import BSTestRunner
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver,filename):
    func_path = os.path.dirname(__file__)
    print(func_path)

    base_dir = os.path.dirname(func_path)
    print(base_dir)

    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')

    print(base_dir)
    base = base_dir.split('/Website')[0]
    print(base)

    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)

def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    user = '739965647@qq.com'
    password = 'wlqhomaleimhbaia###'
    sender = '739965647@qq.com'
    receives = ['cher@govlan.com']
    subject = 'Web selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg["From"] = sender
    msg["To"] = ','.join(receives)

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    print('正在发送邮件>>>>>>>')
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("邮件已发出，请注意查收!")


def latest_report(report_dir):
    lists =os.listdir(report_dir)
    lists.sort(key=lambda fn: os.path.getmtime(report_dir + "\\" + fn))
    file = os.path.join(report_dir,lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
    insert_img(driver,'baidu.png')
    driver.quit()
