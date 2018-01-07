from flask import flash
from werkzeug.utils import secure_filename
import shutil
import os

from helpers import config


def allowed_file(filename):
    return filename and filename.split('.')[-1] in config.ALLOWED_EXTENSIONS


def upload_file(file, filename, upload_folder):
    filename = secure_filename(filename)
    if file and allowed_file(filename):
        path = os.path.join(upload_folder, filename)
        file.save(path)
        return True
    else:
        flash('Please use an image with valid image extension.')
        return False


def make_dir(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)


def create_file(filename):
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.close()


def write_to_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()


def append_to_file(filename, data):
    f = open(filename, 'a')
    f.write(data + '\n')
    f.close()


def delete_file(filename):
    if os.path.exists(filename):
        os.rmdir(filename)


def delete_file_contents(filename):
    with open(filename, 'r'):
        pass


def remove_dir(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory)


def move_image(img):
    if os.path.isdir(config.DATASET_PATH):
        if os.path.isfile(os.path.join(config.UPLOAD_FOLDER, img)):
            os.rename(os.path.join(config.UPLOAD_FOLDER, img),
                      os.path.join(config.DATASET_PATH, img))
    else:
        make_dir(config.DATASET_PATH)
        move_image(img)
