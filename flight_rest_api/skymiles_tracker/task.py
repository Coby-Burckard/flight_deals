from background_task import background
import time

@background()
def check_delta():
    print('running')
    return ''