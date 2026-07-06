import strawberry

from app.graphql.employees import EmployeeQuery, EmployeeMutation
from app.graphql.products import ProductQuery, ProductMutation
from app.graphql.sales import SaleQuery
from app.graphql.todos import TodoQuery, TodoMutation
from app.graphql.users import UserQuery, UserMutation
from app.graphql.auth import AuthQuery, AuthMutation


@strawberry.type
class Query(EmployeeQuery, ProductQuery, SaleQuery, TodoQuery, UserQuery, AuthQuery):
    pass


@strawberry.type
class Mutation(EmployeeMutation, ProductMutation, TodoMutation, UserMutation, AuthMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)