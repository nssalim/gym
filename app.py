from flask import Flask, render_template

from controllers.gym_booking_controller import gym_booking_blueprint
from controllers.gym_member_controller import gym_member_blueprint
from controllers.gym_class_controller import gym_classe_blueprint

app = Flask(__name__)

app.register_blueprint(gym_booking_blueprint)
app.register_blueprint(gym_member_blueprint)
app.register_blueprint(gym_class_blueprint)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
