# 🚀 Fine-Tuning de Modelos GPT de OpenAI

Este proyecto es un ejemplo sencillo de cómo realizar un fine-tuning a modelos GPT de OpenAI utilizando la API de OpenAI. Aquí te mostramos los pasos básicos para crear un archivo de entrenamiento, iniciar un trabajo de fine-tuning y realizar una solicitud de completado de chat con el modelo fine-tuned.

## 📋 Requisitos

- Python 3.6 o superior
- Clave API de OpenAI
- Archivo JSONL con ejemplos adicionales para el entrenamiento

## 📂 Archivos

- `index.py`: Script principal que realiza el fine-tuning y las solicitudes a la API de OpenAI.
- `additional_examples.jsonl`: Archivo JSONL con ejemplos adicionales para el entrenamiento.

## 🚀 Pasos para Ejecutar el Proyecto

1. **Instalar dependencias**:
   ```bash
   pip install openai python-dotenv
   ```

2. **Configurar la clave API**:
   Crea un archivo `.env` en la raíz del proyecto y agrega tu clave API:
   ```
   OPENAI_API_KEY=tu_clave_api
   ```

3. **Asegurarse de que el archivo `.env` no se suba a Git**:
   Agrega `.env` a tu archivo `.gitignore`:
   ```
   # .gitignore
   .env
   ```

4. **Ejecutar el script**:
   ```bash
   python index.py
   ```

## 📜 Descripción del Código

- **Importación de librerías**:
  ```python
  import openai
  import json
  from dotenv import load_dotenv
  import os
  ```

- **Cargar variables de entorno y crear el cliente de OpenAI**:
  ```python
  load_dotenv()
  api_key = os.getenv('OPENAI_API_KEY')
  client = openai.OpenAI(api_key=api_key)
  ```

- **Creación de un archivo para fine-tuning**:
  ```python
  responseFileCreate = client.files.create(
    file=open("additional_examples.jsonl", "rb"),
    purpose="fine-tune"
  )
  print(f"responseFileCreate: {responseFileCreate}")
  ```

- **Creación de un trabajo de fine-tuning**:
  ```python
  responseJobCreate = client.fine_tuning.jobs.create(
    training_file=responseFileCreate.id,
    model="gpt-3.5-turbo"
  )
  print(f"responseJobCreate: {responseJobCreate}")
  ```

- **Listado de trabajos de fine-tuning**:
  ```python
  responseFineTuningJobs = client.fine_tuning.jobs.list(limit=10)
  print(f"responseFineTuningJobs: {responseFineTuningJobs}")
  for FineTuningJob in responseFineTuningJobs.data:
    print(f"FineTuningJob: {FineTuningJob}")
  ```

- **Solicitud de completado de chat**:
  ```python
  responseChatCompletion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-0125:personal::A4xgRpak",
    messages=[
      {"role": "system", "content": "You are a teaching assistant for Machine Learning. You should help to user to answer on his question."},
      {"role": "user", "content": "What is a loss function?"}
    ]
  )
  print(f"responseChatCompletion: {json.dumps(responseChatCompletion.to_dict(), indent=2)}")
  ```

## 📞 Contacto

Para cualquier duda o sugerencia, no dudes en contactarme a través de [nelsonromero219@gmail.com](mailto:nelsonromero219@gmail.com).

¡Gracias por revisar este proyecto! 🎉