#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171122greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai

#region bailam

import re


def greeting(hour_str):
  if hour_str:
    hour_str = hour_str.lower()
    l1 = re.findall('\d+', hour_str)
    l2 = re.findall('am|pm', hour_str)
    time = []
    for i in l1:
      time.append(i)
   
    if len(time)==0:
      return None
    elif len(time[0]) == 4:
      time.append(re.sub('\d','',time[0],2))
      time[0]=re.sub(time[1],'',time[0])

    n_hour = int(time[0])
    
    if len(l2)==1:
      if l2[0]=='pm':
        if n_hour!=12:
          n_hour+=12
      else:
        if n_hour==12:
          n_hour==0
    
    if len(time) == 2:
      n_minute = int(time[1])
      if n_minute==60:
        n_hour+=1
    
    if n_hour>=0 and n_hour<=11:
      return 'Good morning!'
    elif n_hour>=12 and n_hour<=17:
      return 'Good afternoon!'
    else:
      return 'Good evening!'
  return None


#endregion bailam
