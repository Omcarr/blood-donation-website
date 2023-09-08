import smtplib
import json

with open("keys.json", "r") as secret_keys:
 data = json.load(secret_keys)

def mail_sender(to_address_email,message):
 with smtplib.SMTP("smtp.gmail.com") as mail_sender:
  mail_sender.starttls()
  mail_sender.login(user=data["mail_id"],password=data["pass_word"])
  mail_sender.sendmail(from_addr=data["mail_id"],to_addrs=to_address_email,msg=message)

def thanks_donors(NAME,donor_mail):
 with open('MAILS//thanks_to_donor.txt') as letter:
  letter=letter.read()
  letter=letter.replace('[Donors Name]',NAME)
  #mail_sender('donors address from databse',message=letter)
  mail_sender(donor_mail,message=f'Subject:Thank you for registering donorhere!!!\n\n'+letter)

thanks_donors(NAME='',donor_mail='')