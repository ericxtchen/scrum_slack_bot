from .main import app

def start_standup(channel_id):
    try:
        app.client.chat_postMessage(
            channel=channel_id,
            text="Time to start the daily standup!"
        )
        return {"statusCode": 200, "body": "Message sent successfully."}
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to send message: {e}"}

