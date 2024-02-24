import base64

def image_to_url(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        url = f"data:image/png;base64,{encoded_string}"
        return url