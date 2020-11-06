import boto3

client = boto3.client('rekognition')

with open('test_image.jpg', 'rb') as image:
	response = client.detect_faces(
		Image={
			'Bytes': image.read()
		},
		Attributes=["ALL"]
	)

print(f"The total number of faces detected are {len(response['FaceDetails'])}.")

count = 1
for face in response['FaceDetails']:
	print(f"\nThe analysis of face {count} is:\n")
	print(f"Position[Left, Top, Width, Height]: [{face['BoundingBox']['Left']:.2f}, {face['BoundingBox']['Top']:.2f}, {face['BoundingBox']['Width']:.2f}, {face['BoundingBox']['Height']:.2f}]")
	print(f"Age: {face['AgeRange']['Low']}-{face['AgeRange']['High']} yrs.")
	print(f"Gender: {face['Gender']['Value']}")
	if face['Gender']['Value']=='Male':
		print(f"Beard: {face['Beard']['Value']}")
		print(f"Mustache: {face['Mustache']['Value']}")

	else:
		print(f"Smile: {face['Smile']['Value']}")

	emotions = {x['Type']:x['Confidence'] for x in face['Emotions']}
	highest_confidence_emotion = max(emotions.items(), key=lambda k: k[1])
	print(f"Strongest Emotion: {highest_confidence_emotion[0]} with confidence {highest_confidence_emotion[1]:.2f}")
	print(f"EyeGlasses: {face['Eyeglasses']['Value']}")
	count+=1

