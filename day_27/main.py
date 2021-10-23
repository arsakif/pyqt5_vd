import smtplib

my_email = 'ars.akif@gmail.com'
password = '1542Aa01'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs='akifa81@gmail.com', msg='Hello')