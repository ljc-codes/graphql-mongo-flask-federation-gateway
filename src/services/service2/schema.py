import graphene
from graphene_mongo import MongoengineObjectType

from graphene_federation import build_schema, key, external, extend
from models.ReviewModel import ReviewModel


# use extend and the key to tell service2 that this a type from another service
@extend('id')
class User(graphene.ObjectType):
    # define key, use graphene.ID because this is the type used by graphene_mongo
    # set it to external
    id = external(graphene.ID())


# set id as key
@key('id')
class Review(MongoengineObjectType):
    # Add user as type
    user = graphene.Field(User)

    # optional: we dont need to resolve the reference
    def __resolve_reference(self, info, **kwargs):
        return ReviewModel.objects.get(id=self.id)

    # Use Model as Type (common graphene_mongoengine)
    class Meta:
        model = ReviewModel


# define a query
class Query(graphene.ObjectType):
    reviews = graphene.Field(Review)

    def resolve_reviews(self, info, **kwargs):
        return ReviewModel.objects.all().first()


# define a mutation
class CreateReview(graphene.Mutation):
    review = graphene.Field(Review)

    class Arguments:
        name = graphene.String()
        user_id = graphene.String()

    def mutate(self, info, name, user_id):
        review = ReviewModel(name=name, user=user_id)
        review.save()
        return CreateReview(review)


class Mutation(graphene.ObjectType):
    create_review = CreateReview.Field()


# build schema USE THE FEDERATION PACKAGE
schema = build_schema(Query, mutation=Mutation)