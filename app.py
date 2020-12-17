#Pour récupérer les données, j'ai suivi un tutoriel Flask sur internet
#Je ne connaissais pas du tout Flask avant, j'avais un peu travailler avec Django mais flask
# restait le plus facile à prendre en main.

#J'importe donc flask et ngrok qui me permette de run mon serveur en local
from flask import Flask, request, render_template, redirect, url_for
from flask_ngrok import run_with_ngrok
from wtforms import Form, StringField, validators
import data
import json, time, datetime

app = Flask(__name__)
app.debug = True


class InputForm(Form):
  user_login = StringField(validators=[validators.InputRequired()])

#J'ai dans un premier temps fais beaucoups de test pour déterminer mes query

@app.route('/', methods=['POST', 'GET'])
def home():
  form = InputForm(request.form)
  user_login = form.user_login.data

  user_query = data.get_user_query(user_login)
  user_info = data.get_response(user_query)

  data.print_response(user_info)
    
  try:

    #Créations de mes variables contenant les json de la data que je recherche
    user_id = user_info.json()['data'][0]['id']
    img_url = user_info.json()['data'][0]['profile_image_url']
    user_description = user_info.json()['data'][0]['description']
    user_viewcount = user_info.json()['data'][0]['view_count']

    #Exemple d'information sensible : L'email 
    #user_email = user_info.json()['data'][0]['email']


    user_videos_query = data.get_user_videos_query(user_id)
    videos_info = data.get_response(user_videos_query)
    
    data.print_response(videos_info)

    videos_info_json = videos_info.json()

    videos_info_json_data = videos_info_json['data']
    videos_info_json_data_reversed = videos_info_json_data[::-1]
    
    line_labels = []
    line_values = []
    title = 'Données de' +" "+ user_login

    #Je parcours ma liste d'item pour récupérer les noms des vidéos

    for item in videos_info_json_data_reversed:
      if (len(item['title']) == 0):
        line_labels.append('No Name')
      elif (len(item['title']) > 20):
        line_labels.append(item['title'][:20] + '...')
      else:
        line_labels.append(item['title'])
      line_values.append(item['view_count'])


#Je n'ai plus qu'a render mon front et mon formulaire
    return render_template('index.html', title=title, max=max(line_values) + 10, labels=line_labels,values=line_values, img_url=img_url,
        user_description=user_description, user_viewcount=user_viewcount)
  except:
    return render_template("display.html", form=form)

    


if __name__ == '__main__':
   app.run()