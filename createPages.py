import webbrowser

HEADER = "<!DOCTYPE html>"

STYLE = """ <style>
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

    def validated_appraiser_page(uname, psw):
        p_name = 'pages/appraiserSpace.html'
        with open (p_name, 'w', encoding="utf-8") as current_page:
            page = """<!DOCTYPE html>
            <html>
                <!--how will the page look-->"""
            
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
                    document.cookie = "username = {uname}; type = appriaser;"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)

    def create_client_main(data):
        return  f"""<div class="main">
                        <h1>HELLO {data}</h1>
                    </div>"""
    
    def validated_client_page(data):
        print("name: ",data)
        p_name = 'pages/clientSpace.html'
        with open (p_name, 'w', encoding="utf-8") as current_page:
            page = """<!DOCTYPE html>
                <html>
                <!--how will the page look-->
            """
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
            page += CreatePages.create_client_main(data)
            page += f"""</body>
                <script>
                    <!--document.cookie = -->
                    document.cookie = "username = {data}; type = client;"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)
    
    