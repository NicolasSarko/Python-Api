#Bonjour à toi Alexandre et bienvenue sur ce rendu, je te laisse découvrir mon travail ci-dessous

#Je te fait un récap dans une petite documentation comme tu me l'as demandé

#Avant toute chose, j'importe requests pour faire des requetes http, json pour les reponses

import requests, json

#A ce stade ci, il fallais que je crée mon api key via la docs de twitch
#il a fallu que je mette le 2FA pour pouvoir crée et manager une application
#En suivant la documentation api twitch, il a fallu que je crée ma clé Client ID et mon access token

#Je t'invite à faire de même sur twitchtokengenerator.com et à te crée un compte dev(que tu as déjà fait) sur twitch 

#J'ai aussi récupérer la data sur helix

BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-ID': 'gp762nuuoqcoxypju8c569th9wz7q5', 'Authorization': 'Bearer ox3n4o47gblva1rgegxfwxi0gjlzft',"Accept":"aaplication/vnd.v5+json"}
INDENT = 2

#J'ai évidemment supprimer mon Client-ID et mon acces token pour pas que tu aies accès à mes données twitch *insert smyley qui rigole*

# Je récupère ici ma réponse de mon appel API
def get_response(query):
  url  = BASE_URL + query
  response = requests.get(url, headers=HEADERS)
  return response

# je print ensuite ma reponse dans un json
def print_response(response):
  response_json = response.json()
  print_response = json.dumps(response_json, indent=INDENT)
  print(print_response)

# je crée ensuite mes query 
# Dans un premier temps je récupère l'user, sa description, son compteur de vue et ses vidéos
def get_user_streams_query(user_login):
    return 'streams?user_login={0}'.format(user_login)

def get_user_query(user_login):
    return 'users?login={0}'.format(user_login)

def get_user_videos_query(user_id):
    return 'videos?user_id={0}&first=50'.format(user_id)

def get_user_description_query(user_id):
    return 'description?user_description={0}'.format(user_description)

def get_user_viewcount_query(user_id):
    return 'viewcount?user_viewcount={0}'.format(user_viewcount)

#Pour pouvoir prendre en paramètre les informations sensibles de Solary, il me faut leurs autorisation
#Or, cet autorisation s'obtient via le token OpenID Connect Protocol qui permettrais de vérifié l'indentité de l'user
# et d'accèder aux informations basiques du profil en question 

#Imaginons que nous avons un accès user, je simule les informations sensibles que je peut avoir comme par exemple son adresse email perso

def get_user_email(user_id):
    return 'email?user_email={0}'.format(user_email)

