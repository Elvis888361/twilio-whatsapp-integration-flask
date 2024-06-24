# from twilio.rest import Client

# account_sid = '##'
# auth_token = '##'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   body='Hello from Python!',
#   to='whatsapp:+254745638455'
# ) http://127.0.0.1:4040       https://0172-105-163-2-96.ngrok-free.app             

# print(message.sid)
# from flask import Flask, request, jsonify
# from twilio.twiml.messaging_response import MessagingResponse
# import requests

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Welcome to the WhatsApp integration with Flask!'

# @app.route('/favicon.ico')
# def favicon():
#     return '', 204

# @app.route('/whatsapp', methods=['POST'])
# def whatsapp_reply():
#     incoming_msg = request.values.get('Body', '').lower()
#     num_media = int(request.values.get('NumMedia', 0))
#     response = MessagingResponse()
#     msg = response.message()

#     if num_media > 0:
#         media_url = request.values.get('MediaUrl0')
#         media_type = request.values.get('MediaContentType0')
        
#         # Download the media
#         media_response = requests.get(media_url)
#         with open(f'image.{media_type.split("/")[1]}', 'wb') as f:
#             f.write(media_response.content)
        
#         msg.body('Thanks for the image!')
#         print("image")
#     else:
#         if 'hello' in incoming_msg:
#             msg.body('Hi there!')
#         else:
#             msg.body('I am not sure how to respond to that.')

#     return str(response)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import requests
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the WhatsApp integration with Flask!'

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    num_media = int(request.values.get('NumMedia', 0))
    response = MessagingResponse()
    msg = response.message()

    if num_media > 0:
        media_url = request.values.get('MediaUrl0')
        media_type = request.values.get('MediaContentType0')

        if media_type == 'application/pdf':
            media_response = requests.get(media_url)
            with open('document.pdf', 'wb') as f:
                f.write(media_response.content)
            
            msg.body('Thanks for the PDF!')
            print("pdf")
        else:
            msg.body('I can only process PDF files right now.')
    elif num_media > 0:
        media_url = request.values.get('MediaUrl0')
        media_type = request.values.get('MediaContentType0')

        media_response = requests.get(media_url)
        with open(f'image.{media_type.split("/")[1]}', 'wb') as f:
            f.write(media_response.content)
        
        msg.body('Thanks for the image!')
        print("image")
    else:
        if 'hello' in incoming_msg:
            msg.body('Hi there!')
        else:
            msg.body('I am not sure how to respond to that.')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

