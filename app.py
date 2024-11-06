from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

model - pipeline("summary")
def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.Texbox(placeholder="Enter text block to summarize ", lines=4)
    gr.Interface(fn=prdict, inputs=textbox, outputs="text")

demo.launch()





