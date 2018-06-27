# -*- coding: utf-8 -*-
import os
from flask import Flask, request, Response
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import json
from IRNet import IRNet
from Spider import Spider

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+'/upload'

net = IRNet()
net.load_model()
net.predict('1.jpg')
spider = Spider()

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

#net = IRNet()
#net.load_model()

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>图片上传</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=photo>
         <input type=submit value=上传>
    </form>
    '''

@app.route('/certificate/<md5>')
def certificate(md5):
    # 去掉了web3.py调用
    print(md5)
    r = {}
    r['error'] = 0
    r['result'] = '0xc0356bfa8db3d304b108aee3d437461e656cbf2bb9cdfb5d5877bed1b4424eb6'
    return Response(json.dumps(r), mimetype='application/json')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        r = {}
        filename = photos.save(request.files['photo'])
        name =  net.predict(app.config['UPLOADED_PHOTOS_DEST'] + '/'  + filename)
        res = spider.get_data(name)
        if res:
           r['result'] = res
        else:
           r['result'] = None
           r['error'] = 1
        r['error'] = 0
        r['name'] = name
        r['filename'] = filename
        file_url = photos.url(filename)
        r['fileurl'] = file_url
        return Response(json.dumps(r), mimetype='application/json') 
    return html


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
