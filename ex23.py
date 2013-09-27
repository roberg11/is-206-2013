##import sys
##import unittest
##

## These 3 lines imports other python files and imports
## methods used in those files
##from runner.runner_tests.test_mountain import TestMountain
##from runner.runner_tests.test_sensei import TestSensei
##from runner.runner_tests.test_helper import TestHelper


##

## Definition taking no parameters. Utilizes the package unittest
## and the built-in method for that package TestSuite()

##def suite():
##    suite = unittest.TestSuite()
##    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMountain))
##    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSensei))
##    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHelper))
##    return suite
##

## Testing function that compares the definition name in the main file
## to the testing definition.

##if __name__ == '__main__':
##    res = unittest.TextTestRunner(verbosity=2).run(suite())
##    sys.exit(not res.wasSuccessful())


