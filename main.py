import smtplib

my_email = "alphalibrary9@gmail.com"  #
password_ = "avhcukyaegclyegj"  # app password generated

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password_)
    connection.sendmail(from_addr=my_email, to_addrs="swanhtet102002@gmail.com", msg="hello")
    connection.close()


