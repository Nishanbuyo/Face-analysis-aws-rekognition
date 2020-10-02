import boto3

# aws_access_key_id="ASIA2GOY3NVRH5EZ7V7H"
# aws_secret_access_key="7q8ORa1PRoainMqNpl8G7RyeWkwKEKMA6EOmJHI6"
# aws_session_token="FwoGZXIvYXdzEHIaDGg5j/mO6YyG691VgCLWAadCep1aAVVJsyzUE0zUedlUXncFHPWHox3yRqA+ndz4sySjmI/H4FD+ukxfhxMT9tKFb+UbqLu/cW/S5XnT9yOZ73yZmFLsm9tommoU5LgLrM1QR8aGrSbek1gI8ZZZpNqB7yJAh4NLjmxvcrhlpFdu4JgIZ9STEmy+NLOh/P18C7YcD+ipQgLsalx7FwWNztumv7Rt+UVUSYCvcpbvW9py/p2Y7et8piMDHfN3xuJ6+OudQsFb9Rl8kuWA4TBncx1w05cgp+9cOnWRio8iA84EWRsC7asovNTb+wUyLepXzfU6U1QOpGMNegdN3TZpUka/dIpXx/24DRkqVIjeX0TqqVNXk3B3anz/aw=="

def detect_face(photo_path):
    photo = photo_path
    client = boto3.client("rekognition")
    # client = boto3.client("rekognition", aws_access_key_id=aws_access_key_id,
    #                       aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token
    #                       )
    with open(photo, 'rb') as image:
        response = client.detect_faces(
            Image={'Bytes': image.read()}, Attributes=['ALL', 'DEFAULT'])

    with open(photo, 'rb') as image:
        celebrity = client.recognize_celebrities(
            Image={'Bytes': image.read()})

    print('Detected faces for ' + photo)

    res = list(response['FaceDetails'])
    celebrity=list(celebrity['CelebrityFaces'])

    for face in response['FaceDetails']:

        print('Gender: ' + face['Gender']['Value'])

        print(
            f"The age of person is between {face['AgeRange']['Low']} to {face['AgeRange']['High']}")

        print(
            f"The Emotional state of person is {face['Emotions'][0]['Type']} with {face['Emotions'][0]['Confidence']}")

        print(f"Eyeglasses: {face['Eyeglasses']['Value']}")

        print(f"Sunglasses: {face['Sunglasses']['Value']}")
    
    return celebrity, res