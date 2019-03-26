class A:
    __identity_id = 343333333333333
    COUNTRY = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_identity_id(cls):
        return A.__identity_id

    def get_name(self):
        return self.name


chen = A('Chen', 22)
print(A.get_identity_id())

if hasattr(chen, '__identity_id'):
    ret = getattr(chen, '__identity_id')
    print(ret)

print(getattr(chen, 'get_name')())
print(getattr(A, 'COUNTRY'))
print(getattr(A, 'get_identity_id')())