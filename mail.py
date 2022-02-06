import smtplib

MY_EMAIL = "my@mail.com"
MY_PASSWORD = "my_pass"
MY_SMTP = "my.smtp.com"
MY_PORT = 123

REC_EMAIL = "their@mail.com"


def send_mail(title, data):
    subject = title

    for i in data:
        title = i[0]
        body = i[1]
        url = i[2]
        message = f"Headline: {title}\nBrief: {body}\n{url}"

        with smtplib.SMTP(MY_SMTP, port=MY_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=REC_EMAIL,
                                msg=f"Subject:{subject}\n\n"
                                    f"{message}".encode("utf8"))

        print(f"Mail {data.index(i) + 1}/{len(data)} sent.")
