{
    'name': 'hospital managment system',
    'author': 'Yousha',
    'version': '13.0.3.0.0',
    'category': 'Tools',
    'summary': 'patient adding',
    'sequence': '10',
    'license': 'AGPL-3',
    'website': 'Hospital.com',

     'depends': ['sale',
                'mail',
                'website',
                ],
    'demo': [],
    'data': [

        'security/ir.model.access.csv',
        'views/patient.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}

