from binary import Binary
from buffer import Buffer
from folder import Folder
from log import Log
from types import NoneType


class Test:
    root = Folder("root", 16)

    def test_folder_create(self=None):
        folder = Folder("folder", 16, Test.root)
        assert isinstance(folder, Folder)
        assert folder.name == "folder"
        assert folder.lim == 16
        assert folder.parent == Test.root
        assert type(folder.list()) is str

    def test_folder_move(self=None):
        folder = Folder("folder", 16)
        assert type(folder.parent) is NoneType
        folder.move(Test.root)
        assert folder.parent == Test.root

    def test_folder_list(self=None):
        folder = Folder("folder", 16, Test.root)
        assert type(folder.list()) is str

    def test_folder_delete(self=None):
        folder = Folder("folder", 16, Test.root)
        folder.__delete__()

        assert "folder" not in locals()

    def test_folder_delete_not_existing(self=None):
        folder = Folder("folder", 16, Test.root)
        folder.__delete__()

        try:
            folder.__delete__()
        except:
            assert True
        else:
            assert False

    def test_binary_create(self=None):
        binary = Binary("binary", "content", Test.root)
        assert isinstance(binary, Binary)
        assert binary.name == "binary"
        assert binary.content == "content"
        assert binary.parent == Test.root

    def test_binary_move(self=None):
        binary = Binary("binary", "content")
        assert type(binary.parent) is NoneType
        binary.move(Test.root)
        assert binary.parent == Test.root

    def test_binary_readfile(self=None):
        binary = Binary("binary", "content", Test.root)
        assert binary.readfile() == "content"

    def test_binary_delete(self=None):
        binary = Binary("binary", "content", Test.root)
        binary.__delete__()

        assert "binary" not in locals()

    def test_buffer_create(self=None):
        buffer = Buffer("buffer", 16, Test.root)
        assert isinstance(buffer, Buffer)
        assert buffer.name == "buffer"
        assert buffer.lim == 16
        assert buffer.parent == Test.root

    def test_buffer_move(self=None):
        buffer = Buffer("buffer", 16)
        assert type(buffer.parent) is NoneType
        buffer.move(Test.root)
        assert buffer.parent == Test.root

    def test_buffer_push(self=None):
        buffer = Buffer("buffer", 16, Test.root)
        buffer.push("content")
        assert buffer.consume() == "content"

    def test_buffer_consume(self=None):
        buffer = Buffer("buffer", 16, Test.root)
        buffer.push("content")
        assert buffer.consume() == "content"
        assert buffer.consume() is None

    def test_buffer_delete(self=None):
        buffer = Buffer("buffer", 16, Test.root)
        buffer.__delete__()

        assert "buffer" not in locals()

    def test_log_create(self=None):
        log = Log("log", Test.root)
        assert log.name == "log"
        assert log.parent == Test.root

    def test_log_move(self=None):
        log = Log("log")
        assert type(log.parent) is NoneType
        log.move(Test.root)
        assert log.parent == Test.root

    def test_log_append(self=None):
        log = Log("log", Test.root)
        log.append("content")

        assert log.readfile() == "content"

    def test_log_readfile(self=None):
        log = Log("log", Test.root)
        log.append("content")

        assert log.readfile() == "content"

    def test_log_delete(self=None):
        log = Log("log", Test.root)
        log.__delete__()

        assert "log" not in locals()
