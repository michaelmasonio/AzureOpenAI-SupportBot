import weaviate
import json

from flask import Flask
from routes import routes

app = Flask(__name__)

app.add_url_rule('/', 'index', routes.index)
app.add_url_rule('/chat', 'chat', routes.chat, methods=['POST'])
app.add_url_rule('/clear_messages', 'clear_messages', routes.clear_messages, methods=['POST'])



# client = weaviate.Client(
#     embedded_options=weaviate.embedded.EmbeddedOptions(),
# )

# uuid = client.data_object.create({
#     'hello': 'World!'
# }, 'MyClass')

# obj = client.data_object.get_by_id(uuid, class_name='MyClass')

# print(json.dumps(obj, indent=2))

if __name__ == '__main__':
    app.run(debug=True)
