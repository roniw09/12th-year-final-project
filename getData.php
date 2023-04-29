<?php
    $db = 'C:\Users\weiss4\Desktop\Roni\Cyber\12th-year-final-project\DemiDB.mdb';
    $db = new PDO("obcd:Driver={Microsoft Access Driver (*.mdb); DBQ = $db; Uid =; Pwd=;");
    $sql = "SELECT * FROM Clients";
    $res = $db ->query($sql);
    print_r($res->fetchAll());
?>