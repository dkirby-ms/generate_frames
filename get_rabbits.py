# Import necessary libraries
from bing_image_downloader import downloader

# Define search params
query = "rabbit"
limit = 100  # limit to 100 images
output_dir = "c:/dev/cameras/bunnyai/images"  # replace with your directory

# Download images
downloader.download(query, limit=limit, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)

print(f"Images downloaded to {output_dir}/{query}")



