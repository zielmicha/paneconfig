import binascii, os

def write_file(path, data):
    tmp_path = path + '.tmp.' + binascii.hexlify(os.urandom(6)).decode()
    with open(tmp_path, 'wb') as f:
        if isinstance(data, str):
            f.write(data.encode('utf8'))
        else:
            f.write(data)

    os.rename(tmp_path, path)
