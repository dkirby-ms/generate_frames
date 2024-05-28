import cv2, datetime, time, os
from roboflow import Roboflow

# main.py
imagepath = "/frames"
key = os.environ["ROBOFLOW_API_KEY"]
rf = Roboflow(api_key=key)

def rf_upload(path):
    try:    
        workspaceId = 'bunnyai'
        projectId = 'animals-7fizt'
        project = rf.workspace(workspaceId).project(projectId)

        # Upload the image to your project
        print(f"Uploading {path} to Roboflow project {workspaceId}/{projectId}")
        project.upload(f"{path}")

        # Delete stored image
        os.remove(f"{path}")

    except:
        print("Error storing image to disk or uploading image to Roboflow")

def main():
    # Open video capture
    cap = cv2.VideoCapture("rtsp://admin:BunnyAI!!@192.168.2.253:8554")

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video capture")
        return

    # Set the frame rate (15 frames per second)
    frame_rate = 15
    delay = int(1000 / frame_rate)

    while True:
        # Read frame from video capture
        ret, frame = cap.read()

        # Check if frame was successfully read
        if not ret:
            print("Error reading frame")
            break

        # Write frame to disk
        try: 
            current_time = datetime.datetime.now()
            file_name = current_time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = file_name + ".jpg"
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            with open(f"{imagepath}/{file_name}", "wb") as f:
                f.write(encodedImage)
        except:
            print("Error storing image")
        
        rf_upload(f"{imagepath}/{file_name}")

        # Wait for 15 seconds
        time.sleep(15)

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()