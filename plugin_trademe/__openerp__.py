{
    'name' : 'Trademe Plug-In',
    'version' : '1.5',
    'author' : 'Matiar Rahman (matiar.rahman@gmail.com)',    
    'depends' : ['sale'],
    'category': 'Generic Modules/Others',
    'description': """
This module provides the Trademe Plug-in.
=========================================
      """,
    'update_xml': ['security/trademe_security.xml',
                   'views/main.xml', 
                   'views/members.xml', 
                   'views/listing.xml', 
                   'views/questions.xml', 
                   'views/data.xml'],
    'auto_install': False,
    'installable': True,
    'active': True,
}
