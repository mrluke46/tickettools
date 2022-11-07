from website import create_app
#from website import create_database

app = create_app()
#database = create_database()

if __name__ == '__main__' :
    app.run(debug=True, port= 8000)