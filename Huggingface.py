from transformers import pipeline
print("transformers pipeline are present in the evn ")

generator = pipeline("text-generation")
generator("In this couse, we will teach you  the hindi ")