import pip._vendor.requests as requests
from folder import Folder
from types import NoneType

 
class TestAPI:
    def test_create_folder(self):
        response = requests.post("http://localhost:5000/folder?parent=root&name=child&lim=64")
        assert response.status_code == 201
        assert response.json().get('message') == 'Folder was created'
        assert response.json().get('folder').get('lim') == 64
        assert response.json().get('folder').get('count') == 0
        assert not type(response.json().get('folder').get('parent')) is NoneType
        response = requests.post("http://localhost:5000/folder?parent=root&name=child&lim=64")
        assert response.status_code == 400
        assert response.json().get('message') == 'Folder with this name already exists'

    def test_read_folder(self):
        response = requests.get('http://localhost:5000/folder?name=root')
        assert response.status_code == 200
        assert response.json().get('message') == 'Folder was read'
        assert response.json().get('folder').get('lim') == 64
        assert response.json().get('folder').get('count') == 1
        assert type(eval(response.json().get('folder').get('parent'))) is NoneType

    def test_move_folder(self):
        response = requests.patch("http://localhost:5000/folder?name=child&parent=root")
        assert response.status_code == 200
        assert response.json().get('message') == 'Folder was moved'
        assert type(response.json().get('folder').get('parent')) is not NoneType

    def test_delete_folder(self):
        response = requests.delete("http://localhost:5000/folder?name=child")
        assert response.status_code == 200
        assert response.json().get('message') == 'Folder was deleted'
        response = requests.delete("http://localhost:5000/folder?name=child")
        assert response.status_code == 400
        assert response.json().get('message') == 'Folder was not deleted'

    def test_create_buffer(self):
        response = requests.post("http://localhost:5000/buffer?parent=root&size=64&name=buffer")
        assert response.status_code == 201
        assert response.json().get('message') == 'Buffer file was created'
        assert isinstance(response.json().get('buffer').get('content'), list)
        assert response.json().get('buffer').get('size') == 64
        assert not type(response.json().get('buffer').get('parent')) is NoneType
        response = requests.post("http://localhost:5000/buffer?parent=root&size=64&name=buffer")
        assert response.status_code == 400
        assert response.json().get('message') == 'Buffer file with this name already exists'

    def test_read_buffer(self):
        response = requests.get("http://localhost:5000/buffer?name=buffer")
        assert response.status_code == 200
        assert response.json().get('message') == 'Buffer file was read'
        assert isinstance(response.json().get('buffer').get('content'), list)
        assert response.json().get('buffer').get('size') == 64
        assert type(response.json().get('buffer').get('parent')) is str

    def test_move_buffer(self):
        response = requests.patch("http://localhost:5000/buffer?parent=root&name=buffer")
        assert response.status_code == 200
        assert isinstance(response.json().get('buffer').get('content'), list)
        assert response.json().get('buffer').get('size') == 64
        assert response.json().get('buffer').get('parent') == "root"

    def test_push_buffer(self):
        response = requests.patch("http://localhost:5000/buffer?name=buffer&append=some_text")
        assert response.status_code == 201
        assert response.json().get('message') == 'Line was added to buffer file'

    def test_consume_buffer(self):
        response = requests.patch("http://localhost:5000/buffer?name=buffer&consume=true")
        assert response.status_code == 200
        assert response.json().get('message') == 'Line was consumed from buffer file'

    def test_delete_buffer(self):
        response = requests.delete("http://localhost:5000/buffer?name=buffer")
        assert response.status_code == 200
        assert response.json().get('message') == 'Buffer file was deleted'
        response = requests.delete("http://localhost:5000/buffer?name=buffer")
        assert response.status_code == 400
        assert response.json().get('message') == 'Buffer file was not deleted'

    def test_create_binary(self):
        response = requests.post("http://localhost:5000/binary?name=binary&parent=root&content=test")
        assert response.status_code == 201
        assert response.json().get('message') == 'Binary file was created'
        assert response.json().get('binary').get('content') == 'test'
        assert not type(response.json().get('binary').get('parent')) is NoneType
        response = requests.post("http://localhost:5000/binary?name=binary&parent=root&content=test")
        assert response.status_code == 400
        assert response.json().get('message') == 'Binary file with this name already exists'

    def test_read_binary(self):
        response = requests.get("http://localhost:5000/binary?name=binary")
        assert response.status_code == 200
        assert response.json().get('message') == 'Binary file was read'
        assert response.json().get('binary').get('content') == 'test'
        assert type(response.json().get('binary').get('parent')) is str

    def test_move_binary(self):
        response = requests.patch("http://localhost:5000/binary?name=binary&parent=root")
        assert response.status_code == 200
        assert response.json().get('message') == 'Binary file was moved'
        assert response.json().get('binary').get('parent') == "root"

    def test_delete_binary(self):
        response = requests.delete("http://localhost:5000/binary?name=binary")
        assert response.status_code == 200
        assert response.json().get('message') == 'Binary file was deleted'
        response = requests.delete("http://localhost:5000/binary?name=binary")
        assert response.status_code == 400
        assert response.json().get('message') == 'Binary file was not deleted'

    def test_create_log(self):
        response = requests.post("http://localhost:5000/log?name=log&parent=root&content=test")
        assert response.status_code == 201
        assert response.json().get('message') == 'Log file was created'
        assert response.json().get('log').get('content') == 'test'
        assert not type(response.json().get('log').get('parent')) is NoneType
        response = requests.post("http://localhost:5000/log?name=log&parent=root&content=test")
        assert response.status_code == 400
        assert response.json().get('message') == 'Log file with this name already exists'

    def test_read_log(self):
        response = requests.get("http://localhost:5000/log?name=log")
        assert response.status_code == 200
        assert response.json().get('message') == 'Log file was read'
        assert response.json().get('log').get('content') == 'test'
        assert type(response.json().get('log').get('parent')) is str

    def test_move_log(self):
        response = requests.patch("http://localhost:5000/log?name=log&parent=root")
        assert response.status_code == 200
        assert response.json().get('message') == 'Binary file was moved'
        assert response.json().get('file').get('parent') == "root"

    def test_append_log(self):
        response = requests.patch("http://localhost:5000/log?name=log&append=test2")
        assert response.status_code == 201
        assert response.json().get('message') == 'Line was appended to log file'

    def test_delete_log(self):
        response = requests.delete("http://localhost:5000/log?name=log")
        assert response.status_code == 200
        assert response.json().get('message') == 'Log file was deleted'
        response = requests.delete("http://localhost:5000/log?name=log")
        assert response.status_code == 400
        assert response.json().get('message') == 'Log file was not deleted'
