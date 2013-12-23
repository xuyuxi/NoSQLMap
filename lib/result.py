
from exceptions import ParameterError 
from log import Log


class Result():
    """support class for saving a result, and print it
    Structure include METHOD (get or post), url, parameters.
    If a GET parameters is empty and url have injection
    """
    def __init__(self, method, params):
        """if GET params has only url, if POST also payload"""
        try:
            self.url=params[0]
            if method  == 1: #GET
                self.method="GET"
            elif method ==2:
                self.method = "POST"
                self.payload=params[1]
            else:
                Log.error("Missing method in Results")
                raise ParameterError
        except IndexError:
            Log.error("Missing params in Results")
            raise ParameterError

    def write(fd):
        m = "%s %s %s" %(self.method, self.url, self.payload)
        print >> fd, m 
