/* Generated code for Python source for module 'numpy.lib.info'
 * created by Nuitka version 0.5.21.2
 *
 * This code is in part copyright 2016 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.hpp"

#include "__helpers.hpp"

/* The _module_numpy$lib$info is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_numpy$lib$info;
PyDictObject *moduledict_numpy$lib$info;

/* The module constants used, if any. */
static PyObject *const_str_digest_3d6f4969fab4e183f7b0aa22a8f466dd;
extern PyObject *const_str_chr_42;
extern PyObject *const_str_plain_core;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain___file__;
static PyObject *const_list_str_plain_core_str_plain_testing_list;
static PyObject *const_str_digest_4744f3ae17be89ca353c6bb11dbefb6f;
extern PyObject *const_list_str_chr_42_list;
extern PyObject *const_str_plain_division;
extern PyObject *const_str_plain_print_function;
extern PyObject *const_str_plain_global_symbols;
static PyObject *const_str_digest_7d8134536515680674da910bddb241f8;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_testing;
extern PyObject *const_str_plain_depends;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_str_digest_3d6f4969fab4e183f7b0aa22a8f466dd = UNSTREAM_STRING( &constant_bin[ 730086 ], 6375, 0 );
    const_list_str_plain_core_str_plain_testing_list = PyList_New( 2 );
    PyList_SET_ITEM( const_list_str_plain_core_str_plain_testing_list, 0, const_str_plain_core ); Py_INCREF( const_str_plain_core );
    PyList_SET_ITEM( const_list_str_plain_core_str_plain_testing_list, 1, const_str_plain_testing ); Py_INCREF( const_str_plain_testing );
    const_str_digest_4744f3ae17be89ca353c6bb11dbefb6f = UNSTREAM_STRING( &constant_bin[ 736461 ], 50, 0 );
    const_str_digest_7d8134536515680674da910bddb241f8 = UNSTREAM_STRING( &constant_bin[ 736511 ], 14, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_numpy$lib$info( void )
{
    // The module may not have been used at all.
    if (constants_created == false) return;


}
#endif

// The module code objects.


static void createModuleCodeObjects(void)
{

}

// The module function declarations.


// The module function definitions.



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef_numpy$lib$info =
{
    PyModuleDef_HEAD_INIT,
    "numpy.lib.info",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#if PYTHON_VERSION >= 300
extern PyObject *metapath_based_loader;
#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( numpy$lib$info )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_numpy$lib$info );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION >= 350
    PyType_Ready( &Nuitka_Coroutine_Type );
    PyType_Ready( &Nuitka_CoroutineWrapper_Type );
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    createModuleConstants();
    createModuleCodeObjects();

    // puts( "in initnumpy$lib$info" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_numpy$lib$info = Py_InitModule4(
        "numpy.lib.info",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_numpy$lib$info = PyModule_Create( &mdef_numpy$lib$info );
#endif

    moduledict_numpy$lib$info = (PyDictObject *)((PyModuleObject *)module_numpy$lib$info)->md_dict;

    CHECK_OBJECT( module_numpy$lib$info );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_7d8134536515680674da910bddb241f8, module_numpy$lib$info );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_numpy$lib$info );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !0
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#endif

    // Temp variables if any
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;

    // Module code.
    tmp_assign_source_1 = const_str_digest_3d6f4969fab4e183f7b0aa22a8f466dd;
    UPDATE_STRING_DICT0( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_4744f3ae17be89ca353c6bb11dbefb6f;
    UPDATE_STRING_DICT0( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "division");
    UPDATE_STRING_DICT0( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain_division, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_4 );
    tmp_assign_source_5 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_5 );
    tmp_assign_source_6 = LIST_COPY( const_list_str_plain_core_str_plain_testing_list );
    UPDATE_STRING_DICT1( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain_depends, tmp_assign_source_6 );
    tmp_assign_source_7 = LIST_COPY( const_list_str_chr_42_list );
    UPDATE_STRING_DICT1( moduledict_numpy$lib$info, (Nuitka_StringObject *)const_str_plain_global_symbols, tmp_assign_source_7 );

    return MOD_RETURN_VALUE( module_numpy$lib$info );
}
