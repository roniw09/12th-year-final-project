import webbrowser
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
                         <a href="disconnet.html">התנתק</a>
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
                    </body>
                    <script>
                        if (document.cookie == null){
                            document.cookie = "guest=anonymous";
                        }
                        let x = document.cookie;
                            console.log("!!!!!!!!");
                            console.log(x);
                            console.log("!!!!!!!!");
                            
                    </script>
                </html>"""
            current_page.write(page)



    def validated_appraiser_page(uname, psw):
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
                        <a href="home.html">דף הבית</a>
                        <a href="disconnet.html">התנתק</a>
                    </div>
                    
                    <div class="main">
                        <h1>שלום, {uname}</h1>
                    </div>
                </body>
                <script>
                    <!--document.cookie = -->
                    document.cookie = "appraiser={uname};"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)

    def create_client_main(client):
        print(client)
        page = f"""<div class="main">
                            <h1>HELLO {client.GetFirstName()} {client.GetLastName()}</h1>"""
        if client.GetExeTime() == None:
            page += """
                    <a href="setDate.html"><button type="button">קבע תאריך</button></a>
            </form>
            </div>
                    """
        return page
    
    def validated_client_page(client):
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
                        <a href="home.html">דף הבית</a>
                        <a href="disconnet.html">התנתק</a>
                    </div>""" 
            page += CreatePages.create_client_main(client)
            page += f"""</body>
                <script>
                    <!--document.cookie = -->
                    document.cookie = "client={client.GetFirstName()} {client.GetLastName()};"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)
    
    