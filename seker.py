def create_seker(client, cookie):
    """
        creates survey form
    """
    p_name = 'pages/sekerFill.html'
    with open (p_name, 'w', encoding="utf-8") as current_page:
        page = """
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <style>
                            body {font-family: Arial;}

                            /* Style the tab */
                            .tab {
                                overflow: hidden;
                                border: 1px solid #ccc;
                                background-color: #f1f1f1;
                            }

                            /* Style the buttons inside the tab */
                            .tab button {
                                background-color: inherit;
                                float: left;
                                border: none;
                                outline: none;
                                cursor: pointer;
                                padding: 14px 16px;
                                transition: 0.3s;
                                font-size: 17px;
                            }

                            /* Change background color of buttons on hover */
                            .tab button:hover {
                                background-color: #ddd;
                            }

                            /* Create an active/current tablink class */
                            .tab button.active {
                                background-color: #ccc;
                            }

                            /* Style the tab content */
                            .tabcontent {
                                display: none;
                                padding: 6px 12px;
                                border: 1px solid #ccc;
                                border-top: none;
                            }
                        </style>
                        <meta charset="utf-8">
                    </head>
                    <body>

                        <form  action="/appraiserSpace.html" id="seker"></form>

                        <div class="tab">
                            <button class="tablinks" onclick="openChapter(event, 'פרק 1')" id="defaultOpen">פרק</button>
                            <button class="tablinks" onclick="openChapter(event, 'פרק 2')">פרק 2</button>
                            <button class="tablinks" onclick="openChapter(event, 'פרק 3')">פרק 3</button>
                        </div>

                        <div id="פרק 1" class="tabcontent">"""
        page += f"""<select id="cli_id" name="cli_id" form="seker">
                        <option value="{client}" selected="selected">{client}</option>
                    </select>"""

        page += """<table text-align="right">
                    <tr>
                        <td>שם מוצר</td>
                        <td>מחיר</td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c1i1" form="seker"/></td>
                        <td><input type="number" name="c1i1value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c1i2" form="seker"/></td>
                        <td><input type="number" name="c1i2value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c1i3" form="seker"/></td>
                        <td><input type="number" name="c1i3value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c1i4" form="seker"/></td>
                        <td><input type="number" name="c1i4value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c1i5" form="seker"/></td>
                        <td><input type="number" name="c1i5value"  form="seker" /></td>
                    </tr>
                </table>  
            </div>

            <div id="פרק 2" class="tabcontent">
                <table text-align="right">
                    <tr>
                        <td>שם מוצר</td>
                        <td>מחיר</td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c2i1" form="seker"/></td>
                        <td><input type="number" name="c2i1value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c2i2" form="seker"/></td>
                        <td><input type="number" name="c2i2value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c2i3" form="seker"/></td>
                        <td><input type="number" name="c2i3value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c2i4" form="seker"/></td>
                        <td><input type="number" name="c2i4value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c2i5" form="seker"/></td>
                        <td><input type="number" name="c4i5value"  form="seker" /></td>
                    </tr>
                </table>  
            </div>

            <div id="פרק 3" class="tabcontent">
                <table text-align="right">
                    <tr>
                        <td>שם מוצר</td>
                        <td>מחיר</td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c3i1" form="seker"/></td>
                        <td><input type="number" name="c3i1value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c3i2" form="seker"/></td>
                        <td><input type="number" name="c3i2value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c3i3" form="seker"/></td>
                        <td><input type="number" name="c3i3value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c3i4" form="seker"/></td>
                        <td><input type="number" name="c3i4value"  form="seker" /></td>
                    </tr>
                    <tr>
                        <td><input type="text" name="c3i5" form="seker"/></td>
                        <td><input type="number" name="c3i5value"  form="seker" /></td>
                    </tr>
                </table>  
            </div>
            <button type="submit" form="seker">הגש טופס</button>

            <script>
                function openChapter(evt, chapterName) {
                var i, tabcontent, tablinks;
                tabcontent = document.getElementsByClassName("tabcontent");
                for (i = 0; i < tabcontent.length; i++) {
                    tabcontent[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tablinks");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }
                document.getElementById(chapterName).style.display = "block";
                    evt.currentTarget.className += " active";
                }

            
                let x = document.cookie
                console.log(x)
                </script>
                
                </body>
            </html> 
            """
        current_page.write(page)