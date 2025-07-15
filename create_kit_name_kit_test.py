import data
import sender_stand_request

def get_kit_body(kit_name):
   current_body = data.kit_body.copy()
   current_body["name"] = kit_name
   return current_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400


# Prueba n°1
def test_1():
    new_kit_body= get_kit_body ("a")
    positive_assert(new_kit_body)

# Prueba n°2
def test_2():
    new_kit_body= get_kit_body ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

# Prueba n°3
def test_3():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

# Prueba n°4
def test_4():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(new_kit_body)

# Prueba n°5
def test_5():
    new_kit_body = get_kit_body("#%&/")
    positive_assert(new_kit_body)

# Prueba n°6
def test_6():
    new_kit_body = get_kit_body(" A Aaa ")
    positive_assert(new_kit_body)

# Prueba n°7
def test_7():
    new_kit_body = get_kit_body("123")
    positive_assert(new_kit_body)

#Prueba n°8
def test_8():
    new_kit_body = data.kit_body.copy()
    new_kit_body.pop("name")
    negative_assert_code_400(new_kit_body)


# Prueba n°9
def test_9():
    new_kit_body = get_kit_body(123)
    negative_assert_code_400(new_kit_body)
