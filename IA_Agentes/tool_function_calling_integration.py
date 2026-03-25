[CONTENIDO]
import json
from typing import Dict, Any
from qwen25.local_tool import QwenLocalTool
from qwen25.function_calling import QwenFunctionCaller

class ToolAndFunctionIntegration:
    def __init__(self):
        self.tool = QwenLocalTool()
        self.function_caller = QwenFunctionCaller()

    def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user's query by first using the local tool to understand
        what action is required and then call the corresponding function.
        
        Args:
            query (str): User's input query or command.

        Returns:
            Dict[str, Any]: Response from calling the function with the provided data.
        """
        # Step 1: Use QwenLocalTool for understanding the user intent
        tool_response = self.tool.process_query(query)
        if 'error' in tool_response:
            return {'status': 'failed', 'message': f"Error from QwenLocalTool: {tool_response['error']}"}
        
        # Step 2: Extract function and parameters information
        function_name = tool_response.get('function')
        params = tool_response.get('parameters')

        if not (isinstance(function_name, str) and isinstance(params, dict)):
            return {'status': 'failed', 'message': "Invalid response from QwenLocalTool"}

        # Step 3: Call the target function using QwenFunctionCaller
        try:
            func_response = self.function_caller.call_function(function_name, params)
            if not func_response['success']:
                raise Exception(func_response.get('error'))
            return {'status': 'success', 'response': func_response['data']}
        
        except Exception as e:
            return {'status': 'failed', 'message': f"Error calling function {function_name}: {str(e)}"}

if __name__ == '__main__':
    integration = ToolAndFunctionIntegration()
    
    # Example usage of the process_query method
    sample_query = "What's my balance?"
    response = integration.process_query(sample_query)
    
    print(json.dumps(response, indent=4))