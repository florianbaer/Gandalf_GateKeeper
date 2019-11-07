#!/usr/bin/python

# Needed library:
# sudo pip install CppHeaderParser

import sys
import CppHeaderParser
import re
import glob

# Script that parses all the proxy header files of naoqi
# usually found at naoqi-sdk-2.1.4.13-linux64/include/alproxies
# (but adapted to your version)
# and creates python files with classes for each
# module with documentation to enable autocompletion
# and docstrings showage
#
# Author: Sammy Pfeiffer <Sammy.Pfeiffer at student.uts.edu.au>


def parse_doxygen(docs_str):
    """
    Given a doxygen string, parse it into summary, params, return.
    """
    # General cleanup
    docs_str = docs_str.replace('///', '')
    docs_str = docs_str.replace('\n', '')

    # Get summary
    summary = ''
    s = re.search('\<summary\>.*\<\/summary\>', docs_str)
    if s:
        summary = s.group()
        summary = summary.replace('<summary>', '')
        summary = summary.replace('</summary>', '')
        summary = summary.strip()
        docs_str = docs_str[s.end():]

    # Get params
    params = []
    ps = re.search('\<param name\=\"[a-zA-Z0-9_]*\"\>', docs_str)
    while ps:
        p = ps.group()
        docs_str = docs_str[ps.end():]
        p = p.replace('<param name="', '')
        p = p.replace('">', '')

        pdesc = re.search('.*?\<\/param>', docs_str)
        if pdesc:
            desc = pdesc.group()
            docs_str = docs_str[pdesc.end():]
            desc = desc.replace('<param name="' + p + '">', '')
            desc = desc.replace('</param>', '')
            desc = desc.strip()

        d = {'param_name': p,
             'param_description': desc}
        params.append(d)

        # Check for a next param...
        ps = re.search('\<param name\=\"[a-zA-Z0-9_]*\"\>', docs_str)

    # Get returns
    return_str = ''
    r = re.search('\<returns\>.*\<\/returns\>', docs_str)
    if r:
        return_str = r.group()
        return_str = return_str.replace('<returns>', '')
        return_str = return_str.replace('</returns>', '')
        return_str = return_str.strip()

    return summary, params, return_str


# Skeletons for creating the Python class files
header_skeleton = """#!/usr/bin/env python
# Class autogenerated from HEADERFILE
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running




"""

class_skeleton = """
class PROXYCLASSNAME(object):
    def __init__(self, session): \n        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("PROXYCLASSNAME")
"""

method_skeleton = '''
    def METHOD_NAME(METHOD_ARGS):
        """DOCSTRING
        """
        if not self.proxy:
            self.proxy = self.session.service("PROXYCLASSNAME")
        return self.proxy.ORIGINAL_NAME_OF_METHOD(CALL_ARGS)
'''


def create_python_class(header_file, class_name, methods, path,
                        ignore_method_names=[]):
    with open(path + class_name + ".py", 'w') as f:
        header = header_skeleton.replace('HEADERFILE', header_file)
        header = header.replace('PROXYCLASSNAME', class_name)
        f.write(header)

        class_code = class_skeleton.replace('PROXYCLASSNAME', class_name)
        f.write(class_code)

        method_names = []
        for m in methods:
            if m['name'] in ignore_method_names:
                continue
            # Deal with same-name methods
            # because of different number or type of params
            # adding method_nameX where X is a number starting on 2
            if m['name'] not in method_names:
                method_names.append(m['name'])
            else:
                counter = 2
                new_name = m['name'] + str(counter)
                while new_name in method_names:
                    counter += 1
                    new_name = m['name'] + str(counter)
                method_names.append(new_name)
                m['name_original'] = m['name']
                m['name'] = new_name
            sphinx_docs = m['docs']['summary']
            if m['parameters'] or m['returns'] != 'void':
                sphinx_docs += "\n\n"
            method_code = method_skeleton.replace('METHOD_NAME', m['name'])
            method_code = method_code.replace(
                'ORIGINAL_NAME_OF_METHOD', m.get('name_original', m['name']))
            if not m['parameters']:
                method_code = method_code.replace('METHOD_ARGS', 'self')
                method_code = method_code.replace('CALL_ARGS', '')
            else:
                params_str = ''
                for idx, p in enumerate(m['parameters']):
                    params_str += p['name']
                    if p != m['parameters'][-1]:
                        params_str += ", "

                    t = p['raw_type']
                    typ = t if t != 'std::string' else "str"
                    sphinx_docs += "        :param " + \
                        typ + " " + p['name'] + ": "
                    sphinx_docs += m['docs']['params'][idx]['param_description']
                    if p != m['parameters'][-1]:
                        sphinx_docs += "\n"

                method_code = method_code.replace('CALL_ARGS', params_str)
                method_args = "self, " + params_str
                method_code = method_code.replace('METHOD_ARGS', method_args)
            method_code = method_code.replace('PROXYCLASSNAME', class_name)

            t = m['returns']
            typ = t if t != 'std::string' else "str"
            if typ != 'void':
                if m['parameters']:
                    sphinx_docs += "\n"
                sphinx_docs += "        :returns " + typ + ": "
                sphinx_docs += m['docs']['returns']

            method_code = method_code.replace('DOCSTRING', sphinx_docs)

            f.write(method_code)


# All classes are inside of this, I believe
classname = "ALPROXIES_API"

if len(sys.argv) > 1:
    path = sys.argv[1]
    if not path.endswith('/'):
        path += '/'
else:
    path = './'

methods_to_ignore = [
    'exit',  # Unloads the class form the system
    'getBrokerName',  # Not implemented
    'getGenericProxy',  # C++ only
    'getMethodHelp',  # C++ only
    'getMethodList',  # Returns a list with methods we can't call from Python
    'getModuleHelp',  # Does nothing
    'getUsage',  # Only for C++ methods
    'isRunning',  # Need a task ID to check MAYBE THIS SHOULD STAY
    'pCall',  # C++ thing
    'stop',  # C++
    'proxy',  # C++
    'wait',  # C++ MAYBE SHOULD STAY?
]


# Actually go and parse all the files
header_files = glob.glob(path + '*proxy.h')
for h in header_files:
    print("Analysing header file: " + h)
    try:
        # cppHeader = CppHeaderParser.CppHeader("albehaviormanagerproxy.h")
        cppHeader = CppHeaderParser.CppHeader(h)
    except CppHeaderParser.CppParseError as e:
        print(e)

    this_class = cppHeader.classes[classname]
    print("Number of public methods %d" %
          (len(this_class["methods"]["public"])))

    # Get constructor name so we know the actual remote method name with caps
    # and all
    remote_class_name = ''
    for m in this_class["methods"]["public"]:
        if m['constructor']:
            remote_class_name = m['name']
    remote_class_name = remote_class_name[:-5]  # We remove the word 'Proxy'

    print("The remote class is called: " + remote_class_name)

    print("And has the methods (ignoring constructors and destructors): ")
    methods_list_of_dicts = []
    for m in this_class["methods"]["public"]:
        # Ignore constructor and destructors
        if not m['constructor'] and not m['destructor']:
            print("------------------------------------------------------")
            print("  " + m['name'])
            print("  C++        : " + m['debug'])
            param_str = ''
            for param in m['parameters']:
                param_str += param['name'] + " (" + param['raw_type'] + ") "

            nprms = str(len(m['parameters']))
            print("  Params " + nprms + ":      " + param_str)

            print("  Return type: " + m['returns'])
            summary, params, returns = parse_doxygen(m['doxygen'])
            print("  Docs:        ")
            print("       Summary: " + summary)
            print("       Params:  " + str(params))
            print("       Returns: " + returns)

            print
            print

            method_dict = {}
            method_dict['name'] = m['name']
            method_dict['c++'] = m['debug']
            method_dict['parameters'] = m['parameters']
            method_dict['docs'] = {'summary': summary,
                                   'params': params,
                                   'returns': returns}
            method_dict['returns'] = m['returns']

            methods_list_of_dicts.append(method_dict)

    create_python_class(header_file=h, class_name=remote_class_name,
                        methods=methods_list_of_dicts, path=path,
                        ignore_method_names=methods_to_ignore)
