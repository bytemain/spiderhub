from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run(passthrough_errors=True, load_dotenv=True)
