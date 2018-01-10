import boto3
REGION='us-east-1'
def search_faces_by_image(filename, collection_id, threshold=80, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
        image = open(filename, "rb")
	response = rekognition.search_faces_by_image(
		Image={
		  'Bytes': image.read()
		},
		CollectionId=collection_id,
		FaceMatchThreshold=threshold,
	)
        image.close()
	return response['FaceMatches']

# Create collection

faces_files = ['face2.jpg', 'face3.jpg', 'face4.jpg', 'face1.jpg']
rek = boto3.client("rekognition", REGION )
rek.delete_collection(CollectionId='faces1collection')
collection = rek.create_collection(CollectionId='faces1collection')

for filename in faces_files:
  with open(filename, 'rb') as image:
    rek.index_faces(CollectionId='faces1collection', Image = { 'Bytes': image.read() })

for record in search_faces_by_image('face1.jpg', 'faces1collection'):
	face = record['Face']
	print "Matched Face ({}%)".format(record['Similarity'])
	print "  FaceId : {}".format(face['FaceId'])
	print "  ImageId : {}".format(face['ImageId'])

