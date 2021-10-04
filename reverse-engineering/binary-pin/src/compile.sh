#!/usr/bin/env sh

javac Binarypin.java
jar cmf Binarypin.mf Binary-Pin.jar *.class
rm *.class