import Constants

class Camera:

    cameras = {
        "top": 0,
        "bottom": 1,
        "3d": 2
    }

    resolutions = {
        "40x30": 8,
        "80x60": 7,
        "160x120": 0,
        "320x240": 1,
        "640x480": 2,
        "1280x960": 3,
        "2560x1920": 4
    }

    formats = {
        "bmp" :"bmp",
        "dib" :"dib",
        "jpeg" :"jpeg",
        "jpg" :"jpg",
        "jpe" :"jpe",
        "png" :"png",
        "pbm" :"pbm",
        "pgm" :"pgm",
        "ppm" :"ppm",
        "sr" :"sr",
        "ras" :"ras",
        "tiff" :"tiff",
        "tif" :"tif"
    }

    __camera_id = cameras["3d"]#Constants().c3d]
    __resolution = resolutions["640x480"]#Constants().r640x480] # id for ALPhotoCapture 640x480px
    __picture_format = formats["jpeg"]#Constants().fjpeg]

    def __init__(self, robot):
        self.__al_photo = robot.ALPhotoCapture
        self.configure_camera(self.__camera_id, self.__resolution, self.__picture_format)

    def configure_camera(self, camera_id, resolution, format):
        self.__al_photo.setCameraID(camera_id)
        self.__al_photo.setResolution(resolution)
        self.__al_photo.setPictureFormat(format)

    def take_picture(self, path, file_name):
        self.__al_photo.takePicture(path, file_name)