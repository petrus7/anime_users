from flask import Flask

from src.anime_list_service import create_app



app = create_app('DevelopmentConfig')

@app.route('/')
def test():
    return 'ala nie ma kota'


# if __name__ == '__main__':
#     app.run()
