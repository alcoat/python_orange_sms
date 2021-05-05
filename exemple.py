import utils

AUTH_TOKEN = 'Your Auth Token'
message = "Your Message" # Your message
to='+243xxxxxxxxx' # Receiver
from_='+243xxxxxxxxx' # Sender ( your phone number )

sms = utils.SMS(AUTH_TOKEN)
res = sms.send(from_=from_, to=to, message=message)

print(res)  

if res.status_code == 201:
    print('AVERY THING RIGHT : ', res.text)
else:
    print('SAME THING WRONG')