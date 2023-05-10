from usersClasses import Appraiser, Client
from ORM import * 


def build_chat(user, send_to):
    u_type = type(user)
    if u_type == 'Client':
        u_type = 'client'
    else: u_type = 'agent'
    c_name, prev = insert_msg(user)
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
        /* Sender styles */
        .reciever {
            font-weight: bold;
            color: green;
        }
        </style>
		<meta charset="utf-8">
    </head>
    <body>
        <div class="nav">
            <a href="home.html">התנתק</a>
        </div>
        <div id="chat-window">
        <div class="message">"""
    
    for x in prev:
        if u_type == x[-1]:
            u_name = 'You:'
            page += f'<span class="sender">{u_name} </span>{x[3]}<br>'
        else:
            u_name = c_name + ':'
            page += f'<span class="reciever">{u_name} </span>{x[3]}<br>'

    page += f"""
        </div>
        </div>
        <form>
        """
    rec_type = ''
    print(type(user))
    if type(user) == Appraiser:
        rec_type = 'cli'
    else:
        rec_type = 'agent'
    print(type(user), rec_type)
    page += f"""<select name="{rec_type}">"""
        
    page += f"""
                <input type="text" name="{rec_type}qq{send_to}qqmsgcon" id="chat-input" placeholder="Type your message...">"""
    page += """
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
    who_sent = ''
    if cookie[1].split('=')[0] == 'appraiser':
        who_sent = 'agent'
    else:
        who_sent = 'client'
    ORM.save_msg(who_to[1], cookie[1].split('=')[1], msg, who_sent)

def insert_msg(user):
    id = user.GetID()
    n, prev = ORM.get_user_msgs(id, type(user), )
    return n, prev
