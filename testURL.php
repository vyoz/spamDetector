<?php

$url = 'http://localhost:5000/predict'; // Replace with your actual API URL

$data = array(
    'text' => 'Q/微信5988 65779办理 毕业证+成 绩单 真实 留 信 认证100%可查'
);

$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data),
    ),
);

$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);

if ($response === false) {
    echo "Failed to call the web service.";
} else {
    $result = json_decode($response);
  
    if ($result === null) {
        echo "Failed to parse the JSON response.";
    } else {
        $predictedLabel = $result->predicted_label;
        echo "Predicted label: " . $predictedLabel;
    }
}

?>
