from app_factory import create_app

app = create_app()
app.run(port=8000, debug=True)
