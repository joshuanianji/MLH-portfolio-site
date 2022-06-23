echo "Adding a new timeline..."
NUM=$(( $RANDOM ))
CONTENT="Endpoint content test: num=$NUM"
RESPONSE=$( curl -s -X POST http://localhost:5000/api/timeline_post -d "name=Joshua&email=joshuanji23@gmail.com&content=$CONTENT" )
ID=$( echo $RESPONSE | jq '.id' )
echo "ID of new post: $ID"

echo "Checking to make sure the post was added..."
POST=$( curl -s http://localhost:5000/api/timeline_post | jq ".timeline_posts | .[] | select(.id == $ID)" )
if [[ -z $POST ]]
then
    echo "Post wasn't added!" ; exit 1;
else
    echo "Post was added!"
fi

echo "Deleting post..."
curl -X DELETE "http://localhost:5000/api/timeline_post/$ID"
