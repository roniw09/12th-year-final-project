import chat
from usersClasses import *

HEADER = "<!DOCTYPE html>"

STYLE = """ <!--how will the page look-->
        <style>
        body {
            background-color: #b2b2b2;
            height: 500px;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
        }
        .nav a {color:black;text-align: right; font-size: 20px; padding: 10px 10px;font-family: 'assistant';}
        .main{position: relative; top: 10px;text-align: center;font-size: 25px; font-family: assistant; }
        .main h1{position: relative; top: 10px; text-align:center;}
        .contact{position: relative;text-align: right;font-size: 25px; font-family: assistant;}
    </style>"""


class CreatePages:

    def clear_page(page):
        """
        clear last page
        """
        with open(page, 'w') as current_page:
            current_page.truncate(0)

    def validated_user_home(type):
        """
            creates homepage
        """
        p_name = "pages/validatedUserHome.html"
        with open(p_name, "w", encoding="utf-8") as current_page:
            nav = ''
            page =  """<!DOCTYPE html>
                    <html>""" + STYLE + """<head>
                    <title>יובי</title>    
                    </head>
                    <!--body: contains navigation bar and the main part, which contains some info about the team and a video-->
                    <body>"""
            if type =="client":
               nav = """<div class="nav">
                         <a href="disconnet.html">התנתק</a>
                         <a href="clientSpace.html>אזור אישי</a>
                         </div>"""
            else:
                nav = """<div class="nav">
                         <a href="disconnect.html">התנתק</a>
                         <a href="appraiserSpace.html>אזור אישי</a>
                         </div>"""
            page += nav
            page += """<div class="main">
                       </div>

                        <div class="contact">
                            <h2>פרטי ההתקשרות איתנו</h2>
                            <p>מספר טלפון: </p>
                            <p>email: uvgo2014@gmail.com </p>
                        </div>
                    </body>"""
            page += """ <script>
                    <!--document.cookie = -->
                    function deleteAllCookies() {
                        cookies = document.cookie.split(";");
                        
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i];
                            const eqPos = cookie.indexOf("=");
                            const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
                        }
                    }"""
            page += f"""
                    deleteAllCookies()
                </html>"""
            current_page.write(page)



    def validated_appraiser_page(user):
        """
            creates the appraiser page after validation
        """
        p_name = 'pages/appraiserSpace.html'
        with open (p_name, 'w', encoding="utf-8") as current_page:
            page = """<!DOCTYPE html>
            <html> """
            
            page += STYLE 
            page += f"""
                <meta charset="utf-8">
                <!--header-->
                <head>
                    <title>יובי</title>    
                </head>
                <!--body: contains navigation bar and the main part, which contains some info about the team and a video-->
                <body>

                    <div class="nav">
                        <a href="home.html">התנתק</a>
                    </div>
                    
                    <div class="main">
                        <h1>שלום, {user.GetName()}</h1>"""
            if user.GetSkarim() == None:
                page += """<h2> אין לך כרגע כלום! <h2>"""
            else:
                page += """<table border="2" style="width:50%; align-content: center; text-align: center">
                        <tr>
                            <th>שם</th>
                            <th>שעה</th>
                            <th>כתובת</th>
                            <th>מלא סקר</th>
                            <th>צ'אט</th>
                        </tr>"""
                for x in user.GetSkarim():
                    print(x)
                    add = f"{x[2]} {x[3]}, {x[1]}"
                    page += f"""
                    <tr>
                        <th>{x[0]}</th>
                        <th>{str(x[-1].hour).zfill(2)}:{str(x[-1].minute).zfill(2)}</th>
                        <th>{add}</th>
                        <th> <input type="button" onclick="window.location.href='sekerFill.html?id={x[0]}';" value="הכנס סקר" /></th>
                        <th><a href="chat.html?id={x[0]}">chat</a></th>
                    <tr>"""

            page += """</div>
            </body>
                <script>
                    <!--document.cookie = -->
                    function deleteAllCookies() {
                        cookies = document.cookie.split(";");
                        
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i];
                            const eqPos = cookie.indexOf("=");
                            const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
                        }
                    }"""
            page += f"""deleteAllCookies()
                    document.cookie = "appraiser={user.GetID()};"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)


    def create_client_main(client):
        """
            creates the clients main according to execute hour
        """
        print(client)
        page = f"""<div class="main">
                            <h1> שלום, {client.GetFirstName()} {client.GetLastName()}</h1>"""
        if client.GetExeTime() == None:
            page += """
                    <a href="setDate.html"><button type="button">קבע תאריך</button></a>
            </form>
            <a href="chat.html">chat</a>
            </div>"""
        else:
            page += f"""
            <p>תאריך נוכחי</p>
            <p>{client.GetExeTime()}</p>
            <a href="setDate.html"><button type="button">שנה תאריך</button></a>
            </form>
            <a href="chat.html">chat</a>
            </div>"""
        return page
    

    def validated_client_page(client):
        """
            creates the client page after validation
        """
        p_name = 'pages/clientSpace.html'
        with open (p_name, 'w', encoding="utf-8") as current_page:
            page = """<!DOCTYPE html>
                <html>"""
            page += STYLE + f"""
                <meta charset="utf-8">
                <!--header-->
                <head>
                    <title>יובי</title>    
                </head>
                <!--body: contains navigation bar and the main part, which contains some info about the team and a video-->
                <body>

                    <div class="nav">
                        <a href="home.html">התנתק</a>
                    </div>""" 
            page += CreatePages.create_client_main(client)
            page += """
            </body>
                <script>
                    <!--document.cookie = -->
                    function deleteAllCookies() {
                        cookies = document.cookie.split(";");
                        
                        for (let i = 0; i < cookies.length; i++) {
                            const cookie = cookies[i];
                            const eqPos = cookie.indexOf("=");
                            const name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
                            document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
                        }
                    }"""
            page += f"""deleteAllCookies()
                    document.cookie = "client={client.GetID()};"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)

    def go_chat(user, send_to):
        """
            creates chat
        """
        p_name = 'pages/chat.html'

        with open(p_name, 'w', encoding="utf-8") as current_page:
            page = chat.build_chat(user, send_to)
            current_page.write(page)
        return '/chat.html'
    
    