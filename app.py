from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define the home route ("/")
@app.route('/')
def home():
    # Render the 'home.html' template and return it as the response
    return render_template('home.html')

# Define the about-us route ("/about-us")
@app.route('/about-us')
def about_us():
    # Render the 'about.html' template and return it as the response
    return render_template('about.html')

# Define the circle route ("/circle")
@app.route('/circle')
def circle():
    # Render the 'circle.html' template and return it as the response
    return render_template('circle.html')

# Check if the script is running as the main program
if __name__ == '__main__':
    # Run the Flask application
    # Set the host to '0.0.0.0' to make the app accessible from any IP address
    # Set the port to 5000, which is the default port for Flask
    app.run(host='0.0.0.0', port=5000)