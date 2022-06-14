import gradio as gr

with gr.Blocks() as demo:
  with gr.Row():
    num = gr.Number(0, show_label=False).style(container=False)
    btn = gr.Button("Count")

    btn.click(lambda x:x+1, num, num)

if __name__ == "__main__":
  demo.launch()
