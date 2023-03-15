<?php

// Imposta l'URL del sito WordPress e l'endpoint REST API
$site_url = 'http://tuosito.com';
$rest_api_endpoint = '/wp-json/wp/v2/posts';

// Imposta il titolo e il contenuto del post
$post_title = 'Titolo del post';
$post_content = 'Contenuto del post';

// Imposta i dati del post da inviare tramite la REST API
$data = array(
    'title' => $post_title,
    'content' => $post_content,
    'status' => 'publish'
);

// Converti i dati in formato JSON
$json_data = json_encode($data);

// Imposta le opzioni della richiesta HTTP
$options = array(
    'http' => array(
        'method' => 'POST',
        'header' => "Content-type: application/json\r\n",
        'content' => $json_data
    )
);

// Crea il contesto della richiesta HTTP
$context = stream_context_create($options);

// Invia la richiesta HTTP alla REST API di WordPress per creare il post
$response = file_get_contents($site_url . $rest_api_endpoint, false, $context);

// Stampa la risposta della REST API di WordPress
echo $response;
