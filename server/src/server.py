# Pyramid Imports
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.response import Response

# Import MySQL Connector Driver
import mysql.connector as mysql

# Load the DB credentials
import os
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

# Valid commands from web UI controller
valid_commands = ['takeoff','land','up','down','left','right','back','forward','cw','ccw']


""" Helper Functions """

# A Function to Queue Commands to the MySQL Database
def send_command(command):
  # Insert code to insert commands to database here:
  db = mysql.connect(host = db_host, database = db_name, user = db_user, passwd = db_pass)
  cursor = db.cursor()
  query = "insert into Commands (message, completed) values (%s, %s)"
  values = [command, 0]
  cursor.execute(query, values)
  db.commit()

  print('-----INSERT-----')
  print(cursor.rowcount, "record inserted. ", command)

  print('-----Queued Commands-----')
  cursor.execute("select * from Commands where completed=0;")
  response = cursor.fetchall()
  print(response)
  pass


""" Routes """

# TEST ROUTE TEST ROUTE TEST ROUTE TEST ROUTE TEST ROUTE
def test(req):
  send_command("test")
  return Response("Command sent to db (server): 'test'")

# VIEW: Web Controller Route
def web_ui_route(req):
  return render_to_response('templates/web_ui.html', [], request=req)

# REST: Drone Command Route
def drone_command_route(req):
  command = req.matchdict.get('command')
  arg = req.matchdict.get('arg')

  if command not in valid_commands:
    return {'Response (server):':'Invalid command received'}

  # Combine argument with command
  command = command if not arg else command + " " + arg[0]

  print('Sending command: ', command)
  send_command(command)
  return {'Response (server):':'Command sent!'}



#############################################################
###### Copy over what you implemented in lab4 over!!! #######
#############################################################



#############################################################
### Define and build your NEW route functionalities here: ###
#############################################################
def get_telemetry_route(req):
  db = mysql.connect(host = db_host, database = db_name, user = db_user, passwd = db_pass)
  cursor = db.cursor()
  cursor.execute("select * from Telemetry ORDER BY id DESC limit 1;")
  response = cursor.fetchone()

  

  # Check if there was telemetry
  if response is not None:
    returnResponse = ('{ "pitch":'+str(response[1])+', "roll":'+str(response[2])
    +', "yaw":'+str(response[3])+', "vgx":'+str(response[4])
    +', "vgy":'+str(response[5])+', "vgz":'+str(response[6])
    +', "templ":'+str(response[7])+', "temph":'+str(response[8])
    +', "tof":'+str(response[9])+', "h":'+str(response[10])
    +', "bat":'+str(response[11])+', "baro":'+str(response[12])
    +', "time":'+str(response[13])+', "agx":'+str(response[14])
    +', "agy":'+str(response[15])+', "agz":'+str(response[16])+'}'
    )

  #  print(returnResponse)
    return Response(returnResponse)
  else:
    print("TELEMETRY TABLE EMPTY")
    return Response("EMPTY")

def flight_plan_route(commands):
  

  splitList = str(commands.body)
  splitList = splitList[2:-1]
  splitList = splitList.split(",")

  print(splitList)

  for command in splitList:
    send_command(command)
  return Response("Success")




""" Main Entrypoint """

if __name__ == '__main__':
  with Configurator() as config:
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    # TEST ROUTE TEST ROUTE TEST ROUTE TEST ROUTE TEST ROUTE
    config.add_route('test', '/test')
    config.add_view(test, route_name='test')

    config.add_route('web_ui', '/')
    config.add_view(web_ui_route, route_name='web_ui')

    config.add_route('drone_command', '/drone_command/{command}*arg')
    config.add_view(drone_command_route, route_name='drone_command', renderer='json')

    
    #########################################################
    ############## State your NEW routes here: ##############
    #########################################################
    
    config.add_route('get_telemetry', '/get_telemetry')
    config.add_view(get_telemetry_route, route_name='get_telemetry')

    config.add_route('flight_plan', '/flight_plan')
    config.add_view(flight_plan_route, route_name='flight_plan')

    
    config.add_static_view(name='/', path='./public', cache_max_age=3600)

    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 1234, app)
  print('Web server started on: http://0.0.0.0:8000 OR http://localhost:8000')
  server.serve_forever()
