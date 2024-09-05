import requests

# Impostare le informazioni dell'endpoint della REST API di WordPress
url = 'https://example.com/wp-json/wp/v2/posts'
headers = {'Content-Type': 'application/json'}
auth = ('username', 'password') # sostituire con le credenziali dell'utente autorizzato

# Impostare i dati del post da creare
data = {
    'title': 'Titolo del post',
    'content': 'Testo del post',
    'status': 'publish', # Stato del post, ad esempio: "publish", "draft", "pending", "private"
    'categories': [1, 2], # ID delle categorie del post, sostituire con gli ID delle categorie desiderate
    'tags': ['tag1', 'tag2'], # Etichette del post, sostituire con le etichette desiderate
    'meta': {
        'key1': 'valore1',
        'key2': 'valore2'
    } # Altri metadati del post, sostituire con i propri metadati
}

# Invio della richiesta POST alla REST API di WordPress
response = requests.post(url, headers=headers, auth=auth, json=data)

# Stampa della risposta della richiesta
print(response.json())
