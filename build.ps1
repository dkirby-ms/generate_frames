#!/bin/bash

$image_name = "generate_frames"
$tag = "latest"
$acr_login_server = "bunnyacr.azurecr.io"

docker build . -t $image_name
docker tag "$image_name`:$tag" "$acr_login_server/$image_name`:$tag"
docker push "$acr_login_server/$image_name`:$tag"


# docker run -e ROBOFLOW_API_KEY="my_api_key" -e $FRAMES_PATH="c:\path\to\images\0" "$acr_login_server/$image_name`:$tag"