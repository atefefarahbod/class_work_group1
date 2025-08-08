# class UserBatchProcessor:
#     def __init__(self , users):
#         self.__users = users
#         self.__batch_size = 3

#     @property
#     def batch_size(self):
#         return self.__batch_size
    
#     @batch_size.setter
#     def batch_size(self , value):
#         if not isinstance(value , int) or value < 0:
#             raise ValueError ("batch_size in not valid")
#         self.__batch_size = value

#     def get_batches(self):
#         for i in range(0 , len(self.__users) , self.__batch_size):
#             yield self.__users[i: i + self.__batch_size]

#     def total_batches(self):
#         return (len(self.__users) + self.__batch_size) // self.__batch_size
    
#     def has_remaining(self):
#         return len(self.__users) % self.__batch_size != 0
    
# users = ["a" , "b" , "c" , "d" , "e" , "f" , "g"]
# a = UserBatchProcessor(users)
# print(a.batch_size)
# print(a.total_batches)
# print(a.has_remaining)
# for batch in a.get_batches():
#     print(batch)
# ---------
class UserBatchProcessor:
    def __init__(self , users):
        self._users = list(users)
        self._batch_size = 3

    @property
    def batch_size(self):
        return self._batch_size
    
    @batch_size.setter
    def batch_size(self , value):
        if not isinstance(value , int) or value < 0:
            raise ValueError ("batch_size in not valid")
        self._batch_size = value

    @property
    def users(self):
        return self._users
    
    @users.setter
    def users(self , user):
        self._users.append(user)

        
    def get_batches(self):
        for i in range(0 , len(self._users) , self._batch_size):
            yield self._users[i: i + self._batch_size]

    def total_batches(self):
        return (len(self._users) + self._batch_size) // self._batch_size
    
    def has_remaining(self):
        return len(self._users) % self._batch_size != 0
    
users = ["a" , "b" , "c" , "d" , "e" , "f" , "g"]
a = UserBatchProcessor(users)
print(a.batch_size)
print(a.total_batches)
print(a.has_remaining)
for batch in a.get_batches():
    print(batch)
    #    ---