from slack_bolt import App
from dotenv import load_dotenv
import os

load_dotenv()

app = App(token=os.getenv("SLACK_BOT_KEY"), signing_secret=os.getenv("SLACK_SIGNING_SECRET"))

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
