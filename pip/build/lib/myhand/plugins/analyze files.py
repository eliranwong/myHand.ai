"""
My Hand Bot Plugin - analyze files

analyze files with "AutoGen Retriever"
"""


from myhand import config
import os
from myhand.autogen_retriever import AutoGenRetriever

def analyze_files(function_args):
    query = function_args.get("query") # required
    files = function_args.get("files") # required
    if os.path.exists(files):
        config.stopSpinning()
        AutoGenRetriever().getResponse(files, query)
        return ""

    return "[INVALID]"

functionSignature = {
    "name": "analyze_files",
    "description": "retrieve information from files",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Questions that users ask about the given files",
            },
            "files": {
                "type": "string",
                "description": """Return a directory or non-image file path. Return an empty string '' if it is not given.""",
            },
        },
        "required": ["query", "files"],
    },
}

config.chatGPTApiFunctionSignatures.append(functionSignature)
config.chatGPTApiAvailableFunctions["analyze_files"] = analyze_files