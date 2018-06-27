from keras.applications.inception_resnet_v2 import InceptionResNetV2, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
from translate import Translator

class IRNet():
    def load_model(self):
        self.model = InceptionResNetV2()
    def translate(self, x):
        res = ''
        if '_' in x:
          for i in x.split('_'):
             res = res + ' ' + i
        else:
           res = x
        print(res.strip())
        translator= Translator(to_lang="zh")
        return translator.translate(res)
    def predict(self, img_path):
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        preds = self.model.predict(x)
        res = decode_predictions(preds, top=1)[0][0][1]
        return self.translate(res)

