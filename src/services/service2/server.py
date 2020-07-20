from app import app
from graphene_file_upload.flask import FileUploadGraphQLView
from mongoengine import connect
from schema import schema

# we need to connect to both databases
connect('service1',
        host=app.config['MONGO_HOST'],
        alias='user-db',
        username=app.config['MONGO_USER'],
        password=app.config['MONGO_PWD'],
        authentication_source="admin")

connect('service2',
        host=app.config['MONGO_HOST'],
        alias='review-db',
        username=app.config['MONGO_USER'],
        password=app.config['MONGO_PWD'],
        authentication_source="admin")

app.add_url_rule('/graphql', view_func=FileUploadGraphQLView.as_view('graphql', schema=schema, graphiql=app.debug))

if __name__ == '__main__':
    app.run(port=5002)