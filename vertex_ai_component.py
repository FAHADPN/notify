import vertexai  
from vertexai.preview.language_models import TextGenerationModel  
import json

def notify(text: str, PROJECT_ID):
    parameters = {
        "temperature": 0.2,          
        "max_output_tokens": 256,    
        "top_p": 0.8,            
        "top_k": 40,            
    }

    vertexai.init(project=PROJECT_ID)
    model = TextGenerationModel.from_pretrained("text-bison@001")

    response = model.predict(
        f"Make a note markdown - with heading, subheadings, points, and aesthetically pleasing content for the following text : {text}",  
        **parameters
    )
    return response.text