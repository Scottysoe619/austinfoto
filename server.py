import http.server
import socketserver
import os
from PIL import Image

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

    

# Open the uploaded image
image_path = 'path_to_uploaded_image.jpg'
image = Image.open(image_path)

# Display the image
image.show()



# Save the uploaded image
image_path = 'path_to_uploaded_image.jpg'
with open(image_path, 'wb') as f:
    f.write(image_data)