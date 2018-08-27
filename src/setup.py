import sys

def get_repo_name():
    return sys.argv[1]

def get_users_list():
    return sys.argv[2]

def get_admin_id():
    return sys.argv[3]

print(sys.argv)

print(get_repo_name())
print(get_users_list())
print(get_admin_id())
