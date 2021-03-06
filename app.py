from flask import Flask, render_template

from controllers.gym_bookings_controller import gym_bookings_blueprint
from controllers.gym_members_controller import gym_members_blueprint
from controllers.gym_classes_controller import gym_classes_blueprint
from controllers.gym_categories_controller import gym_categories_blueprint

app = Flask(__name__)

import repositories.gym_booking_repository as gym_booking_repository

app.register_blueprint(gym_bookings_blueprint)
app.register_blueprint(gym_members_blueprint)
app.register_blueprint(gym_classes_blueprint)
app.register_blueprint(gym_categories_blueprint)

@app.route("/")
def home():
    gym_bookings = gym_booking_repository.popular()
    return render_template('index.html', gym_bookings = gym_bookings)


if __name__ == '__main__':
    app.run(debug=True)
