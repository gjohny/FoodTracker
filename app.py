from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #automatically rerun the web server when a change is made (turn off in production)