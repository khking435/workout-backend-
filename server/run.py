# run.py 
# we will be running the app from here

from server.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
