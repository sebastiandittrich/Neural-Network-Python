/* Generated code for Python source for module 'numpy.random.info'
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

/* The _module_numpy$random$info is a Python object pointer of module type. */

/* Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module_numpy$random$info;
PyDictObject *moduledict_numpy$random$info;

/* The module constants used, if any. */
static PyObject *const_list_f6e7aa5ecf966dc33f39bff68dc7a81a_list;
extern PyObject *const_list_str_plain_core_list;
extern PyObject *const_str_plain___all__;
extern PyObject *const_str_plain_absolute_import;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_digest_98f8aeb3b26a2825133f47c32c00098f;
extern PyObject *const_str_plain_division;
static PyObject *const_str_digest_2e663657fd96b9bd013cc8ff692de76e;
static PyObject *const_str_digest_7aa49835c293dc919e8051773a781636;
extern PyObject *const_str_plain_core;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain_depends;
extern PyObject *const_str_plain_print_function;

static bool constants_created = false;

static void createModuleConstants( void )
{
    const_list_f6e7aa5ecf966dc33f39bff68dc7a81a_list = PyMarshal_ReadObjectFromString( (char *)&constant_bin[ 1433330 ], 669 );
    const_str_digest_98f8aeb3b26a2825133f47c32c00098f = UNSTREAM_STRING( &constant_bin[ 1433999 ], 17, 0 );
    const_str_digest_2e663657fd96b9bd013cc8ff692de76e = UNSTREAM_STRING( &constant_bin[ 1434016 ], 4287, 0 );
    const_str_digest_7aa49835c293dc919e8051773a781636 = UNSTREAM_STRING( &constant_bin[ 1438303 ], 53, 0 );

    constants_created = true;
}

#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants_numpy$random$info( void )
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
static struct PyModuleDef mdef_numpy$random$info =
{
    PyModuleDef_HEAD_INIT,
    "numpy.random.info",   /* m_name */
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

MOD_INIT_DECL( numpy$random$info )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module_numpy$random$info );
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

    // puts( "in initnumpy$random$info" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module_numpy$random$info = Py_InitModule4(
        "numpy.random.info",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module_numpy$random$info = PyModule_Create( &mdef_numpy$random$info );
#endif

    moduledict_numpy$random$info = (PyDictObject *)((PyModuleObject *)module_numpy$random$info)->md_dict;

    CHECK_OBJECT( module_numpy$random$info );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_digest_98f8aeb3b26a2825133f47c32c00098f, module_numpy$random$info );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module_numpy$random$info );

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
    tmp_assign_source_1 = const_str_digest_2e663657fd96b9bd013cc8ff692de76e;
    UPDATE_STRING_DICT0( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_7aa49835c293dc919e8051773a781636;
    UPDATE_STRING_DICT0( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_assign_source_3 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "division");
    UPDATE_STRING_DICT0( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain_division, tmp_assign_source_3 );
    tmp_assign_source_4 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "absolute_import");
    UPDATE_STRING_DICT0( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain_absolute_import, tmp_assign_source_4 );
    tmp_assign_source_5 = PyObject_GetAttrString(PyImport_ImportModule("__future__"), "print_function");
    UPDATE_STRING_DICT0( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain_print_function, tmp_assign_source_5 );
    tmp_assign_source_6 = LIST_COPY( const_list_str_plain_core_list );
    UPDATE_STRING_DICT1( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain_depends, tmp_assign_source_6 );
    tmp_assign_source_7 = LIST_COPY( const_list_f6e7aa5ecf966dc33f39bff68dc7a81a_list );
    UPDATE_STRING_DICT1( moduledict_numpy$random$info, (Nuitka_StringObject *)const_str_plain___all__, tmp_assign_source_7 );

    return MOD_RETURN_VALUE( module_numpy$random$info );
}
