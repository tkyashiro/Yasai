import time
import datetime
import shutil

def take_image():
    try:
#        import picamera
#        with picamera.PiCamera() as camera:
#            camera.resolution = (1024, 768)
#            camera.start_prewview()
#
#            # warm up
#            time.sleep(2)
#
            now = datetime.datetime.now()
            fname = now.strftime("%Y%m%d%H%M%S") + ".jpg"
            fullpath = "/var/Yasai/images/" + fname

#            camera.capture(fullpath)

            shutil.copy2("./static/imgs/test.jpg", fullpath)

            return True, fname, now
    except Exception as exc:
        print exc
        return False, None, None

