from flask import Flask
from flask import request
import tmdbsimple as tmdb

app = Flask(__name__)
app.debug = True
tmdb.API_KEY = '9b0b3c1fb0687294e34482f133e20eec'
    
@app.route('/')
def search_form():
    html = '<html style="background: url(http://mediad.publicbroadcasting.net/p/kuow/files/styles/medium/public/201308/0828-m4tik.jpg) no-repeat;background-size: 100%;"><body>'
    html += '<form method="POST" action="results">\n'
    html += '<div style="background-color: white;border-radius: 50px 50px;width: 500;position: fixed;left: 33%;"><br>'
    html += '<h1 style="text-align:center;color: blue;">Enter Movie Name</h1><br>\n'
    html += '</div>'
    html += '<input type="textbox" style="width: 300px;position: relative;top: 200px;left: 40%;text-align: center;padding: 5px;background-color: #7ceffd;border-style: solid;border-radius: 50px 50px;border-color: black;" name="find_movie" placeholder="Enter a movie name"><br>\n'
    html += '<input style="position:relative; left: 47%; top: 200px;border-radius: 50px 50px; border-style: none; color: red" type="submit" value="Search Movie">\n'
    html += '</form>\n'
    html += '</body>\n</html>\n'
    return html

@app.route('/results', methods=['POST'])
def results():
    find_movie = request.form['find_movie']

    #Looks thru database and prints the movies found
    search = tmdb.Search()
    response = search.movie(query=find_movie)
    
    html = '<html style="background: url(http://mediad.publicbroadcasting.net/p/kuow/files/styles/medium/public/201308/0828-m4tik.jpg) no-repeat;background-size: 100%;">\n<body>\n'
    html += '<table style="background-color: powderblue;margin: 4em auto;border-collapse: collapse;border: 2px solid black;">\n<tr style="background-color: #b51d1d;font-size: 30px;border: 2px solid black;">\n<th style="border: 2px solid black;padding: 12px;">Movie Name</th>\n<th style="border: 2px solid black;padding: 12px;">Movie ID</th>\n<th style="border: 2px solid black;padding: 12px;">Release Date</th>\n<th style="border: 2px solid black;padding: 12px;">Popularity</th>\n</tr>'
    for movie in search.results:
        html += '<tr style="border: 2px solid black;">\n<td style="border: 2px solid black;">' + movie["title"] + '</td>\n<td style="border: 2px solid black;">' + str(movie["id"]) + '</td>\n<td style="border: 2px solid black;">' + str(movie["release_date"]) + '</td>\n<td style="border: 2px solid black;">' + str(movie["popularity"]) + '</td>\n</tr>\n'
    html += '</table>\n'
    html += '<a href="/"><button style="Border-radius: 5px 5px; Border: dotted; position:fixed;left: 50%;">Back</button></a>'
    html += '</body>\n</html>\n'
    return html

if __name__ == "__main__":
    app.run()
