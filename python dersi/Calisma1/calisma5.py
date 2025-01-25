import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
import sys

mesaj = MIMEMultipart() # mail yapimizi olusturuyoruz.
mesaj["From"] = "aysegul.tekes91@erzurum.edu.tr" # kimden gonderecegimiz
mesaj["To"] = "aysett.ta@gmail.com" # kime gonderecegimiz
mesaj["Subject"] = "Smtp Mail Gonderme" #Mailimizin konusu

yazi = """
Merhaba, 
Python ile ilk gonderdigim buuuuu.
Bu dünya sıkı giyinsin gidiyorum senden

Aysegul Tekes
"""

mesajGovdesi = MIMEText(yazi,"plain")#Mailimizin govdesi bu siniftan olusturulur
mesaj.attach(mesajGovdesi) # Mailimizin gövdesini mail yapımıza ekliyoruz.

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.

    mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.

    mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli

    mail.login("aysegul.tekes91@erzurum.edu.tr",
               "Aa210682Aa2")  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.
    print("Mail başarıyla gönderildi....")
    mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

except:
    sys.stderr.write(
        "Mail göndermesi başarısız oldu...")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
    sys.stderr.flush()