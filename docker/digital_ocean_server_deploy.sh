#! /bin/bash



git archive --format tar --output ./project.tar master

echo "Uploading the project.....:-)...Be Patient!"
rsync ./project.tar root@134.209.181.179:/tmp/project.tar
echo "Upload complete....:-)"


echo "Building the image......."
ssh -o StrictHostKeyChecking=no root@134.209.181.179 << 'ENDSSH'
    mkdir -p /app
    rm -rf /app/* && tar -xf /tmp/project.tar -C /app
    docker-compose -f /app/production.yml build

ENDSSH
echo "Build completed successfully.......:-)"