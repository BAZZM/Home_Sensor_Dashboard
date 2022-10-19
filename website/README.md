# Sensors Dashboard 
A pythonic implementation of real-time dashboard for the data streaming from sensors using flask

A backup repository of gitlab one


## UPDATES

**11th May**
 Sethu-01:27am
  Added graphs for each atmospheric factor in JSONs. Left attributes which are 'null' all the time. Added max,min,avg temperatures for all of the graph pages.
 ## TASKS pending
 Database up and running, front end elements, confimration of login functionality, when DB works we need to put properties class so we know what data to extract for certain user.
 **NOTE** Do not use bootstrap please. we dont have time to redo entire front end for the sake of bootstrap at this point. use the oof.html template to extend things.
 
 **7thMay**
## GRAPHS

to understand how graphs are created simply refer **graph.html** and check code route for /graph. The extraction of details can be made into a function so we dont have to repeat ourselves but for now (7may) we are testing the STABLE-ITLY of the code by experimenting

ALL in ALL, we using ApexChartsJS and they have got wonderfull tutorialas with code for every possible graph refer to docs. CAN BE IMPORTED BY CDN ALIAS Content Delivery Network AKA "the web pip"

## FRONT END

So I made a html file linked to google icons lib, w3 schools template. This is basic structure of the front end.whoever is working on front end can either decides to make a base.html and then extend this html to other htmls or jsut copy paste this code for every html adn remove unwanted things(probably body elements excluding <nav> tag. so navigation bar would still be there. IF we can make variables of info like number of flags,  we can show directly using flask variables and maybe even make use of database. 
  
 So if you are working on frontend make sure u put the graph scripts in divs of ur own creation or some empty containers i left in the html and then CSS it to fit the screen according to our needs.
 
 
 ## TASKS pending/needs to be confirmed :
 Database up and running, front end elements placement, a way to make graphs realtime,confimation on login functionality, 
 
## File explorer

**Sensor_data** contains **SAMPLE** data from Alia, the client. We are yet to recieve the full data.

**forms.py** - validates the form like if someone enters someone's email, it rejects cauz u cant have 2 diff ppl with same email

**routes.py** is a file which has routes for all of our webpages any page requiring post or get functionality can be given the permission here. Also u can wrtie logic like if      user_is_validated && entered_correct_password take him to main page


 
 
 



