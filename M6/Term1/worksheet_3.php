<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ผลลัพธ์ PHP</title>
    <style>
        .container {
            display: flex;
            gap: 100px; 
            font-family: sans-serif;
            font-size: 18px;
        }
        h3 {
            margin-bottom: 20px;
        }
        p {
            margin: 10px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <div>
        <h3>ผลลัพธ์</h3>
        <?php
        $a = 3;
        $b = 4;
        $sum = $a + $b;

        echo "<p>ค่าของ \$a คือ $a</p>";
        echo "<p>ค่าของ \$b คือ $b</p>";
        echo "<p>ผลรวมของ \$a และ \$b คือ $sum</p>";
        ?>
    </div>

    <div>
        <h3>ผลลัพธ์</h3>
        <?php
        $A = "B";
        $$A = 20.5; 

        echo "<p>\$A=$A</p>";
        echo "<p>\$\$A=" . $$A . "</p>";
        echo "<p>\$B=$B</p>";
        ?>
    </div>
</div>

</body>
</html>
