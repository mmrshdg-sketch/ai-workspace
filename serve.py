from llama_cpp import Llama
import gradio as gr

# Load the GGUF model (ensure the path is available in your workspace)
MODEL_PATH = "model/gemma-1b.gguf"
llm = Llama(model_path=MODEL_PATH)

# Define a simple function to handle user prompts
def chat_with_model(prompt):
    response = llm(prompt)
    return response['content']

# Gradio interface to expose the chatbot
interface = gr.Interface(fn=chat_with_model, inputs="text", outputs="text")
interface.launch(server_name="0.0.0.0", server_port=7860)
