from .main import app
from .handlers import enable_response, disable_response

def start_standup(channel_id):
    try:
        app.client.chat_postMessage(
            channel=channel_id,
            text="Time to start the daily standup! \n What did you work on yesterday?\n What will you work on today?\n Any blockers\n?"
        )
        enable_response()
        return {"statusCode": 200, "body": "Message sent successfully."}
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to send message: {e}"}

def end_standup(channel_id):
    try:
        app.client.chat_postMessage(
            channel=channel_id,
            text="Daily standup ended!"
        )
        disable_response()
        return {"statusCode": 200, "body": "Message sent successfully."}
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to send message: {e}"}
