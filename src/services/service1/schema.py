import graphene
from graphene_mongo import MongoengineObjectType

from graphene_federation import build_schema, key
from models.UserModel import UserModel


# The primary key 
@key('id')
class User(MongoengineObjectType):

    # we resolve a db reference by the id
    def __resolve_reference(self, info, **kwargs):
        # common mongoengine query
        return UserModel.objects.get(id=self.id)

    # Use Model as Type (common graphene_mongoengine)
    class Meta:
        model = UserModel


# define a query
class Query(graphene.ObjectType):
    users = graphene.Field(User)

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()


# define a mutation
class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()
        age = graphene.Int()

    def mutate(self, info, username, age):
        user = UserModel(username=username, age=age)
        user.save()
        return CreateUser(user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# build schema USE THE FEDERATION PACKAGE
schema = build_schema(Query, types=[User], mutation=Mutation)