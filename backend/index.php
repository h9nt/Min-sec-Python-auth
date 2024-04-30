<?php
header('Content-Type: application/json');
include_once("utils/__init__.php");
error_reporting(E_ALL);
ini_set('display_errors', 1);

# made with <3 by @Fhivo aka vardxg on Telegram!

# - Host me on a localhost / server etc works on any hosting where u can host php!

if ($_SERVER['REQUEST_METHOD'] != "POST") {
    http_response_code(405);
    exit;
}


$hwid = $_POST['hwid'];
if (empty($hwid)) {
    http_response_code(400);
    echo json_encode([
        'error' => true,
        'now' => time() * 1000
    ]);
    exit;
} else {
    $decrypted_hwid = vardxg::xor_decode($hwid, "your_sec_key");

    $blocked = [
        '127.0.0.1',
        'localhost',
    ];

    if (in_array($_SERVER['REMOTE_ADDR'], $blocked)) {
        http_response_code(401);
        echo json_encode([
            'error' => true,
            'message' => 'u got blocked try again!',
            'now' => time() * 1000
        ]);
        exit;
    } else {

    }
    
    $paid_clients = [
        ''
    ];

    if (!in_array($decrypted_hwid, $paid_clients)) {
        http_response_code(403);
        echo json_encode([
            'status' => false,
            'message' => "no access",
            'now' => time() * 1000
        ]);
        exit;
    } else {
        http_response_code(201);
        echo json_encode([
            'status' => true,
            'message' => "welcome back: $decrypted_hwid",
            'now' => time() * 1000
        ]);
        exit;
    }
}

?>
