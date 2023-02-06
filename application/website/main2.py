from flask  import *
import json ,time
#creating the app 
app=Flask(__name__) 
#creating the first end point
@app.route('/',methods=['GET'])
def home_page():
    dataset={'Page':'Home','Message':'Successful laoded the home page','Timestamp':time.time}
     #changing this data into json