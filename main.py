# https://github.com/lefticus/cpp_weekly/issues/220
import cppyy

cppyy.include("test.hpp")
cppyy.gbl.go()

