# Importamos la librería openai para interactuar con la API de OpenAI
import openai
# Importamos la librería json para trabajar con datos en formato JSON
import json
# Importamos la librería dotenv para cargar las variables de entorno
from dotenv import load_dotenv
import os

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# Obtenemos la clave API desde las variables de entorno
api_key = os.getenv('OPENAI_API_KEY')

# Creamos un cliente de OpenAI utilizando una clave API
client = openai.OpenAI(api_key = api_key)

# Creamos un archivo en OpenAI para el fine-tuning utilizando un archivo JSONL
responseFileCreate = client.files.create(
  file=open("additional_examples.jsonl", "rb"),
  purpose="fine-tune"
)
# Imprimimos la respuesta de la creación del archivo
print(f"responseFileCreate: {json.dumps(responseFileCreate.to_dict(), indent=2)}")

# Creamos un trabajo de fine-tuning utilizando el archivo creado anteriormente y un modelo específico
responseJobCreate = client.fine_tuning.jobs.create(
  training_file = responseFileCreate.id,
  model = "gpt-3.5-turbo"
)
# Imprimimos la respuesta de la creación del trabajo de fine-tuning
print(f"responseJobCreate: {json.dumps(responseJobCreate.to_dict(), indent=2)}")

# Listamos los últimos 10 trabajos de fine-tuning
responseFineTuningJobs = client.fine_tuning.jobs.list(limit=10)
# Imprimimos la lista de trabajos de fine-tuning
print(f"responseFineTuningJobs: {json.dumps(responseFineTuningJobs.to_dict(), indent=2)}")

# Creamos una solicitud de completado de chat utilizando el modelo fine-tuned
responseChatCompletion = client.chat.completions.create(
  model=responseFineTuningJobs.data[0].fine_tuned_model,
  messages=[
    {"role": "system", "content": "You are a teaching assistant for Machine Learning. You should help to user to answer on his question."},
    {"role": "user", "content": "What is a loss function?"}
  ]
)
# Imprimimos la respuesta de la solicitud de completado de chat en formato JSON
print(f"responseChatCompletion: {json.dumps(responseChatCompletion.to_dict(), indent=2)}")