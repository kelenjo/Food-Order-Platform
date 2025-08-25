# import pytest
#
#
# def sum(a, b):
#     return a+b
#
#
# def test_sum():
#     assert sum(5, 5) == 10
#     assert sum(5, 0) == 5
#
#
# class User:
#     real_person = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sum(self, x):
#         return self.age + x
#
#     @classmethod
#     def is_real_person(cls):
#         return cls.real_person
#
#     @classmethod
#     def get_class(cls):
#         return cls
#
#
# def test_class():
#     user = User("gio", 15)
#     assert user.sum(-2) == 13
#     assert user.is_real_person() == True
#     assert User.is_real_person() == True
#     assert User.get_class().real_person == True
#     assert user.get_class().real_person == True
#
#
# @pytest.fixture(autouse=True)
# def ini(request):
#     if request.cls is not None:  # Only for class-based tests
#         request.cls.user = User("mari", 15)
#         request.cls.p = 3.14159
#
#
# @pytest.mark.usefixtures("ini")
# class Testsmt:
#     def test_user(self):
#         assert self.user.name=="mari"
#
#     @pytest.mark.skip
#     def test_pruwi(self):
#         assert self.p*5==3.14159*0
#
#
#
#
