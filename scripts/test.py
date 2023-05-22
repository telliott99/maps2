import sys

def find_script_path():
    d = sys.path[0]
    parent = '/'.join(d.split('/')[:-1])
    sys.path.insert(0,parent + '/scripts')

find_script_path()

print(sys.path[0])