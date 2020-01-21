# -*- coding: utf-8 -*-
{
    'name': "Hcm Pro",

    'summary': """
        human capital management system""",

    'description': """
        Human capital management system that can manage Employee salary,
        Employee Documents and Employee Training ,Appraisal ,And Resignation process
        and also cover all employee related Detail.
    """,

    'author': "Muhammad Danish Hassan",
    'website': "http://www.telenoc.org",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base_setup', 'hr', 'mail', 'hr_payroll', 'hr_contract',
                'resource', 'hr_gamification', 'hr_holidays','survey', 'hr_recruitment', 'project'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'security/hr_appraisal_security.xml',
        'views/templates.xml',
        'views/applicant_profile_report_view.xml',
        'views/hr_recruitment_employee_views.xml',
        # 'views/hr_recruitment_views.xml',
        'views/training_views.xml',
        'views/hr_views.xml',
        'views/employee_check_list_view.xml',
        'views/employee_document_view.xml',
        'views/gosi_view.xml',
        'views/hr_payslip_wizard_view.xml',
        'views/sequence.xml',
        'views/hr_employee_view.xml',
        'views/hr_employee.xml',
        'views/resignation_view.xml',
        'views/resignation_sequence.xml',
        'views/approved_resignation.xml',
        'views/hr_notification.xml',
        'views/leave_request_alias_view.xml',
        'views/hr_leave_template.xml',
        'views/res_config_views.xml',
        'views/hr_appraisal_form_view.xml',
        'views/hr_appraisal_survey_views.xml',
        'views/view_leave_refuse_reason_form.xml',
        'views/project_task_type_view.xml',
        'views/project_task_view.xml',
        'wizard/select_training_view.xml',
        'wizard/add_refuse_reason_view.xml',
        'data/rule.xml',
        'data/resign_employee.xml',
        'data/hr_appraisal_stages.xml',
    ],
    'images': ['static/description/cover.png'],
    'price': 60.00,
    'currency': 'USD',
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    "installable": True,
    "application": True,
    "auto_install": False,
}
