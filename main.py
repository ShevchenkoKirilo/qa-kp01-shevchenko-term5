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
