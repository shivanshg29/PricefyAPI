from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2 as cv
# Create your views here.

def videoCap():
    cap=cv.VideoCapture(0)

    while True:
        succ,frame=cap.read()
        if not succ:
            break


        ret, buffer = cv.imencode('.jpg', frame)
        if not ret:
            continue
        
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    
    cap.release()

def video_feed(request):
    return StreamingHttpResponse(videoCap(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def live_feed_page(request):
    return render(request, 'videos.html') 
