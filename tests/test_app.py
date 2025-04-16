import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import hello

def test_hello():
    assert hello() == "Hello, DevOps World!"
    
if __name__ == "__main__":
    test_hello()
    print("All tests passed!")