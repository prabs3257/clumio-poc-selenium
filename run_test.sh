#!/bin/bash

# Create chrome node
current_time=$(date +%s%3N)
chrome_container_id=$(docker run -d --name chrome-$current_time --net grid-network --shm-size=2gb \
-e SE_EVENT_BUS_HOST=selenium-hub \
-e SE_EVENT_BUS_PUBLISH_PORT=4442 \
-e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
-e SE_NODE_OVERRIDE_MAX_SESSIONS=true \
-e SE_NODE_MAX_SESSIONS=1 \
selenium/node-chrome:4.10.0-20230607)

# Create video recording node for chrome
vid_container_id=$(docker run -d --name chrome-video-$current_time --net grid-network \
-v $PWD/tmp/videos:/videos \
-e DISPLAY_CONTAINER_NAME=chrome-$current_time \
-e FILE_NAME=chrome_video_$current_time-$1.mp4 \
selenium/video:ffmpeg-4.3.1-20230607)

# echo "id: $vid_container_id"

# Run pytest
pytest /Users/prabhavchopra/Documents/docker-selenium/test_clumio.py::TestClumio::$1 -v  # Replace with your pytest command and options

# Check the exit code of pytest
if [ $? -eq 0 ]; then
    
    # Stop the Docker container
    docker stop $chrome_container_id
    docker rm $chrome_container_id

    docker stop $vid_container_id
    docker rm $vid_container_id

    echo "Complete"
else
    echo "Test failed"
fi
