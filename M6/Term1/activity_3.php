<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>while loop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .box {
            background-color: #f4f4f9;
            padding: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <div class="box">
        <h2>1. แปลงค่าองศาเซลเซียส (C) เป็นฟาเรนไฮต์ (F) ด้วย While Loop</h2>
        <ul>
        <?php
            $celsius = 0; 
            while ($celsius <= 50) {
                $fahrenheit = ($celsius * 1.8) + 32;
                echo "<li>{$celsius} องศาเซลเซียส = {$fahrenheit} องศาฟาเรนไฮต์</li>";
                $celsius += 10; 
            }
        ?>
        </ul>
    </div>

    <div class="box">
        <h2>2. แสดงเลขคู่ตั้งแต่ 2 ถึง 20 ด้วย Do While Loop</h2>
        <p>ผลลัพธ์: 
        <?php
            $number = 2;
            do {
                echo $number . " "; 
                $number += 2; 
            } while ($number <= 20);
        ?>
        </p>
    </div>

</body>
</html>