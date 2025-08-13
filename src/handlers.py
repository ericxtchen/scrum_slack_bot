from .main import app
import globals

def enable_response():
    globals.STANDUP_ACTIVE = True

def disable_response():
    globals.STANDUP_ACTIVE = False

@app.command("/standup")
def handle_response(ack, body):
    if globals.STANDUP_ACTIVE == False:
        ack("Standup session is over!")
    else:
        ack()
        user_id = body["user_id"]
