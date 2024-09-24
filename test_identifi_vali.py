import unittest
from apps.validators import Validators


class ValidatorTest(unittest.TestCase):
    def setUp(self): #prepara o lugar
        print("oi sou eu setup: test case here")

    def test_identified_valid_size(self):
        result = Validators.check_valid_identifier(self,"Rosemiro")
        self.assertTrue(result,"Identificdor Invalido")

    def test_identified_valid_number(self):
        result = Validators.check_valid_identifier(self,"rose1")
        self.assertTrue(result,"Identificdor Invalido")

    def test_idetified_init_especial_character(self):
        result = Validators.check_email(self,"ro@gmail")
        self.assertFalse(result,"Email Válido")

    def test_identified_valid_senha(self):
        result = Validators.check_password(self,"ro5emir@")
        self.assertTrue(result,"Password Invalido")

    def test_verificar_idade_0_ate_16(self):
        result = Validators.check_age_for_work(self,16)
        self.assertEqual("Não Empregar", result)

    def test_verificar_idade_17_a_18(self):
        result = Validators.check_age_for_work(self,17)
        self.assertEqual(result,"Empregado Parcial")

    def test_verificar_idade_19_a_55(self):
        result = Validators.check_age_for_work(self,20)
        self.assertEqual(result,"Empregado Integral")

    def test_verificar_idade_56_a_99(self):
        result = Validators.check_age_for_work(self,60)
        self.assertEqual(result,"Não Empregar")

    def test_verificar_idade_15(self):
        result = Validators.check_brazilian_voter(self,15)
        self.assertEqual(result,"Não Vota")

    def test_verificar_idade_18_a_69(self):
        result = Validators.check_brazilian_voter(self,30)
        self.assertEqual(result,"Obrigatório")

    def test_verificar_inverte(self):
        result = Validators.isPalindrome(s="or")
        self.assertFalse(result,"False")

    def tearDown(self):
        print("--")




if __name__ == '__main__':
    unittest.main()
