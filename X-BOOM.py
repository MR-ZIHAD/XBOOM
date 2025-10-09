import marshal
import base64
import binascii

# Update this with the correct path to your hex-encoded file
encoded_file_path = 'sexy.py'

# Read the hex encoded content from the file
with open(encoded_file_path, 'r') as file:
    hex_encoded = file.read()

# Step 1: Decode the hex to get the marshaled data
marshal_encoded = binascii.unhexlify(hex_encoded)

# Step 2: Unmarshal the data to get the Base64 string
base64_encoded = marshal.loads(marshal_encoded).decode('utf-8')

# Step 3: Decode the Base64 to get the original Python script content
original_content = base64.b64decode(base64_encoded).decode('utf-8')

# Step 4: Execute the original Python content
exec(original_content)
