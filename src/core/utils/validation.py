
def validate_name(name):
    if '.' in name:
        raise Exception("Invalid name %s, '.' is not allowed" % name)
