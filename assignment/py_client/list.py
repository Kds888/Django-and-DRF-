import requests

get_model_response_post = requests.get("http://localhost:8000/api/students/") 
print(get_model_response_post.json())
