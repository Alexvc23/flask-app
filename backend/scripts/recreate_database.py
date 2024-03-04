from App import create_app, db  # Import your Flask app and database instance

app = create_app()  # Create an instance of your app with the appropriate config
def recreate_database():
    with app.app_context():  # Activate the app context
        db.drop_all()  # Drop all tables
        db.create_all()  # Recreate all tables
