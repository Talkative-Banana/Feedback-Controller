import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lakshay/Walt/Sem7/IRob/Project/Feedback_Controller/install/fc'
