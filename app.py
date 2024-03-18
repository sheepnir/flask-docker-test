from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the root route ("/")
@app.route('/')
def hello():
    # Return the greeting message
    return 'Hello from Flask and Docker'

# Define the "/about-us" route
@app.route('/about-us')
def about_us():
    # Return the about-us message
    return 'This is a test app'

# Check if the script is running as the main program
if __name__ == '__main__':
    # Run the Flask application
    # Set the host to '0.0.0.0' to make the app accessible from any IP address
    # Set the port to 5000, which is the default port for Flask
    app.run(host='0.0.0.0', port=5000)