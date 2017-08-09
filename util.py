from enum import Enum


TEST_STATUS = Enum('Test_Status', 'ready in_development unused')

def set_status(status, tests=None):
    """Add the status to the function
    If a dict is passed, store the function"""
    def decorator(func):
        func.status = status
        if tests is not None:
            if status not in tests:
                tests[status] = list()
            tests[status].append(func)
        return func
    return decorator
