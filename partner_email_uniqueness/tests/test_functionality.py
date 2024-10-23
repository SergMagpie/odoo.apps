from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase, tagged
from odoo.addons.base.tests.common import DISABLED_MAIL_CONTEXT


@tagged('post_install', '-at_install')
class TestHospitalPartnerEmailUniquenessFunctionality(TransactionCase):
    """My amazing test case."""

    @classmethod
    def setUpClass(cls):
        """Class method for setting up the test case"""
        super().setUpClass()

        cls.env = cls.env['base'].with_context(**DISABLED_MAIL_CONTEXT).env

        cls.partner_1 = cls.env['res.partner'].create({
            'name': 'Test Partner 1',
            'email': 'test_partner_1@example.com',
        })
        cls.partner_2 = cls.env['res.partner'].create({
            'name': 'Test Partner 2',
            'email': 'test_partner_2@example.com',
        })

    def test_partner_email_uniqueness(self):
        """Just method for testing some test cases"""
        with self.assertRaises(ValidationError):
            self.partner_1.write({
                'email': 'test_partner_2@example.com',
            })
        with self.assertRaises(ValidationError):
            self.partner_2.write({
                'email': 'test_partner_1@example.com',
            })
        with self.assertRaises(ValidationError):
            self.partner_1.create({
                'name': 'Test Partner 3',
                'email': 'test_partner_1@example.com',
            })
        self.assertTrue(self.partner_1.create({
            'name': 'Test Partner 3',
            'email': 'test_partner_3@example.com',
        }))
