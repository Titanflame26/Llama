from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/bharadwaj_26/LLama2-tutorial-description/workflows/workflow-a52c0e"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="b6668c0a07d940479aefb10baae1dfdb"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)