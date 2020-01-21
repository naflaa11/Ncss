# -*- coding: utf-8 -*-
{
    'name': "TeleNoc HCM PRO",

    'summary': """
        Telenoc HCM is HR  module with all employee management features""",

    'description': """
        This module will help to manage your HR  department.It has all features
        related to HR like Employees salary management,leave management,expense management,
        their attendance system,payroll system .It will also help to project management you 
        can manage your running project and also process of hiring of new employees available
         in this module. In additional there are GOSI Company Contribution and deduction For Saudi Employee
         and feature of End Services Benefits.It is complete HRMS for version 12
    """,

    'author': "TeleNoc ",
    'website': "http://www.telenoc.org",


    'category': 'HR',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_expense', 'hr_attendance', 'hr_holidays', 'hr_payroll', 'hr_recruitment', 'hr_timesheet','hr_contract', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/employee_document_view.xml',
        'views/employee_check_list_view.xml',
        'views/hr_payslip_wizard_view.xml',
        'views/gosi_view.xml',
        'views/salary_rul.xml',
        'views/sequence.xml',
        'views/templates.xml',
        'data/rule.xml',




    ],
    'qweb': [
        "static/src/xml/hr_dashboard.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/hcm_banner.png'],
    'price': 77.00,
    'currency': 'USD',
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,

}
