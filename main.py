from binary import Binary
from buffer import Buffer
from folder import Folder
from log import Log

from tests import Test

Test.test_folder_create()
Test.test_folder_move()
Test.test_folder_list()
Test.test_folder_delete()
Test.test_folder_delete_not_existing()

Test.test_binary_create()
Test.test_binary_move()
Test.test_binary_readfile()
Test.test_binary_delete()

Test.test_buffer_create()
Test.test_buffer_move()
Test.test_buffer_push()
Test.test_buffer_consume()
Test.test_buffer_delete()

Test.test_log_create()
Test.test_log_move()
Test.test_log_append()
Test.test_log_readfile()
Test.test_log_delete()

root = Folder("root", 16)
folder1 = Folder("folder1", 8, root)
folder2 = Folder("folder2", 8, root)
folder3 = Folder("folder3", 8, folder1)
binary1 = Binary("binary1", "random content", folder3)
binary2 = Binary("binary2", "random content", folder1)
buffer = Buffer("buffer", 8, folder2)
log = Log("log", root)

print(root.list())


