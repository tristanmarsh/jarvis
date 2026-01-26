"""Logger which only prints to stdout if verbose is set"""
class Logger:
    def __init__(self, verbose: bool):
        self.verbose = verbose
    
    def log(self,message):
        if self.verbose:
            print(f"Log: {message}")
