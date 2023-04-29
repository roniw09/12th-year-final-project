from usersClasses import Appraiser, Client
from ORM import * 


def build_chat(user):
    page = """<!DOCTYPE html>
    <html>
    <head>
        <title>Chat</title>
        <style>
        body {
            background-color: #b2b2b2;
            font-family: 'assistant';
        }
        /* Chat window styles */
        #chat-window {
            width: 100%;
            height: 500px;
            background-color: #fff;
            border: 1px solid #ccc;
            overflow: auto;
        }

        /* Input field styles */
        #chat-input {
            width: 100%;
            height: 50px;
            font-size: 16px;
            padding: 10px;
            border: none;
            border-top: 1px solid #ccc;
        }

        /* Message styles */
        .message {
            padding: 10px;
            margin: 5px;
            background-color: #f1f0f0;
            border-radius: 5px;
        }

        /* Sender styles */
        .sender {
            font-weight: bold;
            color: blue;
        }
        </style>
    </head>
    <body>
        <div class="nav">
            <a href="home.html">התנתק</a>
        </div>
        <div id="chat-window"></div>
        <form>
        """
    rec_type = ''
    options = []
    print(type(user))
    if type(user) == Appraiser:
        rec_type = 'cli'
        options, names = ORM.get_app_clients(user)
    else:
        rec_type = 'agent'
        options, names = ORM.get_client_app(user)
    page += f"""<select name="{rec_type}">"""

    for x in range(len(options)):
        page += f"""<option value="{options[x]}">{names[x]}</option>"""
        
    page += """
        </select>
        <input type="text" name="msgcon" id="chat-input" placeholder="Type your message...">
        <button type="submit" onclick="sendMessage()">Send</button>
        </form>
        
        <script>
        function sendMessage() {
            const message = document.getElementById('chat-input').value;
            const chatWindow = document.getElementById('chat-window');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'message';
            messageDiv.innerHTML = `<span class="sender">You:</span> ${message}`;
            chatWindow.appendChild(messageDiv);
        }
        </script>
    </body>
    </html>
    """
    return page

def update_send_msg(who_to, msg, cookie):
    print (who_to, msg, cookie)
    ORM.save_msg(who_to[1], cookie[1].split('=')[1], msg)
    if who_to[0] == 'cli':
        pass
    pass