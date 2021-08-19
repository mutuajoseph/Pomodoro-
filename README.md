## Pomodoro 

1. Create a virtual environment: python3 -m venv <'env_name'>

2. Install the required packages: pip install -r requirements.txt

3. Create a .env file and add the following data instances

```
FLASK_APP=<'app name'>
FLASK_ENV=<'environment'>
DATABASE=<'database_name'>
POSTGRES_USER=<'postgres_user'>
POSTGRES_PASSWORD=<'postgres_password'>
SQLALCHEMY_DATABASE_URI=<'database_urli'>


```
4. Run migrations to update the changes to db: flask db upgrade
5. Configure a start.sh file to execute your app
6. Execute you start.sh file from terminal to lauch app