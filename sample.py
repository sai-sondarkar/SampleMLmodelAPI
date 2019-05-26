from flask import Flask
#imported Flask in our this Python file



app = Flask(__name__)
#Created a constructor of the Flask Object



#Decorator for the Route creation
@app.route("/")
def hello_sample_function():
    #Sample function for the API to host
    return "http://bit.ly/lusmapleapi"



#If the file running directly please run the APP
if __name__ == "__main__":
    app.run(debug= True)


