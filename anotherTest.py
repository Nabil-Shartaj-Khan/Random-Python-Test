def testModule():
    print("This message is from the testModule from anotherTest file")

def testAnModule():
    print("This is just another function")

import anotherTest
anotherTest.hello()
