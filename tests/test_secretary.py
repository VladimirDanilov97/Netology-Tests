from unittest import TestCase, main
import unittest
from unittest.mock import patch
import sys
sys.path.append('..')
from app import *


class SecretaryTest(TestCase):

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('11-2'), True)
        self.assertEqual(check_document_existance('*'), False)
    

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')
    

    @patch('builtins.input', return_value='10006')
    def test_delete_doc(self, mock_input):
        self.assertEqual(delete_doc(), ('10006', True))
    

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('1', 'passport', 'Owner', '1'),
        '1')


    @unittest.expectedFailure
    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name_fail(self, mock_input):
        self.assertEqual(get_doc_owner_name(), 'Геннадий')
  

    def test_get_all_doc_owners_names(self):
        self.assertSetEqual(get_all_doc_owners_names(), 
                            {"Василий Гупкин", "Геннадий Покемонов", 'Owner'})
    

    def test_remove_doc_from_shelf(self):
        self.assertEqual(remove_doc_from_shelf('11-2'), '11-2')
        self.assertEqual(remove_doc_from_shelf('11-2'), None)
    

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))
        pass


    @patch('builtins.input', return_value='5')
    def test_add_new_shelf_input(self, mock_input):
        self.assertEqual(add_new_shelf(), ('5', True))


    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf(doc_number='11-2', shelf_number='5'), None)
        self.assertEqual(append_doc_to_shelf(doc_number='1234', shelf_number='4'), ['1234'])

   
    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('11-2'), '1')
    

    def test_move_doc_to_shelf(self):
        self.assertEqual(move_doc_to_shelf(
            user_doc_number='2207 876234',
            user_shelf_number='2'), ('2207 876234', '2'))
    

    def test_show_document_info(self):
        self.assertEqual(show_document_info(documents[0]),
        'passport "2207 876234" "Василий Гупкин"')
    

    def test_show_all_docs_info(self):
        self.assertEqual(set(show_all_docs_info()),
        {'passport "2207 876234" "Василий Гупкин"',
         'invoice "11-2" "Геннадий Покемонов"',
         'passport "1" "Owner"',})
       
    
if __name__ == '__main__':
    main()