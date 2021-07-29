from click import command, echo, group
from click.decorators import option

from extensions import db, security
from app import MainApp
from endpoints.users.models import User
from endpoints.roles.models import Role

app = MainApp(environment="development")
app.setup()

@group()
def cli():
    pass

@command(name="run")
def run():
    app.run(port=8004, debug=True)

@command(name="create_superuser")
@option
def create_superuser():
    echo("Creating superuser...")

@command(name="migrate")
def migrate():
    echo("Initializing the database")

    with app.app_context():
        db.create_all()

    echo("Completed database creation")

@command(name="drop_tables")
def drop_tables():
    echo("Dropping the database...")

    with app.app_context():
        db.drop_all()

    echo("Completed dropping tables")

@command(name="make_migrations")
def make_migrations():
    echo('Committing migrations...')

    with app.app_context():
        admin = Role(name='admin')
        manager = Role(name='manager')
        superuser = Role(name='superuser')
        moderator = Role(name='moderator')

        one = User(username='One', password=security.hash_password('Theone'))
        two = User(username='Two', password=security.hash_password('Thetwo'))
        three = User(username='Three', password=security.hash_password('TheThree'))
        four = User(username='Four', password=security.hash_password('TheFour'))
        five = User(username='Five', password=security.hash_password('TheFive'))

        db.session.add_all([admin, manager, superuser, moderator, one, two, three, four, five])
        db.session.commit()


cli.add_command(run)
cli.add_command(migrate)
cli.add_command(drop_tables)
cli.add_command(make_migrations)


if __name__ == "__main__":
    cli()