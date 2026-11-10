import base64
"""
encoded_string = ''
decoded_string = base64.b64decode(encoded_string)
print(decoded_string)
"""


data = b'{"type":"null","html":"<script>alert(\'hi im Joker @221298\')</script>"}\n'

encoded_data = base64.b64encode(data)

print(encoded_data)

