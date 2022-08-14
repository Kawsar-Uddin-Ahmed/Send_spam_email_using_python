#1.Login into Your(Sender) Gmail Account.
#2.then Go To MyAccount Section By visiting https://myaccount.google.com
#3.Then Open Security Tab from the left side.
#4.Then make 2-factor authentication active
#5.After activing 2-factor authentication . You will see in  https://myaccount.google.com that App Passwords option click on it.
#6.Select app as Mail and select your corresponding device. Then Click on Generate to create App Password.
#7.You are Done. Now your app Password is been created and You are now able to Use this password in Your SMTP.
import smtplib
try:
   a = input("Enter the sender mail : ")
   p = input("App password of sender : ")
   b = int(input("How many sender you want: "))
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.starttls()
   server.login(a,p) #sender email and its app password
   message = input("Enter the messagel : ")
   for i in range(0,b+1):
        rec = input("Enter the reciever mail : ")
        server.sendmail(a,rec,message) #server.sendmail("sender_mail","receiver_mail","message")

    #you will get the message in spam folder.
   server.quit()
except:
    print("Provide correct information")