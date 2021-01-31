from PIL import Image, ImageDraw
import qrcode

from .forms import CreateStudentForm
from .views import teacher_ui

data=""
img=qrcode.make(data)
img.save("filename")
