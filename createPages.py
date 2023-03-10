import webbrowser

HEADER = "<!DOCTYPE html>"


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
                <!--how will the page look-->
                <style>
                    .nav a {color:black;text-align: center; font-size: 20px; padding: 10px 10px;font-family: 'assistant';}
                    .main{position: relative; top: 10px;text-align: center;font-size: 25px;}
                    .main{position: relative; top: 10px; text-align:center;font-family: assistant;}
                </style>

                <meta charset="utf-8">
            """
            page += f"""
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
                        <h1>HELLO</h1>
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
    
    def validated_client_page(name):
        print(name)
        p_name = 'pages/clientSpace.html'
        with open (p_name, 'w', encoding="utf-8") as current_page:
            page = """<!DOCTYPE html>
                <html>
                <!--how will the page look-->
                <style>
                    .nav a {color:black;text-align: center; font-size: 20px; padding: 10px 10px;font-family: 'assistant';}
                    .main{position: relative; top: 10px;text-align: center;font-size: 25px;}
                    .main{position: relative; top: 10px; text-align:center;font-family: assistant;}
                </style>

                <meta charset="utf-8">
            """
            page += f"""
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
                        <h1>HELLO {name}</h1>
                    </div>
                </body>
                <script>
                    <!--document.cookie = -->
                    document.cookie = "username = {name}; type = client;"
                    let x = document.cookie
                    console.log(x)
                </script>
            </html>"""
            current_page.write(page)