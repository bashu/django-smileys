VERSION = (0, 2, 0, 'beta')

def version():
    return '%s.%s.%s-%s' % VERSION

def get_version():
    return 'django-smileys %s' % version()
