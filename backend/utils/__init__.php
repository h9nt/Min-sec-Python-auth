<?php

class vardxg {
    public static function xor_encode($string, $key) {
        $result = '';
        for ($i = 0; $i < strlen($string); $i++) {
            $result .= chr(ord($string[$i]) ^ ord($key[$i % strlen($key)]));
        }
        return base64_encode($result);
    }

    public static function xor_decode($string, $key) {
        $decoded_string = base64_decode($string);
        $result = '';
        for ($i = 0; $i < strlen($decoded_string); $i++) {
            $result .= chr(ord($decoded_string[$i]) ^ ord($key[$i % strlen($key)]));
        }
        return $result;
    }
}

?>
