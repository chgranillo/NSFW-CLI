import requests
import json
import sys

apiKey = "**YOUR_KEY_HERE**"

# Documentation for AnalyzeAdult Endpoint
# https://www.haystack.ai/docs?python#analyzeadult
def imageContainsNudity(image):
	outputType = "json"
	customModel = "yahoonsfw"
	requestUri = "https://api.haystack.ai/api/image/analyzeadult?output={}&apikey={}".format(outputType, apiKey)
	apiResponse = requests.post(requestUri, data=image)
	response = json.loads(apiResponse.text)

	return response["containsNudity"]

image = sys.argv[1]

with open(image, "rb") as imageData:
	if imageContainsNudity(imageData):
		print(image)