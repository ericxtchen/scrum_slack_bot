from .main import app

@app.command("standup")
def handle_response(ack, message):
    ack()