import csv

from decouple import config
from openai import OpenAI
from rest_framework.response import Response
from rest_framework.views import APIView

client = OpenAI(api_key=config("OPENAI_KEY"))


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
    response = client.completions.create(model="text-davinci-003", prompt=message, max_tokens=100)
    # format the response
    formatted_response = response.choices[0].text.strip()
    return formatted_response
