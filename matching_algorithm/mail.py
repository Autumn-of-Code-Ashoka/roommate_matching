import json
import smtplib, ssl

def mail(pair_data):
    # modify this code to email the matches!
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"  # Enter your address
    receiver_email = "your@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = f"""\
    Subject: Hi there

    {pair_data}."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

rel = 'matches/'
with open(rel+'matches.json','r') as json_file:
    data = json.load(json_file)

# first of each pair as the senders
senders_1_cc = [[name_tag.split(':')[1] for name_tag in pair] for _,pair in data.items()]
# second of each pair as the senders
senders_2_cc = [[name_tag.split(':')[1] for name_tag in pair][::-1] for _,pair in data.items()]
print(senders_1_cc,senders_2_cc,sep='\n\n')

# for pair in [senders_1_cc,senders_2_cc]:
#   for elem in pair:
#       mail(elem)