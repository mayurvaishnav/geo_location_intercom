import sys
import os
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import unittest
from src.utils.fileIOHelper import readFile, writeIntoFile
import src.constants.constant as const

class TestFileIOHelper(unittest.TestCase):
	"""
	Test cases for File input output helper class
	"""
	inputFile = const.CUSTOMER_FILE_PATH
	outputFile = path.join(const.ROOT_DIR, 'output/test_output.txt')

	def test_readFile(self):
		data = readFile(self.inputFile)
		self.assertTrue(data != None)
		self.assertIsInstance(data, list)

	# Negative case when path is null or file does not exist
	def test_readFile_0(self):
		try:
			data = readFile("/file/not/found")
		except Exception as e:
			self.assertTrue(True)
		else:
			self.fail('Exception not raised')

	def test_writeIntoFile(self):
		string = "Unit Test output"
		try:
			filePath = writeIntoFile(string, self.outputFile)
			content = open(self.outputFile)
			result = content.read()
			content.close()
		except Exception as e:
			self.fail('Exception not raised')
		finally:
			os.remove(self.outputFile)
		self.assertEqual(result, string)

	# test case if no such directory exists
	def test_writeIntoFileWithNoDir(self):
		outputFileTest = path.join(const.ROOT_DIR, 'output_test/test_output.txt')
		string = "Unit Test output"
		try:
			filePath = writeIntoFile(string, self.outputFileTest)
		except FileNotFoundError as e:
			self.assertTrue(True)
		except Exception as e:
			self.assertTrue(True)
