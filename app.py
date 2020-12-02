from flask import Flask, render_template

from controllers.gym_bookings_controller import gym_bookings_blueprint
from controllers.gym_members_controller import gym_members_blueprint
from controllers.gym_classes_controller import gym_classes_blueprint

app = Flask(__name__)

app.register_blueprint(gym_bookings_blueprint)
app.register_blueprint(gym_members_blueprint)
app.register_blueprint(gym_classes_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
