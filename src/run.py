from app import app
import os


if __name__ == "__main__":
    app.run(port=3000, host="0.0.0.0", debug=bool(os.getenv('DEBUG')))
