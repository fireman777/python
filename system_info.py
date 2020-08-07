#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, platform

# Get all given arguments except the first one (script name)
given_arguments = sys.argv[1:]
allowed_arguments=['-a', '-dn', '-f', '-m', '-n', '-nm', '-p', '-proc', '-pc', '-pi', '-pv', '-pvt', '-r', '-s', '-sa', '-sv', '-v', '-vs', '-h']


if len(given_arguments)!=1:
    print('Error: Allowed only 1 argument. Possible such options:{}. -h for help.'.format(allowed_arguments))
#    sys.exit()
else:
    given_argument = given_arguments[0]
    if given_argument in allowed_arguments:
        if given_argument=="-a":
            print(platform.architecture())
        elif given_argument=="-dn":
            print((platform.DEV_NULL)) if platform.system()=="Linux" else print('Error: this is not Linux!')
        elif given_argument=="-f":
            print(platform.__file__)
        elif given_argument=="-m":
            print(platform.machine())
        elif given_argument=="-n":
            print(platform.node())
        elif given_argument=="-nm":
            print(platform.__name__)
        elif given_argument=="-p":
            print(platform.platform())
        elif given_argument=="-proc":
            print(platform.processor())
        elif given_argument=="-pc":
            print(platform.python_compiler())
        elif given_argument=="-pi":
            print(platform.python_implementation())
        elif given_argument=="-pv":
            print(platform.python_version())
        elif given_argument=="-pvt":
            print(platform.python_version_tuple())
        elif given_argument=="-r":
            print(platform.release())
        elif given_argument=="-s":
            print(platform.system())
        elif given_argument=="-sa":
            print(platform.system_alias(platform.system(), platform.release(), platform.version()))
        elif given_argument=="-sv":
            print(platform._sys_version())
        elif given_argument=="-v":
            print(platform.version())
        elif given_argument=="-vs":
            print(platform.__version__)
        else:
            print('Help:This csrypt shows info about platform. Available argument are available below.\nFlag:\tInfo about:')
            print('-a\tarchitecture\n-m\tnachine\n-n\tnode\n-dn\tDEV_NULL\n-f\tfile\n-m\tmachine\n-n\tnode\n-nm\tname\n-p\tplatform')
            print('-proc\tprocessor\n-pc\tpython_compiler\n-pi\tpython_implementation\n-pv\tpython_version')
            print('-pvt\tpython_version_tuple \n-r\trelease \n-s\tsystem \n-sa\tsystem_alias(system, release, version)\n-sv\tsys_version\n-v\tversion\n-h\thelp')
    else:
        print('Error: Allowed only such argments: {}. -h for help.'.format(allowed_arguments))

