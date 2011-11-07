import os, shutil, unittest
from test.testing import *

from keepnote import PROGRAM_NAME, PROGRAM_VERSION_TEXT

def mk_clean_dir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.makedirs(dirname)
    

class TestCaseInstall (unittest.TestCase):
    
    def setUp(self):      
        pass


    def old_test_distutil(self):
        """Test distutil install"""
        
        install_dir = "test/tmp/distutil"
        home_dir = "test/tmp/home"
        
        mk_clean_dir(install_dir)
        mk_clean_dir(home_dir)
        
        self.assertEquals(
            os.system("python setup.py install --prefix=%s" % install_dir),
            0)

        self.assertEquals(
            os.system("HOME=%s %s/bin/keepnote --no-default" %
                      (home_dir, install_dir)),
            0)


    def test_distutil_sdist(self):
        """Test distutil install"""

        pkg = "keepnote-%s" % PROGRAM_VERSION_TEXT
        sdist = "dist/%s.tar.gz" % pkg
        install_dir = "test/tmp/distutil"
        home_dir = "test/tmp/home"
        
        mk_clean_dir(install_dir)
        mk_clean_dir(home_dir)

        self.assertEquals(
            os.system("tar zxv -C %s -f %s" % (install_dir, sdist)),
            0)
        
        self.assertEquals(
            os.system("/usr/bin/python %s/%s/setup.py install --home=%s" %
                      (install_dir, pkg, install_dir)),
            0)

        os.system("cp ~/.Xauthority %s" % home_dir)

        cmd = "HOME=%s; PYTHONPATH=%s/lib/python; python %s/bin/keepnote --no-default" % (home_dir, install_dir, install_dir)

        print
        print cmd
        self.assertEquals(os.system(cmd), 0)



if __name__ == "__main__":
    test_main()
