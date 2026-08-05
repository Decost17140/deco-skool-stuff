<?php
// ดึงไฟล์เชื่อมต่อฐานข้อมูล
require_once 'connect.php';

// ดึงข้อมูลเรียงตาม ID เพื่อให้ชื่อของคุณขึ้นเป็นลำดับที่ 1
try {
    $stmt = $conn->prepare("SELECT * FROM students WHERE id =1");
    $stmt->execute();
    $students = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    echo "เกิดข้อผิดพลาดในการดึงข้อมูล: " . $e->getMessage();
    exit();
}
?>

<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ระบบจัดการข้อมูลนักศึกษา</title>
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables Bootstrap 5 CSS -->
    <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container py-5">
    <div class="card shadow-sm">
        <div class="card-header bg-primary text-white">
            <h4 class="mb-0">ตารางรายชื่อนักศึกษา</h4>
        </div>
        <div class="card-body">
            <table id="studentTable" class="table table-striped table-hover table-bordered w-100">
                <thead class="table-dark">
                    <tr>
                        <th class="text-center" style="width: 5%;">id</th>
                        <th style="width: 10%;">รหัสนักเรียน</th>
                        <th style="width: 10%;">Username</th>
                        <th style="width: 10%;">Password</th>
                        <th style="width: 5%;">คำนำหน้า</th>
                        <th style="width: 25%;">ชื่อ</th>
                        <th style="width: 25%;">นามสกุล</th>
                        <th style="width: 10%;">ชั้น</th>
                    </tr>
                </thead>
                <tbody>
                    <?php 
                    $no = 1; // ตัวแปรนับลำดับเลขที่
                    foreach ($students as $row): 
                    ?>
                        <tr <?= ($no === 1) ? 'class="table-warning fw-bold"' : ''; ?>>
                            <td class="text-center"><?= $no++; ?></td>
                            <td><?= htmlspecialchars($row['student_id']); ?></td>
                            <td><?= htmlspecialchars($row['username']); ?></td>
                            <td><?= htmlspecialchars($row['password']); ?></td>
                            <td><?= htmlspecialchars($row['title']); ?></td>
                            <td><?= htmlspecialchars($row['first_name']); ?></td>
                            <td><?= htmlspecialchars($row['last_name']); ?></td>
                            <td><?= htmlspecialchars($row['class']); ?></td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
            <button><a href = "decoz.php">View Gihub</a> </button>
        </div>
    </div>
</div>

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
<!-- Bootstrap 5 Bundle JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<!-- DataTables JS -->
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>

<script>
    $(document).ready(function() {
        $('#studentTable').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/th.json" // เมนูภาษาไทย
            },
            "pageLength": 10,
            "ordering": true
        });
    });
</script>

</body>
</html>
