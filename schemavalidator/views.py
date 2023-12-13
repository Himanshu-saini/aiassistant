import csv

import openai
from decouple import config
from rest_framework.response import Response
from rest_framework.views import APIView


class ValidateSchemaView(APIView):
    def post(self, request):
        schema_file = request.FILES.getlist("file")[0]

        decoded_file = schema_file.read().decode("utf-8").splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            for column, value in row.items():
                print(column, value)
        message = request_ai("hi what is your name")
        resp = {"data": message}
        return Response(data=resp, status=200)


def request_ai(message):
    openai.api_key = config("OPENAI_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt=message,
        max_tokens=100,  # Adjust based on your needs
    )
    # format the response
    formatted_response = response.choices[0].text.strip()
    return formatted_response
