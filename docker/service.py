fake_db = []

def get_users_service():
    return {
        "status": "success",
        "data": fake_db
    }


def create_users_service(user):
    new_user = {
        "id": len(fake_db) + 1,
        "name": user.name,
        "email": user.email
    }

    fake_db.append(new_user)

    return {
        "status": "created",
        "data": new_user
    }
