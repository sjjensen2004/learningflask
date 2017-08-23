from flask_mail import Message
from hello import mail
from hello import app
msg = Message('test subject', 
sender ='sjjensen2004@outlook.com',
recipients =['sjjensen2004@outlook.com'])
msg.body = 'text body'
msg.html = '<b> HTML </b> body'
with app.app_context():
	mail.send(msg)
