import weaviate
import json

client = weaviate.Client(
    embedded_options=weaviate.embedded.EmbeddedOptions(),
    additional_headers={
        'X-OpenAI-Api-Key': 'YOUR-OPENAI-API-KEY'  # Replace w/ your OPENAI API key
    })

client.schema.create_class({
    'class': 'Wine',
    'vectorizer': 'text2vec-openai',
})

client.data_object.create({
    'name': 'Chardonnay',
    'review': 'Goes well with fish!',
}, 'Wine')

response = (
    client.query
    .get('Wine', ['name', 'review'])
    .with_near_text({
        'concepts': ['great for seafood']
    })
    .do()
)

assert response['data']['Get']['Wine'][0]['review'] == 'Goes well with fish!'