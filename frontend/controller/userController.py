from frontend.models.userModel import Users

class userController:

    def addUser(self, userData):
        """
        add a new user to the database
        
        userData = {
            "userName": "ankush"
            "email": "ankush302@gmail.com"
            "password": "supersecret"
        }

        """

        query = Users(
            userName = userData['userName'],
            email = userData['email'],
            password = userData['password']
        ).save()

        return query
