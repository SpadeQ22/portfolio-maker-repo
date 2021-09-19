from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint


# Configure API key authorization: Apikey

def convert_to_pdf(input_file):
    configuration = cloudmersive_convert_api_client.Configuration()
    print(configuration.api_key)
    configuration.api_key['Apikey'] = 'YOUR_API_KEY'

    # create an instance of the API class
    api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(
        cloudmersive_convert_api_client.ApiClient(configuration))
    # input_file = '/path/to/file'  # file | Input file to perform the operation on.

    try:
        # Convert Word DOCX Document to PDF
        api_response = api_instance.convert_document_docx_to_pdf(input_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConvertDocumentApi->convert_document_docx_to_pdf: %s\n" % e)


convert_to_pdf('Autofill/AutofillResults/My Midterm.docx')
