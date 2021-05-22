#can predict both dicom and jpeg images
from PIL import Image
import numpy as np
from skimage import transform
from keras.models import load_model

try:
    # keras 2.2
    import keras_preprocessing.image.utils as KPImageUtils
    import keras_preprocessing.image as KPImage
except:
    # keras 2.1
    import keras.preprocessing.image as KPImage
    
from PIL import Image
import pydicom #pydicom==1.2.0

def read_dicom_image(in_path):
    img_arr = pydicom.read_file(in_path).pixel_array
    return img_arr/img_arr.max()
    
class medical_pil():
    @staticmethod
    def open(in_path):
        if '.dcm' in in_path:
            c_slice = read_dicom_image(in_path)
            int_slice =  (255*c_slice).clip(0, 255).astype(np.uint8) # 8bit images are more friendly
            return Image.fromarray(int_slice)
        else:
            return Image.open(in_path)
    fromarray = Image.fromarray
    
KPImageUtils.pil_image = medical_pil
  

def load(filename):
   if '.dcm' in filename:
     np_image = KPImageUtils.pil_image.open(filename)
   else:
     np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (224, 224, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

def test(image_path):
  #output pred_score returns an array like this [[9.256325e-08, 0.9999999]] where the first value 0 (not pneumonia), second value is 1 (pneumonia)
  #load model
   model_path = "./densenet121 male female pa rsna normal and pneumonea 11 epochs train auc 96% test auc 67% last to 14_14 layer unfreeze_new augmentation_zoom.h5"
   model = models.load_model(model_path)
   image = load(image_path)
   pred_score = model.predict(image)
   return pred_score
