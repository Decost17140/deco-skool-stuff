<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>ผลลัพธ์ PHP</title>
    <style>
        .container {
            display: flex;
            gap: 100px; /* ระยะห่างระหว่างคอลัมน์ */
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
        // กำหนดค่าตัวแปร
        $a = 3;
        $b = 4;
        $sum = $a + $b;

        // ใช้เครื่องหมาย \ หน้า $ เพื่อให้แสดงตัวอักษร $ ออกมาตรงๆ โดยไม่มองว่าเป็นตัวแปร
        echo "<p>ค่าของ \$a คือ $a</p>";
        echo "<p>ค่าของ \$b คือ $b</p>";
        echo "<p>ผลรวมของ \$a และ \$b คือ $sum</p>";
        ?>
    </div>

    <div>
        <h3>ผลลัพธ์</h3>
        <?php
        // กำหนดค่าตัวแปร $A
        $A = "B";
        
        // กำหนดค่า $$A ซึ่งจะนำค่าของ $A (คือ "B") มาสร้างเป็นตัวแปรใหม่ชื่อ $B
        $$A = 20.5; 

        echo "<p>\$A=$A</p>";
        echo "<p>\$\$A=" . $$A . "</p>";
        echo "<p>\$B=$B</p>"; // จะเห็นได้ว่าเราสามารถเรียกใช้ $B ได้เลย เพราะถูกสร้างมาจาก $$A แล้ว
        ?>
    </div>
</div>

</body>
</html>