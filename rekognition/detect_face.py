import boto3

FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")

def detect_faces(filename, attributes=['ALL'], region="eu-west-1"):
	rekognition = boto3.client("rekognition", region)
        image = open(filename,'rb')
	response = rekognition.detect_faces(
	    Image={
		   'Bytes': image.read()
		},
	    Attributes=attributes,
	)
        image.close()
	return response['FaceDetails']
 
filename = "face1.jpg"
for face in detect_faces(filename):
	print "Face ({Confidence}%)".format(**face)
	# emotions
	for emotion in face['Emotions']:
		print "  {Type} : {Confidence}%".format(**emotion)
	# quality
	for quality, value in face['Quality'].iteritems():
		print "  {quality} : {value}".format(quality=quality, value=value)
	# facial features
	for feature, data in face.iteritems():
		if feature not in FEATURES_BLACKLIST:
			print "  {feature}({data[Value]}) : {data[Confidence]}%".format(feature=feature, data=data)
